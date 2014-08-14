#from TASSELpy.javaObj import javaObj,genericJavaObj
import TASSELpy.javaObj
from TASSELpy.utils.OrderedSet import lruOrderedSet
from functools import wraps,update_wrapper,partial
import numpy as np
import javabridge
import re

if not javabridge.get_env():
    from TASSELpy import TASSELbridge
    TASSELbridge.start()

java_imports = {'String':'java/lang/String'}
str_class = javabridge.get_env().find_class(java_imports['String'])
to_java_string = lambda x: javabridge.make_instance(java_imports['String'],
                                                    "(Ljava/lang/String;)V", x)
## Define numpy types that need to be converted to java arrays
def make_string_array(arr):
    java_arr = javabridge.get_env().make_object_array(len(arr),str_class)
    for i,s in enumerate(arr):
        javabridge.get_env().set_object_array_element(java_arr,
                    i,javabridge.get_env().new_string_utf(s))
    return java_arr

array_conversion_func_dict = {np.int8: javabridge.get_env().make_byte_array,
                              np.int32: javabridge.get_env().make_int_array,
                              np.int64: javabridge.get_env().make_long_array,
                              np.string_: make_string_array}

## Dictionary that automatically inserts both k->v and v->k under set
class bidirectional_dict(dict):
    ## Instantiates bidirectionary dictionary
    # @param args A bunch of pairs to be (key,values)
    def __init__(self, *args):
        super(bidirectional_dict,self).__init__()
        for k,v in args:
            self[k] = v
    def __setitem__(self,k,v):
        super(bidirectional_dict,self).__setitem__(k,v)
        super(bidirectional_dict,self).__setitem__(v,k)

## Define a set of equivalent python types in signatures
eq_types = bidirectional_dict((int,np.int32),(long,np.int64),
                              (str,unicode))
## Define a set of types that, while actually equivalent in python,
# should not be considered equivalent for signatures
segregate_types = bidirectional_dict((int,np.int64))

## Default-dict type dictionary to work with signatures
class signature_dict(dict):
    def __missing__(self, key):
        found = False
        ## Find the right key
        for k in self:
            if len(k) != len(key): continue
            use = True
            ## Check all arguments in key to see if everything
            # subclass instance of existing key
            for i,arg in enumerate(key):
                # Skip if NoneType
                if arg == type(None): continue
                # Check if the arg type should be segregated from the k[i] type
                if k[i] in segregate_types:
                    if arg == segregate_types[k[i]]:
                        use = False
                        break
                # Check if k[i] a subclass of this type in key
                if not issubclass(arg,k[i]):
                    if k[i] in eq_types:
                        if not (arg == eq_types[k[i]]):
                            use = False
                            break
                    else:
                        use = False
                        break
            # Set the value if appropriate
            if use:
                self[key] = self[k]
                found = True
                break
        if not found:
            raise KeyError("Arguments do not fit any signature")
        else:
            return self[key]
    

## Decorator class used to overload java wrapper functions
# that are non-constructor members of an instantiated class
class javaOverload(object):
    """
    Creates a function decorator for a javabridge function that
    is the member of a class

    Arguments:

    func_name -- The name of the java function
    args -- tuples of form (java_signature, (python arg types),post_process_func)
            e.g. ("(I)I",(int,),None)
            or ("(I)[L",(int,),lambda x: javabridge.get_env().get_long_array_elements(x))
    """
    def __init__(self, func_name, *args):
        """
        Creates a function decorator for a javabridge function that
        is the member of a class

        Arguments:

        func_name -- The name of the java function
        args -- tuples of form (java_signature, (python arg types),post_process_func)
                e.g. ("(I)I",(int,),None)
                or ("(I)[L",(int,),lambda x: javabridge.get_env().get_long_array_elements(x))
        """
        self.func_name = func_name
        ## Create signature dictionary of {(python args) -> function}
        self.func_dict = signature_dict()
        self.return_func_dict = signature_dict()
        for sig, pyargs, py_return in args:
            pyargs = tuple(map(self._process_pyarg, pyargs))
            self.func_dict[pyargs] = javabridge.make_method(func_name,
                                                    sig)
            if py_return is None:
                self.return_func_dict[pyargs] = lambda x: x
            else:
                self.return_func_dict[pyargs] = self._process_py_return(py_return)
    def _process_pyarg(self, x):
        if isinstance(x, tuple):
            #return getattr(__import__(x[0],globals(),locals(),[x[1]]),x[1])
            return getattr(__import__(x[0],globals(),locals()),x[1])
        else:
            return x
    def _process_py_return(self, x):
        if isinstance(x, tuple):
            #func = getattr(__import__(x[0],globals(),locals(),[x[1]]),x[1]).__init__
            func = getattr(__import__(x[0],globals(),locals()),x[1]).__init__
            return lambda y: func(obj = y)
        else:
            return x
    def __call__(self, f):
        @wraps(f)
        def wrapped_f(*args):
            if len(args) > 1:
                # Get the right function based on argument types
                key = tuple(map(type, args[1:]))
                # Convert any wrapped java items to their java objects
                args = list(args)
                args[1:] = map(lambda x: (x.o if isinstance(x,TASSELpy.javaObj.javaObj) else x),
                                   args[1:])
                return_val = self.func_dict[key](*args)
                if self.func_name != 'getClass':
                    return self.return_func_dict[key](return_val)
                else:
                    # Special method for getClass to put in generic type
                    return_obj = self.return_func_dict[key](return_val)
                    if not hasattr(return_obj, 'generic_dict'):
                        return return_obj
                    else:
                        return_obj.generic_dict['/@1/'] = type(args[0])
                        return return_obj
            else:
                return_val = self.func_dict[()](*args)
                return self.return_func_dict[()](return_val)
        return wrapped_f

## Decorator class used to overload constructors
class javaConstructorOverload(object):
    """
    Creates a function decorator for a javabridge function that is
    a constructor for an instantiated class

    Arguments:

    class_name -- The name of the java class, as in path/to/class
    args -- tuples of form (java signature,(python arg types))
            e.g. ("(I)V",(int,))
    """
    def __init__(self, class_name, *args):
        """
        Creates a function decorator for a javabridge function that is
        a constructor for an instantiated class

        Arguments:

        class_name -- The name of the java class, as in path/to/class
        args -- tuples of form (java signature,(python arg types))
                e.g. ("(I)V",(int,))
        """
        self.class_name = class_name
        ## Create signature dictionary of {(python args) -> function}
        self.func_dict = signature_dict()
        for sig, pyargs in args:
            pyargs = tuple(map(self._process_pyarg, pyargs))
            self.func_dict[pyargs] = javabridge.make_new(self.class_name,sig)
    def _process_pyarg(self, x):
        if isinstance(x, tuple):
            #return getattr(__import__(x[0],globals(),locals(),[x[1]]),x[1])
            return getattr(__import__(x[0],globals(),locals()),x[1])
        else:
            return x
    def __call__(self, f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            if 'obj' in kwargs:
                ## If wrapping existing java object, put in
                # raw Java object as attribute so that methods can
                # find it
                if isinstance(kwargs['obj'], unicode):
                    args[0].o = to_java_string(kwargs['obj'])
                else:
                    args[0].o = kwargs['obj']
            elif len(self.func_dict) == 0:
                ## Skip if there are no actual java functions being wrapped
                pass
            else:
                if len(args) > 1:
                    # Get the right function based on argument types
                    key = tuple(map(type, args[1:]))
                    # Convert any wrapped java items to their java objects
                    args = list(args)
                    #args[1:] = map(lambda x: (x.o if not hasattr(x,'toPrimative') else x.toPrimative()) \
                    #                    if isinstance(x,TASSELpy.javaObj.javaObj) else x,
                    #                   args[1:])
                    args[1:] = map(lambda x: (x.o if isinstance(x,TASSELpy.javaObj.javaObj) else x),
                                       args[1:])
                    self.func_dict[key](*args)
                else:
                    self.func_dict[()](*args)
            if 'generic' in kwargs:
                ## Put in the generic type dictionary if necessary
                args[0].generic_dict = dict(zip(map(lambda x: '/@%d/' % x,
                                                xrange(1,len(kwargs['generic'])+1)),
                                            kwargs['generic']))
            # Make the call from the function body
            f(*args, **kwargs)
        return wrapped_f


class javaStaticOverload(object):
    """
    Creates a function decorator for a javabridge static function

    Arguments:

    class_name -- The name of the java class containing the method, as in path/to/class
    func_name -- The name of the java function
    args -- tuples of form (java signature, (python arg types), post process function)
            e.g. ("(I)I",(int,),None)
            or ("(I)[L",(int,),lambda x: javabridge.get_env().get_long_array_elements(x))
    """
    def __init__(self, class_name, func_name, *args):
        """
        Creates a function decorator for a javabridge static function

        Arguments:

        class_name -- The name of the java class containing the method, as in path/to/class
        func_name -- The name of the java function
        args -- tuples of form (java signature, (python arg types), post process function)
                e.g. ("(I)I",(int,),None)
                or ("(I)[L",(int,),lambda x: javabridge.get_env().get_long_array_elements(x))
        """
        self.func_name = func_name
        self.class_name = class_name
        ## Create signature dictionary of {(python args) -> function}
        self.func_dict = signature_dict()
        self.return_func_dict = signature_dict()
        for sig, pyargs, py_return in args:
            self.func_dict[pyargs] = javabridge.make_static_call(self.class_name,
                                    self.func_name,sig)
            if py_return is None:
                self.return_func_dict[pyargs] = lambda x: x
            else:
                self.return_func_dict[pyargs] = py_return
    def _arg_convert(self, x):
        if isinstance(x, TASSELpy.javaObj.javaObj):
            return x.o
        elif isinstance(x, str):
            return to_java_string(x)
        else:
            return x
    def __call__(self, f):
        def wrapped_f(*args):
            # Get the right function based on argument types
            key = tuple(map(type,args))
            # Convert any wrapped java items to their java objects
            args = list(args)
            args = map(self._arg_convert, args)
            # Convert any numpy arrays to their java arrays
            if np.ndarray in key:
                args = map(lambda x: array_conversion_func_dict[x.dtype.type](x) \
                           if type(x) == np.ndarray else x, args)
            return_val = self.func_dict[key](*args)
            return self.return_func_dict[key](return_val)
        wrapped_f = update_wrapper(wrapped_f,f,
                                assigned=('__doc__','__name__','__module__'))
        wrapped_f = staticmethod(wrapped_f)
        return wrapped_f

## Decorator class used to overload java wrapper functions
# that are non-constructor members of an instantiated class
# and return and/or accept a generic type
class javaGenericOverload(object):
    """
    Creates a function decorator for a javabridge function that
    is the member of a class and returns and/or accepts a generic type

    Arguments:

    func_name -- The name of the java function
    args -- tuples of form (java_signature, (python arg types),post_process_func)
            Java signatures should have java/lang/Object where generic types go.
            
            In the Python arg types, a generic types specified as, say (type1,type2)
            in the generic argument of the constructor should be specified as a string
            "/@1/" or "/@2/", corresponding to type1 and type2 respectively.

            In the post_process_func, you can specify None or a function as usual in
            order to deal with pre-specified types. Alternatively, you can put in
            the string "/@1/" or whatever the corresponding string is for a given type
            in order to send the return object through the constructor of that type
            (e.g. type1(obj=x)). In the case of types that should receive generic arguments,
            you can specify a dictionary with 'type' and 'generic' keys. For instance,
            to send the return object to a wrapper class named MyClass that should receive
            type1 as its one and only generic type argument, you can put in the following
            dictionary:

            dict(type=MyClass, generic=("/@1/",))
    """
    def __init__(self, func_name, *args):
        """
        Creates a function decorator for a javabridge function that
        is the member of a class

        Arguments:

        func_name -- The name of the java function
        args -- tuples of form (java_signature, (python arg types or None),post_process_func)
                For java signature, put /@/ sign where the actual type of the generic should be placed.
                For python args/return type put None where it should be
                Note that if the returned type is the generic, the post-process function will
                cast to the specified type unless otherwise specified
                e.g. ("(/@/)I",(None,),None)
                or ("(/@/)[L",(None,),lambda x: javabridge.get_env().get_long_array_elements(x))
        """
        self.func_name = func_name
        # Store function parameters
        self.func_params = args
        # Set the sig_set dictionary
        self.sig_set = lruOrderedSet()
    def __call__(self, f):
        @wraps(f)
        def wrapped_f(*args):
            ## If the signature is not set, do it
            if args[0] not in self.sig_set:
                self.func_dict = signature_dict()
                self.return_func_dict = signature_dict()
                ## Set up signature dictionary ##
                for sig, pyargs, py_return in self.func_params:
                    ## Replace any instances of strings in the pyargs with the python type
                    pyargs = tuple(map(lambda x: (args[0].generic_dict[x] if \
                                        x in args[0].generic_dict else TASSELpy.javaObj.javaObj) if \
                                       type(x) == str else x,pyargs))
                    # Set func_dict entries
                    self.func_dict[pyargs] = javabridge.make_method(self.func_name,sig)
                    if type(py_return) == str:
                        ## If return function is replaced with string, meaning
                        # to instantiate generic type
                        if hasattr(args[0].generic_dict[py_return],'generic_dict'):
                            generic_tuple = tuple(map(lambda x: x[1],
                                    sorted(args[0].generic_dict[py_return].generic_dict.items())))
                            self.return_func_dict[pyargs] = lambda x: \
                              args[0].generic_dict[py_return](obj=x, generic=generic_tuple) if \
                              isinstance(x,javabridge.JB_Object) else \
                              (args[0].generic_dict[py_return](x) if x is not None else None)
                        else:
                            def da_return_func(x):
                                if isinstance(x, javabridge.JB_Object):
                                    return args[0].generic_dict[py_return](obj=x)
                                elif x is None:
                                    return None
                                else:
                                    try:
                                        return args[0].generic_dict[py_return](x)
                                    except KeyError:
                                        obj = None
                                        if isinstance(x, str) or isinstance(x,unicode):
                                            obj = javabridge.make_instance('java/lang/String',
                                                            '(Ljava/lang/String;)V',x)
                                        elif isinstance(x, int):
                                            obj = javabridge.make_instance('java/lang/Integer',
                                                            '(Ljava/lang/Integer;)V',x)
                                        elif isinstance(x, float):
                                            obj = javabridge.make_instance('java/lang/Double',
                                                            '(Ljava/lang/Double;)V',x)
                                        if obj is None: return obj
                                        else:
                                            return args[0].generic_dict[py_return](obj=obj)
                            self.return_func_dict[pyargs] = da_return_func
                    elif isinstance(py_return, dict):
                        ## If this is a dictionary, specify the generic type
                        # and make constructor call method
                        if 'type' not in py_return:
                            raise ValueError("Return type of object not given")
                        elif 'generic' not in py_return:
                            raise ValueError("Generic type(s) for return object not given")
                        self.return_func_dict[pyargs] = \
                              lambda x: py_return['type'](obj=x,
                                generic=tuple(map(lambda y: args[0].generic_dict[y] if \
                                                  isinstance(y,str) else y,
                                                  py_return['generic']))) if \
                                        isinstance(x,javabridge.JB_Object) else x
                    elif py_return is None:
                        ## If no return function specified, return raw output
                        self.return_func_dict[pyargs] = lambda x: x
                    else:
                        ## If function specified, use that
                        self.return_func_dict[pyargs] = py_return
                # Set sig_set variable to true
                self.sig_set.add(args[0])
            ## Run the function ##
            if len(args) > 1:
                # Get the right function based on argument types
                key = tuple(map(type, args[1:]))
                # Convert any wrapped java items to their java objects
                args = list(args)
                #args[1:] = map(lambda x: (x.o if not hasattr(x,'toPrimative') else x.toPrimative()) \
                #                    if isinstance(x,TASSELpy.javaObj.javaObj) else x,
                #                   args[1:])
                args[1:] = map(lambda x: (x.o if isinstance(x,TASSELpy.javaObj.javaObj) else x),
                                   args[1:])
                return_val = self.func_dict[key](*args)
                return self.return_func_dict[key](return_val)
            else:
                return_val = self.func_dict[()](*args)
                return self.return_func_dict[()](return_val)
        return wrapped_f
