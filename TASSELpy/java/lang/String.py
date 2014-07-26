from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.javaObj import javaObj, javaArray
from TASSELpy.java.lang.Object import Object
from TASSELpy.utils.helper import make_sig
from abc import ABCMeta
import numpy as np
import javabridge

java_imports = {'String':'java/lang/String'}

class metaString:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C,str):
            return True
        elif issubclass(C,np.string_):
            return True
        elif issubclass(C,unicode):
            return True
        elif issubclass(C, String):
            return True
        else:
            return False
## Wrapper class for java.lang.String
class String(Object):
    """
    Wrapper class for java.lang.String
    """
    _java_name = java_imports['String']
    @javaConstructorOverload(java_imports['String'],
        (make_sig([],'void'),()),
        (make_sig([java_imports['String']],'void'),(metaString,)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a new String

        Signatures:

        String()
        String(String original)

        Arguments:

        String(String original)
           original -- The string to copy over
        """
        pass
    def __repr__(self):
        return "String('%s')" % self.toString()
    def __eq__(self, other):
        if isinstance(other, javaObj):
            return super(String, self).__eq__(other)
        elif isinstance(other, metaString):
            return (self.toString() == other)
        else:
            return False
    ## Gets an empty wrapped java array that can accept the type of the wrapped
    # java object
    # @param size The size of the array
    # @return An instance of the array of the given size
    @classmethod
    def getArray(cls, size):
        """
        Gets an empty wrapped java array that can accept the type of the wrapped
        java object

        Arguments:

        size -- the size of the array

        Returns:

        An instance of the array of the given size
        """
        return String.make_array(size, pyType=metaString)
    ## Gets an empty wrapped java array that can accept the type of other wrapped java String arrays
    # i.e. String[][]
    # @param rows The number of rows that should be in the array (the first dimension
    # @param cols The number of columns that should be in the array (if not specified, the
    # array objects will not be instantiated at these locations
    # @return An instance of an array of arrays
    @classmethod
    def getDblArray(cls, rows, cols=None):
        """
        Gets an empty wrapped java array that can accept the type of other wrapped java String arrays:
        i.e. String[][]

        Arguments:

        rows -- The number of rows that should be in the array (the first dimension)
        cols -- The number of columns that should be in the array (if not specified, the
                array objects will not be instantiated at these locations

        Returns:

        An instance of an array of arrays
        """
        array_array = String.make_array(1, pyType=metaString).getArray(rows)
        if cols:
            for i in xrange(rows):
                array_array[i] = String.make_array(cols, pyType=metaString)
        return array_array
    ## Wraps a java array of this class's type
    # @param arr_instance The java array
    # @return The wrapped java array
    @classmethod
    def wrap_existing_array(cls, arr_instance):
        """
        Wraps a java array of this class's type

        Arguments:

        arr_instance -- The java array

        Returns:

        The wrapped java array
        """
        def setter(self, key, val):
            if not isinstance(val, self.baseClass):
                raise TypeError("Value not an instance of %s." % str(self.baseClass))
            elif not isinstance(val, String):
                val = String(val)
            self.pyArr[key] = val
            if key < 0:
                key = len(self) + key
            javabridge.get_env().set_object_array_element(self.o,
                            key, val.o)
        arr = javaArray.to_wrapped_array(arr_instance, String, setter=setter)
        arr.baseClass = metaString
        return arr
    ## Makes a wrapped java array for the string class
    # @param length The length of the array to make
    # @param pyType The type of the javaObj. This must be passed unless using a javaObj instance to
    # make the array
    # @return The wrapped java array
    @staticmethod
    def make_array(length, pyType=None):
        """
        Makes a wrapped java array for some java class

        Arguments:

        length -- The length of the array to make
        pyType -- The type of the javaObj. This must be passed unless using a javaObj instance to make
                  the array

        Returns:

        The wrapped java array
        """
        java_class = javabridge.get_env().find_class(java_imports['String'])
        pyClass_base = 'metaString'
        ## Instantiate java array
        java_arr = javabridge.get_env().make_object_array(length,java_class)
        ## Create the array type
        def setter(self, key, val):
            if not isinstance(val, self.baseClass):
                raise TypeError("Value not an instance of %s." % str(self.baseClass))
            elif not isinstance(val, String):
                val = String(val)
            self.pyArr[key] = val
            if key < 0:
                key = len(self) + key
            javabridge.get_env().set_object_array_element(self.o,
                            key, val.o)
        arr_type = type(pyClass_base,(javaArray,),{'baseClass':pyType, '__setitem__':setter})
        ## Create the array python object
        if issubclass(arr_type.baseClass,javaArray):
            if pyType is None:
                raise ValueError("Python type must be specified if making array of arrays")
            else:
                if not hasattr(pyType, ref_type):
                    arr_type.ref_type = pyType.baseClass
                else:
                    arr_type.ref_type = pyType.ref_type
            arr_type.dim = pyType.dim + 1
        else:
            arr_type.dim = 1
        py_arr_obj = arr_type()
        py_arr_obj.o = java_arr
        py_arr_obj._java_name = javabridge.get_env().get_object_class(java_arr)
        py_arr_obj.pyArr = [None for x in xrange(length)]
        return py_arr_obj
