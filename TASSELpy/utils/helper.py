import re
import javabridge

## Dictionary holding the symbols for primatives in javabridge signatures
primative_dict = {'boolean':'Z','byte':'B','char':'C','short':'S',
                  'int':'I','long':'J','float':'F','double':'D',
                  'void':'V'}

## Constructs the signature needed by javabridge for a function
# @param args A list of argument types for the function. If an array is specified, the
# class name should end with []. The begninning L and ; will be added
# if not already present. Otherwise, just put in the primative name (i.e. int, char, etc)
# @param return_type The return type for the function, specified in the same way as the arguments 
# @return The signature for the java method
def make_sig(args,return_type):
    """
    Constructs the signature needed by javabridge for a function

    Arguments:

    args -- A list of argument types for the function. If an array is specified, the class name
            should end with []. The beginning L and end ; will be added if not already present.
            Otherwise, just put in the primative name (i.e. int char, etc)
    return_type -- The return type of the function, specified in the same way as the arguments

    Returns:

    The signature for the java method
    """
    # Run arguments through
    for i,arg in enumerate(args):
        array = False
        n_array = 0
        if arg in primative_dict or (re.match(r'[a-z]+(?=\[)',arg) and \
                re.match(r'[a-z]+(?=\[)',arg).group() in primative_dict):
            # If this is a primative
            if arg.endswith('[]'):
                # If this should be an array
                array = True
                while arg.endswith('[]'):
                    arg = arg[:-2]
                    n_array += 1
            # Turn into signature form
            if array:
                args[i] = "%s%s" % ('['*n_array,primative_dict[arg])
            else:
                args[i] = primative_dict[arg]
        elif '/' in arg:
            # If this is a class name
            if arg.endswith('[]'):
                # If this should be an array
                array = True
                while args[i].endswith('[]'):
                    args[i] = args[i][:-2]
                    n_array += 1
            if not args[i].startswith('L'):
                # Check that it begins with L
                args[i] = "L%s" % args[i]
            if not args[i].endswith(';'):
                # Check that it ends with a semicolon
                args[i] = "%s;" % args[i]
            if array:
                # Put in array if necessary
                args[i] = "%s%s" % ('['*n_array,args[i])
        else:
            raise ValueError("%s is not a valid type!" % arg)
    # Run return type through
    array = False
    n_array = 0
    if return_type in primative_dict or (re.match(r'[a-z]+(?=\[)',return_type) and \
                re.match(r'[a-z]+(?=\[)',return_type).group() in primative_dict):
        # If this is a primative
        if return_type.endswith('[]'):
            # If this should be an array
            array = True
            while return_type.endswith('[]'):
                return_type = return_type[:-2]
                n_array += 1
        # Turn into signature form
        if array:
            return_type = "%s%s" % ('['*n_array,primative_dict[return_type])
        else:
            return_type = primative_dict[return_type]
    elif '/' in return_type:
        # If this is a class name
        if return_type.endswith('[]'):
            # If this should be an array
            array = True
            while return_type.endswith('[]'):
                return_type = return_type[:-2]
                n_array += 1
        if not return_type.startswith('L'):
            # Check that it begins with L
            return_type = "L%s" % return_type
        if not return_type.endswith(';'):
            # Check that it ends with a semicolon
            return_type = "%s;" % return_type
        if array:
            # Put in array if necessary
            return_type = "%s%s" % ('['*n_array,return_type)
    else:
        raise ValueError("%s is not a valid type!" % return_type)
    ## Return the signature
    return "(%s)%s" % (''.join(args),return_type)

## Constructs the signature needed by javabridge for a constructor function
# @param args A list of argument types for the function. If an array is specified, the
# class name should end with []. The begninning L and ; will be added
# if not already present. Otherwise, just put in the primative name (i.e. int, char, etc)
# @return The signature for the java constructor
def make_constructor_sig(args):
    """
    Constructs the signature needed by javabridge for a function

    Arguments:

    args -- A list of argument types for the function. If an array is specified, the class name
            should end with []. The beginning L and end ; will be added if not already present.
            Otherwise, just put in the primative name (i.e. int char, etc)

    Returns:

    The signature for the java constructor
    """
    # Run arguments through
    for i,arg in enumerate(args):
        array = False
        if arg in primative_dict or arg[:-2] in primative_dict:
            # If this is a primative
            if arg.endswith('[]'):
                # If this should be an array
                arg = arg[:-2]
                array = True
            # Turn into signature form
            if array:
                args[i] = "[%s" % primative_dict[arg]
            else:
                args[i] = primative_dict[arg]
        elif '/' in arg:
            # If this is a class name
            if arg.endswith('[]'):
                # If this should be an array
                args[i] = arg[:-2]
                array = True
            if not args[i].startswith('L'):
                # Check that it begins with L
                args[i] = "L%s" % args[i]
            if not args[i].endswith(';'):
                # Check that it ends with a semicolon
                args[i] = "%s;" % args[i]
            if array:
                # Put in array if necessary
                args[i] = "[%s" % args[i]
        else:
            raise ValueError("%s is not a valid type!" % arg)
    ## Return the signature
    return "(%s)V" % (''.join(args))

## Function to use in case a value returned from javabridge is a python
# primative that needs to be sent back to a java object before further processing
# @param prim_val The python primative value
# @return A wrapped java object of the appropriate type (String, Integer, or Double)
def send_to_java(prim_val):
    if isinstance(prim_val, str) or isinstance(prim_val,unicode):
        return javabridge.make_instance("java/lang/String",
                                       "(Ljava/lang/String;)V",prim_val)
    elif isinstance(prim_val, int):
        return javabridge.make_instance("java/lang/Integer",
                                       "(Ljava/lang/Integer;)V",prim_val)
    elif isinstance(prim_val, float):
        return javabridge.make_instance("java/lang/Double",
                                       "(Ljava/lang/Double;)V",prim_val)
    else:
        return prim_val
