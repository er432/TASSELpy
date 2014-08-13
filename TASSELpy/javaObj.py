from abc import ABCMeta
from TASSELpy.utils.helper import make_sig
from functools import wraps
import numpy as np
import javabridge
import re

java_imports = {'Object':'java/lang/Object',
                'String':'java/lang/String'}


class javaObj(object):
    #__metaclass__ = ABCMeta
    _java_name = java_imports['Object']
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
        return javaArray.make_array(cls._java_name, size, pyType=cls)
    ## Gets an empty wrapped java array that can accept the type of other wrapped java arrays
    # i.e. Object[][]
    # @param rows The number of rows that should be in the array (the first dimension
    # @param cols The number of columns that should be in the array (if not specified, the
    # array objects will not be instantiated at these locations
    # @return An instance of an array of arrays
    @classmethod
    def getDblArray(cls, rows, cols=None):
        """
        Gets an empty wrapped java array that can accept the type of other wrapped java arrays:
        i.e. Object[][]

        Arguments:

        rows -- The number of rows that should be in the array (the first dimension)
        cols -- The number of columns that should be in the array (if not specified, the
                array objects will not be instantiated at these locations

        Returns:

        An instance of an array of arrays
        """
        array_array = javaArray.make_array(cls._java_name, 1, pyType=cls).\
            getArray(rows)
        if cols:
            for i in xrange(rows):
                array_array[i] = javaArray.make_array(cls._java_name, cols, pyType=cls)
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
        return javaArray.to_wrapped_array(arr_instance, cls)

## Java object that can accept type in angle brackets
class genericJavaObj(javaObj):
    """
    Base class for all java object wrappers that you want to accept angle bracket arguments
    """
    def __init__(self, *args, **kwargs):
        """
        Sets the type of elements that would be given by angle brackets in java
        i.e. MyClass<String> myobj

        Arguments:

        generic -- wrapper class
        """
        if 'generic' in kwargs:
            self.generic_dict = dict(zip(map(lambda x: '/@%d/' % x,
                                        xrange(1,len(kwargs['generic'])+1)),
                                        kwargs['generic']))
        else:
            self.generic_dict = {'/@1/':javaObj}        


## Java Object to represent arrays of wrapped objects
class javaArray(javaObj):
    """
    Base class for arrays of wrapped objects
    """
    def __setitem__(self, key, val):
        # Check if value member of baseClass
        if isinstance(val, javaArray):
            if val.dim != (self.dim - 1):
                raise TypeError("Value is not of correct dimension")
            if val.dim == 1 and val.baseClass != self.ref_type:
                raise TypeError("Value is not of correct reference type")
            elif val.dim > 1 and val.ref_type != self.ref_type:
                raise TypeError("Value is not of correct reference type")
        elif not isinstance(val,self.baseClass):
            raise TypeError("Value not an instance of %s." % str(self.baseClass))
        self.pyArr[key] = val
        if key < 0:
            key = len(self) + key
        javabridge.get_env().set_object_array_element(self.o,
                        key, val.o)
    def __getitem__(self, key):
        return self.pyArr[key]
    def __instancecheck__(self,x):
        return self.__subclasscheck__(type(x))
    def __subclasscheck__(self, subclass):
        if not isinstance(subclass,type):
            if isinstance(subclass, javaArray):
                if subclass.dim == self.dim:
                    if self.dim == 1:
                        return self.baseClass == subclass.baseClass
                    else:
                        return self.ref_type == subclass.ref_type
                else: return False
            else:
                return False
        elif issubclass(subclass,javaArray):
            if subclass.dim == self.dim:
                if self.dim == 1:
                    if self.baseClass == subclass.baseClass:
                        return True
                    else:
                        return issubclass(self.baseClass,subclass.baseClass)
                else:
                    if self.ref_type == subclass.ref_type:
                        return True
                    else:
                        return issubclass(self.ref_type,subclass.ref_type)
            else: return False
        else:
            return False
    def __len__(self):
        return javabridge.static_call('java/lang/reflect/Array','getLength',
                                      make_sig([java_imports['Object']],'int'),
                                      self.o)
    def __iter__(self):
        for i in xrange(len(self)):
            yield self[i]
    def __repr__(self):
        if hasattr(self, 'o'):
            if len(self) <= 5:
                return "javaArray([%s])" % ", ".join(map(str, self))
            else:
                return "javaArray([%s, %s, ..., %s, %s])" % tuple(map(str, (self[0], self[1],
                                                           self[-2], self[-1])))
        else:
            return "<class javaArray.%s>" % self.baseClass
    ## Makes a wrapped java array for some java class
    # @param Class_instance Either an instance of a javaObj, an instance of a javabridge.JB_Object,
    # an instance of javabridge._javabridge.JB_Class, or the name of a java class as path/to/class
    # @param pyType The type of the javaObj. This must be passed unless using a javaObj instance to
    # make the array
    # @return The wrapped java array
    @staticmethod
    def make_array(Class_instance, length, pyType=None):
        """
        Makes a wrapped java array for some java class

        Arguments:

        Class_instance -- Either an instance of a javaObj, an instance of a javabridge.JB_Object,
                          an instance of javabridge._javabridge.JB_Class, or the name of a java class
                          as path/to/class
        pyType -- The type of the javaObj. This must be passed unless using a javaObj instance to make
                  the array

        Returns:

        The wrapped java array
        """
        ## Get the java class object
        if isinstance(Class_instance,javaObj):
            java_class = javabridge.get_env().get_object_class(Class_instance.o)
            pyClass_base = re.search('(?<=\.)[a-zA-Z0-9_]+(?=\'\>)',str(type(Class_instance))).group()
        elif isinstance(Class_instance, javabridge.JB_Object):
            java_class = javabridge.get_env().get_object_class(Class_instance)
            if pyType is None:
                raise ValueError("Python type must be specified if passing JB_Object")
            else:
                pyClass_base = re.search('(?<=\.)[a-zA-Z0-9_]+(?=\'\>)',str(pyType)).group()
        elif isinstance(Class_instance, javabridge._javabridge.JB_Class):
            java_class = Class_instance
            if pyType is None:
                raise ValueError("Python type must be specified if passing JB_Class")
            else:
                pyClass_base = re.search('(?<=\.)[a-zA-Z0-9_]+(?=\'\>)',str(pyType)).group()
        elif isinstance(Class_instance,str):
            java_class = javabridge.get_env().find_class(Class_instance)
            if pyType is None:
                raise ValueError("Python type must be specified if passing Java Class name")
            else:
                pyClass_base = re.search('(?<=\.)[a-zA-Z0-9_]+(?=\'\>)',str(pyType)).group()
        else:
            raise ValueError("Class_instance must be a wrapped java object or name of java class")
        ## Instantiate java array
        java_arr = javabridge.get_env().make_object_array(length,java_class)
        ## Create the array type
        if pyType is None:
            arr_type = type(pyClass_base,(javaArray,),{'baseClass':type(Class_instance)})
        else:
            arr_type = type(pyClass_base,(javaArray,),{'baseClass':pyType})
        ## Create the array python object
        if issubclass(arr_type.baseClass,javaArray):
            if pyType is None:
                raise ValueError("Python type must be specified if making array of arrays")
            else:
                if not hasattr(pyType, 'ref_type'):
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
    @staticmethod
    def get_array_type(Class):
        pyClass_base = re.search('(?<=\.)[a-zA-Z0-9_]+(?=\'\>)',str(Class)).group()
        if not isinstance(Class, type):
            if isinstance(Class, javaArray):
                return type(pyClass_base,(javaArray,),{'baseClass':Class,
                                                   'dim': Class.dim + 1,
                                                   'ref_type':Class.baseClass})()
            else:
                raise ValueError("You must input a class")
        if issubclass(Class, javaArray):
            return type(pyClass_base,(javaArray,),{'baseClass':Class,
                                                   'dim': Class.dim + 1})()
        else:
            return type(pyClass_base,(javaArray,),{'baseClass':Class, 'dim': 1})()
    ## Wraps a current array
    # @param arr_instance A java object containing the array
    # @param pyType The type of the javaObj.
    # @return The wrapped java array
    @staticmethod
    def to_wrapped_array(arr_instance, pyType, setter=None):
        """
        Wraps a current array

        Arguments:

        arr_instance -- A java object containing the array
        pyType -- The type of the javaObj

        Returns:

        The wrapped java array
        """
        pyClass_base = re.search('(?<=\.)[a-zA-Z0-9_]+(?=\'\>)',str(pyType)).group()
        if setter is None:
            arr_type = type(pyClass_base,(javaArray,),{'baseClass':pyType})
        else:
            arr_type = type(pyClass_base,(javaArray,),{'baseClass':pyType,'__setitem__':setter})
        ## Create the array python object
        if issubclass(arr_type.baseClass,javaArray):
            if not hasattr(pyType, 'ref_type'):
                arr_type.ref_type = pyType.baseClass
            else:
                arr_type.ref_type = pyType.ref_type
            arr_type.dim = pyType.dim + 1
        else:
            arr_type.dim = 1
        py_arr_obj = arr_type()
        py_arr_obj.o = arr_instance
        py_arr_obj._java_name = javabridge.get_env().get_object_class(arr_instance)
        if not issubclass(pyType, javaArray):
            py_arr_obj.pyArr = map(lambda x: pyType(obj=x),
                           javabridge.get_env().get_object_array_elements(arr_instance))
        else:
            py_arr_obj.pyArr = map(lambda x: pyType.to_wrapped_array(x, pyType.baseClass),
                                   javabridge.get_env().get_object_array_elements(arr_instance))
        return py_arr_obj
    ## Makes a numpy array copy of the Java array
    # @return numpy array containing data
    def to_numpy_array(self):
        """
        Makes a numpy array copy of the Java primative array

        Returns:

        Numpy array containing data
        """
        if self.dim == 1:
            return np.array([x for x in self])
        elif self.dim == 2:
            arr = []
            for i,x in enumerate(self):
                arr.append(np.array([y for y in x]))
            arr = np.array(arr)
            return arr
        else:
            raise ValueError("Dimensions over 2 not implemented")

"""
import os
from TASSELpy.TASSELbridge import TASSELbridge
home_dir=os.path.expanduser('~')
tassel_dir=os.path.join(home_dir,'bioinformatics','tassel5-standalone')
geno_file=os.path.join(tassel_dir,'TASSELTutorialData','data','mdp_genotype.hmp.txt')
TASSELbridge.start(tassel_dir)
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable

genoTable = ImportUtils.readGuessFormat(geno_file)
genoTable.genotype(0,0)
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.net.maizegenetics.taxa.TaxaListBuilder import TaxaListBuilder
from TASSELpy.javaObj import javaArray
#arr = javaArray.make_array(Taxon('test'),2)
arr = Taxon.getArray(2)
arr[0] = Taxon('one')
arr[1] = Taxon('two')
builder = TaxaListBuilder()
builder.addAll(arr)

from TASSELpy.net.maizegenetics.dna.snp.FilterGenotypeTable import FilterGenotypeTable
filtered = FilterGenotypeTable.functionalFilters(genoTable,
   sitesFilter=lambda x: x.getChromosome().getName() == '1',
   taxaFilter=lambda x: x.getName().startswith('3'))
"""
