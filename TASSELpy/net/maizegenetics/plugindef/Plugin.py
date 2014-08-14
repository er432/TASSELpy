from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Class import Class
from TASSELpy.java.util.List import List
from TASSELpy.java.lang.String import String, metaString
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.net.maizegenetics.plugindef.Datum import Datum
from TASSELpy.net.maizegenetics.plugindef.PluginParameter import PluginParameter
from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.java.lang.Enum import Enum
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.Overloading import javaGenericOverload
from abc import ABCMeta

## Dictionary to hold java imports
java_imports = {'Class':'java/lang/Class',
                'Comparable':'java/lang/Comparable',
                'DataSet':'net/maizegenetics/plugindef/DataSet',
                'Datum':'net/maizegenetics/plugindef/Datum',
                'Enum':'java/lang/Enum',
                'List':'java/util/List',
                'Object':'java/lang/Object',
                'Plugin':'net/maizegenetics/plugindef/Plugin',
                'PluginParameter':'net/maizegenetics/plugindef/PluginParameter',
                'String':'java/lang/String'}

class metaPlugin:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C, Plugin):
            return True
        else:
            return False

class DataSet(Object):
    """ This is a set of Datum """
    _java_name = java_imports['DataSet']
    @javaConstructorOverload(java_imports['DataSet'],
                             (make_sig([java_imports['List'],java_imports['Plugin']],'void'),
                               (List, metaPlugin)),
                             (make_sig([java_imports['Datum'],java_imports['Plugin']],'void'),
                               (Datum, metaPlugin)),
                             (make_sig([java_imports['Datum']+'[]',java_imports['Plugin']],'void'),
                               (javaArray.get_array_type(Datum), metaPlugin)))
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
                   lambda x: Plugin(obj=x)))
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

class Plugin(Object):
    _java_name = java_imports['Plugin']
    @javaConstructorOverload(java_imports['Plugin'])
    def __init__(self, *args, **kwargs):
        """ Instantiates the Plugin
        """
        pass
    @javaOverload("performFunction",
                  (make_sig([java_imports['DataSet']],java_imports['DataSet']),
                   (DataSet,),
                  lambda x: DataSet(obj=x)))
    def performFunction(self, *args):
        """ Performs the function of this plugin

        Signatures:

        DataSet performFunction(DataSet input)

        Arguments:

        input -- input

        Returns:

        Resulting data set or null
        """
        pass
    @javaOverload("processData",
                  (make_sig([java_imports['DataSet']],java_imports['DataSet']),
                   (DataSet,),
                  lambda x: DataSet(obj=x)))
    def processData(self, *args):
        """ For the new Generic plugin parameter design, performFunction() will
        automatically call this. Therefore, coders of Plugins should override this
        instead of performFunction()

        Signatures:

        DataSet processData(DataSet input)

        Arguments:

        input -- input

        Returns:

        Resulting data set or null
        """
        pass
    @javaOverload("getParameter",
                  (make_sig([java_imports['Enum']],java_imports['Comparable']),
                   (Enum,),lambda x: Comparable(obj=x)),
                   (make_sig([java_imports['String']],java_imports['Comparable']),
                    (metaString,),lambda x: Comparable(obj=x)))
    def getParameter(self, *args):
        """ Returns a parameter value for given parameter key

        Signatures:

        Comparable getParameter(Enum key)
        Comparable getParameter(String key)

        Arguments:

        Comparable getParameter(Enum key)
            key -- key
        Comparable getParameter(String key)
            key -- key

        Returns:

        value
        """
        pass
    @javaOverload("setParameter",
                  (make_sig([java_imports['PluginParameter'],
                             java_imports['Object']],java_imports['Plugin']),
                  (PluginParameter, Object), lambda x: Plugin(obj=x)),
                  (make_sig([java_imports['String'], java_imports['Comparable']],
                            java_imports['Plugin']),(metaString, Comparable),
                  lambda x: Plugin(obj=x)),
                  (make_sig([java_imports['String'],java_imports['String']],
                            java_imports['Plugin']),(metaString,metaString),
                  lambda x: Plugin(obj=x)))
    def setParameter(self, *args):
        """ Sets parameter value

        Signatures:

        Plugin setParameter(PluginParameter param, Object value)
        Plugin setParameter(String key, Comparable value)
        Plugin setParameter(String key, String value)

        Arguments:

        Plugin setParameter(PluginParameter param, Object value)
            param -- parameter
            value -- value
        Plugin setParameter(String key, Comparable value)
            key -- key
            value -- value
        Plugin setParameter(String key, String value)
            key -- key
            value -- value

        Returns:

        This plugin
        """
        pass
    @javaOverload("receiveInput",
                  (make_sig([java_imports['Plugin']],'void'),(metaPlugin,),None))
    def receiveInput(self, *args):
        """ Sets up this plugin to receive input from another plugin

        Signatures:

        void receiveInput(Plugin input)

        Arguments:

        input -- input
        """
        pass
    @javaOverload("isInteractive",
                  (make_sig([],'boolean'),(),None))
    def isInteractive(self, *args):
        """ If interactive == true, the plugin will create dialgos and panels
        to interact with the user

        Signatures:

        boolean isInteractive()

        Returns:

        boolean for whether it's interactive
        """
        pass
    @javaOverload("setParameters",
                  (make_sig([java_imports['String']+'[]'],'void'),
                   (javaArray.get_array_type(String),),None))
    def setParameters(self, *args):
        """ Allows self-describing Plugins to use args to set parameters specific
        to itself

        Signatures:

        void setParameters(String[] args)

        Arguments:

        args -- arguments
        """
        pass
    @javaOverload("getCitation",
                  (make_sig([],java_imports['String']),(),None))
    def getCitation(self, *args):
        """ Returns Citation for this plugin

        Signatures:

        String getCitation()

        Returns:

        Citation
        """
        pass
    @javaOverload("pluginDescription",
                  (make_sig([],java_imports['String']),(),None))
    def pluginDescription(self, *args):
        """ Returns description of the plugin

        Signatures:

        String pluginDescription()

        Returns:

        description
        """
        pass

