from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import String, metaString
from TASSELpy.net.maizegenetics.plugindef.PluginParameter import PluginParameter
from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.java.lang.Enum import Enum
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import javaArray
from abc import ABCMeta
from . import DataSet

## Dictionary to hold java imports
java_imports = {'Comparable':'java/lang/Comparable',
                'DataSet':'net/maizegenetics/plugindef/DataSet',
                'Enum':'java/lang/Enum',
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

class Plugin(Object):
    _java_name = java_imports['Plugin']
    @javaConstructorOverload(java_imports['Plugin'])
    def __init__(self, *args, **kwargs):
        """ Instantiates the Plugin
        """
        pass
    @javaOverload("performFunction",
                  (make_sig([java_imports['DataSet']],java_imports['DataSet']),
                   (DataSet,),lambda x: DataSet(obj=x)))
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
                   (DataSet,),lambda x: DataSet(obj=x)))
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

# TODO: Get the following working:
"""
from TASSELpy.TASSELbridge import TASSELbridge
TASSELbridge.start()
from TASSELpy.data.data_constants import *
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTableUtils import GenotypeTableUtils
from TASSELpy.net.maizegenetics.trait.ReadPhenotypeUtils import ReadPhenotypeUtils
from TASSELpy.net.maizegenetics.trait.FilterPhenotype import FilterPhenotype
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.java.util.LinkedList import LinkedList
from TASSELpy.net.maizegenetics.plugindef.Datum import Datum
from TASSELpy.net.maizegenetics.plugindef.DataSet import DataSet
from TASSELpy.net.maizegenetics.analysis.data.IntersectionAlignmentPlugin import IntersectionAlignmentPlugin
import numpy as np

inputAlign = ImportUtils.readFromHapmap(HAPMAP_FILE)
traits = ReadPhenotypeUtils.readGenericFile(TRAITS_FILE)
pop = ReadPhenotypeUtils.readGenericFile(POP_STRUCTURE_FILE)

useTraits = javaPrimativeArray.make_array('int',1)
useTraits[0] = 2
eardia = FilterPhenotype.getInstance(traits, None, useTraits)
a = GenotypeTableUtils.removeSitesOutsideRange(inputAlign, 0, 9)
b = GenotypeTableUtils.removeSitesBasedOnFreqIgnoreMissing(a, np.float64(0.1),
                                                           np.float64(1), 100)
dataList = LinkedList(generic=(Datum,))
dataList.add(Datum('trait',eardia,'eardia'))
dataList.add(Datum('population',pop,'pop'))
dataList.add(Datum('alignment',b,'genotypes'))

ds = DataSet(dataList, None)
iap = IntersectionAlignmentPlugin(None, False)
joined = iap.performFunction(ds)
"""
