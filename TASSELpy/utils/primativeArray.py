from TASSELpy.javaObj import javaArray
from TASSELpy.java.lang.reflect.Array import Array
from TASSELpy.java.lang.Byte import metaByte
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Long import metaLong
from TASSELpy.java.lang.Float import metaFloat
from TASSELpy.java.lang.Double import metaDouble
from abc import ABCMeta
import javabridge
import numpy as np
import re

class meta_byte_array:
    __metaclass__ = ABCMeta
    java_arr_type = None
    @classmethod
    def __subclasshook__(cls, C):
        if cls.java_arr_type is None:
            cls.java_arr_type = javaPrimativeArray.get_array_type('byte')
        if C == np.ndarray:
            return True
        elif issubclass(C, cls.java_arr_type):
            return True
        else:
            return False

class meta_int_array:
    __metaclass__ = ABCMeta
    java_arr_type = None
    @classmethod
    def __subclasshook__(cls, C):
        if cls.java_arr_type is None:
            cls.java_arr_type = javaPrimativeArray.get_array_type('int')
        if C == np.ndarray:
            return True
        elif issubclass(C, cls.java_arr_type):
            return True
        else:
            return False

class meta_long_array:
    __metaclass__ = ABCMeta
    java_arr_type = None
    @classmethod
    def __subclasshook__(cls, C):
        if cls.java_arr_type is None:
            cls.java_arr_type = javaPrimativeArray.get_array_type('long')
        if C == np.ndarray:
            return True
        elif issubclass(C, cls.java_arr_type):
            return True
        else:
            return False
        
class meta_float_array:
    __metaclass__ = ABCMeta
    java_arr_type = None
    @classmethod
    def __subclasshook__(cls, C):
        if cls.java_arr_type is None:
            cls.java_arr_type = javaPrimativeArray.get_array_type('float')
        if C == np.ndarray:
            return True
        elif issubclass(C, cls.java_arr_type):
            return True
        else:
            return False

class meta_double_array:
    __metaclass__ = ABCMeta
    java_arr_type = None
    @classmethod
    def __subclasshook__(cls, C):
        if cls.java_arr_type is None:
            cls.java_arr_type = javaPrimativeArray.get_array_type('double')
        if C == np.ndarray:
            return True
        elif issubclass(C, cls.java_arr_type):
            return True
        else:
            return False
## Java Object to represent arrays of wrapped primatives
class javaPrimativeArray(javaArray):
    """
    Wraps arrays of primative types
    """
    def __setitem__(self, key, val):
        # Check if value member of baseClass
        if not isinstance(val,self.baseClass):
            raise TypeError("Value not an instance of %s." % str(self.baseClass))
        if key < 0:
            key = len(self) + key
        self.setter(key, val)
    def __getitem__(self, key):
        if key < 0:
            key = len(self) + key
        return self.getter(key)
    ## Makes a numpy array copy of the Java primative array
    # @return numpy array containing data
    def to_numpy_array(self):
        """
        Makes a numpy array copy of the Java primative array

        Returns:

        Numpy array containing data
        """
        if self.dim == 1:
            _dtype = None
            if self.baseClass == metaByte: _dtype = np.int8
            elif self.baseClass == metaBoolean: _dtype=np.bool
            elif self.baseClass == metaInteger: _dtype=np.int32
            elif self.baseClass == metaLong: _dtype=np.int64
            elif self.baseClass == metaFloat: _dtype=np.float32
            elif self.baseClass == metaDouble: _dtype=np.float64
            return np.array([x for x in self],dtype=_dtype)
        elif self.dim == 2:
            _dtype = None
            if self.ref_type == metaByte: _dtype = np.int8
            elif self.ref_type == metaBoolean: _dtype=np.bool
            elif self.ref_type == metaInteger: _dtype=np.int32
            elif self.ref_type == metaLong: _dtype=np.int64
            elif self.ref_type == metaFloat: _dtype=np.float32
            elif self.ref_type == metaDouble: _dtype=np.float64
            arr = np.zeros((len(self),len(self[0])),dtype=_dtype)
            for i,x in enumerate(self):
                arr[i,:] = np.array([y for y in x],dtype=_dtype)
            return arr
        else:
            raise ValueError("Dimensions over 2 not implemented")
    @staticmethod
    def get_array_type(primative_name):
        if primative_name == 'byte':
            arr_type = type('byte', (javaPrimativeArray,),
                            {'baseClass':metaByte})
        elif primative_name == 'boolean':
            arr_type = type('boolean',(javaPrimativeArray,),
                            {'baseClass':metaBoolean})
        elif primative_name == 'int':
            arr_type = type('int',(javaPrimativeArray,),
                            {'baseClass':metaInteger})
        elif primative_name == 'long':
            arr_type = type('long',(javaPrimativeArray,),
                            {'baseClass':metaLong})
        elif primative_name == 'float':
            arr_type = type('float',(javaPrimativeArray,),
                            {'baseClass':metaFloat})
        elif primative_name == 'double':
            arr_type = type('double',(javaPrimativeArray,),
                            {'baseClass':metaDouble})
        else:
            raise ValueError("%s is not an implemented java primative type" % primative_name)
        arr_type.dim = 1
        arr_type.primative = True
        return arr_type()
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
        return javaPrimativeArray.to_wrapped_array(arr_instance, cls)
    ## Makes a wrapped java array for some java primative
    # @param primative_name The name of the java primative (e.g. 'int')
    # @param length The length of the array
    # @return The wrapped java array
    @staticmethod
    def make_array(primative_name, length):
        """
        Makes a wrapped java array for some java primative

        Arguments:

        primative_name -- The name of the java primative (e.g. 'int')
        length -- The length of the array

        Returns:

        The wrapped java array
        """
        ## Create the java array and the array type
        if primative_name == 'byte':
            java_arr = javabridge.get_env().make_byte_array(np.zeros(length,dtype=np.uint8))
            arr_type = type('byte', (javaPrimativeArray,),
                            {'baseClass':metaByte,'getter':Array.getByte,
                             'setter':Array.setByte})
        elif primative_name == 'boolean':
            java_arr = javabridge.get_env().make_boolean_array(np.zeros(length,dtype=np.bool))
            arr_type = type('boolean',(javaPrimativeArray,),
                            {'baseClass':metaBoolean,'getter':Array.getBoolean,
                             'setter':Array.setBoolean})
        elif primative_name == 'int':
            java_arr = javabridge.get_env().make_int_array(np.zeros(length,dtype=np.int32))
            arr_type = type('int',(javaPrimativeArray,),
                            {'baseClass':metaInteger,'getter':Array.getInt,
                             'setter':Array.setInt})
        elif primative_name == 'long':
            java_arr = javabridge.get_env().make_long_array(np.zeros(length,dtype=np.int64))
            arr_type = type('long',(javaPrimativeArray,),
                            {'baseClass':metaLong,'getter':Array.getLong,
                             'setter':Array.setLong})
        elif primative_name == 'float':
            java_arr = javabridge.get_env().make_float_array(np.zeros(length,dtype=np.float32))
            arr_type = type('float',(javaPrimativeArray,),
                            {'baseClass':metaFloat, 'getter':Array.getFloat,
                             'setter':Array.setFloat})
        elif primative_name == 'double':
            java_arr = javabridge.get_env().make_double_array(np.zeros(length,dtype=np.float64))
            arr_type = type('double',(javaPrimativeArray,),
                            {'baseClass':metaDouble,'getter':Array.getDouble,
                             'setter':Array.setDouble})
        else:
            raise ValueError("%s is not an implemented java primative type" % primative_name)
        ## Create the array python object
        arr_type.dim = 1
        arr_type.primative = True
        py_arr_obj = arr_type()
        py_arr_obj.o = java_arr
        py_arr_obj._java_name = javabridge.get_env().get_object_class(java_arr)
        return py_arr_obj
    ## Makes an empty wrapped java array that can accept the type of other wrapped java arrays
    # of a primative type: e.g. double[][]
    # @param rows The number of rows that should be in the array (the first dimension
    # @param cols The number of columns that should be in the array (if not specified, the
    # array objects will not be instantiated at these locations
    # @return An instance of an array of arrays
    @staticmethod
    def make_dbl_array(primative_name, rows, cols=None):
        """
        Makes an empty wrapped java array that can accept the type of other
        wrapped java arrays of a primative type: e.g. double[][]

        Arguments:

        rows -- The number of rows that should be in the array (the first dimension)
        cols -- The number of columns that should be in the array (if not specified, the
                array objects will not be instantiated at these locations)

        Returns:

        An instance of an array of arrays
        """
        array_array = javaPrimativeArray.make_array(primative_name,1).getArray(rows)
        if cols:
            for i in xrange(rows):
                array_array[i] = javaPrimativeArray.make_array(primative_name, cols)
        return array_array
    ## Sends a returned java object to a wrapped java array
    # @param primative_name The name of the java primative (e.g. 'int')
    # @param obj The java object
    # @return The wrapped java array
    @staticmethod
    def make_array_from_obj(primative_name, obj):
        """
        Sends a returned java object of a wrapped java array

        Arguments:

        primative_name -- The name of the java primative (e.g. 'int')
        obj -- The java object

        Returns:

        The wrapped java array
        """
        ## Create the java array and the array type
        if primative_name == 'byte':
            arr_type = type('byte', (javaPrimativeArray,),
                            {'baseClass':metaByte,'getter':Array.getByte,
                             'setter':Array.setByte})
        elif primative_name == 'boolean':
            arr_type = type('boolean',(javaPrimativeArray,),
                            {'baseClass':metaBoolean,'getter':Array.getBoolean,
                             'setter':Array.setBoolean})
        elif primative_name == 'int':
            arr_type = type('int',(javaPrimativeArray,),
                            {'baseClass':metaInteger,'getter':Array.getInt,
                             'setter':Array.setInt})
        elif primative_name == 'long':
            arr_type = type('long',(javaPrimativeArray,),
                            {'baseClass':metaLong,'getter':Array.getLong,
                             'setter':Array.setLong})
        elif primative_name == 'float':
            arr_type = type('float',(javaPrimativeArray,),
                            {'baseClass':metaFloat, 'getter':Array.getFloat,
                             'setter':Array.setFloat})
        elif primative_name == 'double':
            arr_type = type('double',(javaPrimativeArray,),
                            {'baseClass':metaDouble,'getter':Array.getDouble,
                             'setter':Array.setDouble})
        else:
            raise ValueError("%s is not an implemented java primative type" % primative_name)
        ## Create the array python object
        arr_type.dim = 1
        arr_type.primative = True
        py_arr_obj = arr_type()
        py_arr_obj.o = obj
        py_arr_obj._java_name = javabridge.get_env().get_object_class(obj)
        return py_arr_obj
    ## Wraps a current array
    # @param arr_instance A java object containing the array
    # @param pyType The type of the javaObj.
    # @return The wrapped java array
    @staticmethod
    def to_wrapped_array(arr_instance, pyType):
        """
        Wraps a current array

        Arguments:

        arr_instance -- A java object containing the array
        pyType -- The type of the javaObj

        Returns:

        The wrapped java array
        """
        pyClass_base = re.search('(?<=\.)[a-zA-Z0-9_]+(?=\'\>)',str(pyType)).group()
        func_dict = {}
        if pyClass_base == 'metaByte':
            func_dict = {'getter':Array.getByte,
                             'setter':Array.setByte}
        elif pyClass_base == 'metaBoolean':
            func_dict = {'getter':Array.getBoolean,
                             'setter':Array.setBoolean}
        elif pyClass_base == 'metaInteger':
            func_dict = {'getter':Array.getInt,
                             'setter':Array.set}
        elif pyClass_base == 'metaLong':
            func_dict = {'getter':Array.getLong,
                             'setter':Array.setLong}
        elif pyClass_base == 'metaFloat':
            func_dict = {'getter':Array.getFloat,
                             'setter':Array.setFloat}
        elif pyClass_base == 'metaDouble':
            func_dict = {'getter':Array.getDouble,
                             'setter':Array.setDouble}
        if not issubclass(pyType,javaArray):
            primative_name = re.search('(?<=meta).+',pyClass_base).group().lower()
            if primative_name == 'integer': primative_name = primative_name[:3]
            return javaPrimativeArray.make_array_from_obj(primative_name, arr_instance)
        elif pyType.dim == 1:
            ## Create the array python object
            arr_type = None
            arr_type = type(pyClass_base,(javaArray,),{'baseClass':pyType})
            if not hasattr(pyType, 'ref_type'):
                arr_type.ref_type = pyType.baseClass
            else:
                arr_type.ref_type = pyType.ref_type
            arr_type.dim = pyType.dim + 1
            py_arr_obj = arr_type()
            py_arr_obj.o = arr_instance
            py_arr_obj._java_name = javabridge.get_env().get_object_class(arr_instance)
            if issubclass(pyType, javaArray):
                py_arr_obj.pyArr = map(lambda x: javaPrimativeArray.make_array_from_obj(pyClass_base,
                                                                                        x),
                                       javabridge.get_env().get_object_array_elements(arr_instance))
            return py_arr_obj
        elif pyType.dim > 1:
            raise ValueError("Dimensions greater than 2 not supported for primative types")
        else:
            raise ValueError("Invalid input")
    
            
