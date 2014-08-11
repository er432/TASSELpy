from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Class import Class
from TASSELpy.java.util.List import List
from TASSELpy.java.lang.String import metaString, String
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.net.maizegenetics.plugindef.Datum import Datum
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.utils.Overloading import javaGenericOverload
import TASSELpy.net.maizegenetics.plugindef.Plugin

## Dictionary to hold java imports
java_imports = {'Class':'java/lang/Class',
                'DataSet':'net/maizegenetics/plugindef/DataSet',
                'Datum':'net/maizegenetics/plugindef/Datum',
                'List':'java/util/List',
                'Plugin':'net/maizegenetics/plugindef/Plugin'}

class DataSet(Object):
    """ This is a set of Datum """
    _java_name = java_imports['DataSet']
    @javaConstructorOverload(java_imports['DataSet'],
                             (make_sig([java_imports['List'],java_imports['Plugin']],'void'),
                               (List, TASSELpy.net.maizegenetics.plugindef.Plugin.Plugin)),
                             (make_sig([java_imports['Datum'],java_imports['Plugin']],'void'),
                               (Datum, TASSELpy.net.maizegenetics.plugindef.Plugin.Plugin)),
                             (make_sig([java_imports['Datum']+'[]',java_imports['Plugin']],'void'),
                               javaArray.get_array_type(Datum)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a DataSet

        Signatures:

        DataSet(List<Datum> list, Plugin creator)
        DataSet(Datum theDatum, Plugin creator)
        DataSet(Datum[] list, Plugin creator)

        Arguments:

        DataSet(List<Datum> list, Plugin creator)
            list -- list of data elements
            creator -- creating plugin
        DataSet(Datum theDatum, Plugin creator)
            theDatum -- a single Datum
            creator -- creating plugin
        DataSet(Datum[] list, Plugin creator)
            list -- list of data elements
            creator -- creating plugin
        """
        pass
    @javaOverload("getDataSet",
                  (make_sig([],java_imports['List']),(),lambda x: List(obj=x)))
    def getDataSet(self, *args):
        """ Gets the dataset as a list

        Signatures:

        List getDataSet()

        Returns:

        The data set as a list
        """
        pass
    @javaOverload("getData",
                  (make_sig(['int'],java_imports['Datum']),(metaInteger,),
                   lambda x: Datum(obj=x)))
    def getData(self, *args):
        """ Gets a particular datum

        Signatures:

        Datum getData(int i)

        Arguments:

        i -- The index to get

        Returns:

        The datum
        """
        pass
    @javaOverload("getSize",
                  (make_sig([],'int'),(),None))
    def getSize(self, *args):
        """ Gets the size of the dataset

        Signatures:

        int getSize()

        Returns:

        The size of the dataset
        """
        pass
    @javaOverload("getCreator",
                  (make_sig([],java_imports['Plugin']),(),
                   lambda x: TASSELpy.net.maizegenetics.plugindef.Plugin.Plugin(obj=x)))
    def getCreator(self, *args):
        """ Gets the creator of the dataset

        Signatures:

        Plugin getCreator()

        Returns:

        The creator of the dataset
        """
        pass
    @javaGenericOverload("getDataOfType",
                         (make_sig([java_imports['Class']],java_imports['List']),
                          (Class,),
                         dict(type=List,generic=(Datum,))),
                         (make_sig([java_imports['Class']+'[]'],java_imports['List']),
                          (javaArray.get_array_type(Class),),
                         dict(type=List,generic=(Datum,))))
    def getDataOfType(self, *args):
        """ Gets the data of a type or list of types

        Signatures:

        List<Datum> getDataOfType(Class theClass)
        List<Datum> getDataOfType(Class[] classes)

        Arguments:

        List<Datum> getDataOfType(Class theClass)
            theClass -- The class of the data to get
        List<Datum> getDataOfType(Class[] classes)
            classes -- Classes of the data to get
        Returns:

        A list of the data of the type(s)
        """
        pass
    @javaGenericOverload("getDataWithName",
                         (make_sig([java_imports['String']],java_imports['List']),
                          (metaString,),
                         dict(type=List,generic=Datum)),
                         (make_sig([java_imports['String']+'[]'],
                                   java_imports['List']),
                         (javaArray.get_array_type(String),),
                         dict(type=List,generic=(Datum,))))
    def getDataWithName(self, *args):
        """ Gets the data named somehow

        Signatures:

        List<Datum> getDataWithName(String name)
        List<Datum> getDataWithName(String[] names)

        Arguments:

        List<Datum> getDataWithName(String name)
            name -- The name of the data to get
        List<Datum> getDataWithName(String[] names)
            names -- The names of the data to get
        Returns:

        A list of data with the name(s)
        """
        pass
    @javaGenericOverload("getDataOfTypeWithName",
                         (make_sig([java_imports['Class']+'[]',
                                    java_imports['String']+'[]'],
                                    java_imports['List']),
                         (javaArray.get_array_type(Class),
                          javaArray.get_array_type(String)),
                         dict(type=List, generic=(Datum,))))
    def getDataOfTypeWithName(self, *args):
        """ Gets data of some type that has some name

        Signatures:

        List<Datum> getDataOfTypeWithName(Class[] classes, String[] names)

        Arguments:

        classes -- The array of classes of types to keep
        names -- The list of names of the data to keep

        Returns:

        The list of data to keep
        """
        pass
