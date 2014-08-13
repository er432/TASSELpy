from TASSELpy.net.maizegenetics.plugindef.AbstractPlugin import AbstractPlugin
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Boolean import Boolean, metaBoolean
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Long import metaLong
from TASSELpy.java.lang.String import String, metaString

java_imports = {'FixedEffectLMPlugin':'net/maizegenetics/analysis/association/FixedEffectLMPlugin',
                'Frame':'java/awt/Frame',
                'String':'java/lang/String'}

class FixedEffectLMPlugin(AbstractPlugin):
    _java_name = java_imports['FixedEffectLMPlugin']
    @javaConstructorOverload(java_imports['FixedEffectLMPlugin'],
                             (make_sig([java_imports['Frame'],'boolean'],'void'),
                              (Object,metaBoolean)))    
    def __init__(self, *args, **kwargs):
        """ Creates a new instance of FixedEffectLMPlugin

        Signatures:

        FixedEffectLMPlugin(Frame parentFrame, boolean isInteractive)

        Arguments:

        parentFrame -- A frame, can be null
        isInteractive -- Whether in an interactive session
        """
        pass
    @javaOverload("setOutputFile",
                  (make_sig([java_imports['String']],'void'),(metaString,),None))
    def setOutputFile(self, *args):
        """ Sets the output file

        Signatures:

        void setOutputFile(String filename)

        Arguments:

        filename -- the name of the filename
        """
        pass
    @javaOverload("setRestrictOutput",
                  (make_sig(['boolean'],'void'),(metaBoolean,),None))
    def setRestrictOutput(self, *args):
        """ Set the output to be restricted (or not)

        Signatures:

        void setRestrictOutput(boolean restrict)

        Arguments:

        restrict -- whether to restrict the output
        """
        pass
    @javaOverload("setMaxP",
                  (make_sig(['double'],'void'),(metaDouble,),None))
    def setMaxP(self, *args):
        """ Sets the maximum value of the p-value to keep

        Signatures:

        void setMaxP(double value)

        Arguments:

        value -- the maximum p-value
        """
        pass
    @javaOverload("setPermute",
                  (make_sig(['boolean'],'void'),(metaBoolean,),None))
    def setPermute(self, *args):
        """ Sets whether to perform permutations

        Signatures:

        void setPermute(boolean permute)

        Arguments:

        permute -- Whether to perform permutations
        """
        pass
    @javaOverload("setNumberOfPermutations",
                  (make_sig(['int'],'void'),(metaInteger,),None))
    def setNumberOfPermutations(self, *args):
        """ Sets the number of permutations to perform

        Signatures:

        void setNumberOfPermutations(int numberOfPermutations)

        Arguments:

        numberOfPermutations -- the number of permutations to perform
        """
        pass
    @javaOverload("setRandomizer",
                  (make_sig(['long'],'void'),(metaLong,),None))
    def setRandomizer(self, *args):
        """ Sets the randomizer seed so that permutation results are reproducible
        for testing. The same seed will reproduce the same sequence of pseudo-random
        numbers

        Signatures:

        void setRandomizer(long seed)

        Arguments:

        seed -- the seed
        """
        pass

class easy_GLM(FixedEffectLMPlugin):
    """ Subclass of FixedEffectLMPlugin that allows for easy running of GLMs
    """
    def __init__(self, outputFile = None, restrictOutput = False, maxP = None,
                 permute = False, numberOfPermutations = 1000, seed = None):
        """ Instantiates a GLM analysis

        Parameters
        ----------
        outputFile : str, optional
            A file for outputting results
        restrictOutput : boolean, optional
            Whether to restrict output
        maxP : double, optional
            A maximum p-value
        permute : boolean, optional
            Whether to run permutations
        numberOfPermutations : int, optional
            Number of permutations to perform (if performing permutations)
        seed : int, optional
            Random seed if reproducible permutations desired
        """
        # Call the java constructor
        super(easy_GLM, self).__init__(None, False)
        # Set the parameters
        if outputFile:
            self.setOutputFile(outputFile)
        self.setRestrictOutput(restrictOutput)
        if maxP:
            self.setMaxP(maxP)
        self.setPermute(permute)
        self.setNumberOfPermutations(numberOfPermutations)
        if seed:
            self.setRandomizer(seed)
    # TODO: Finish easy_GLM class

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
from TASSELpy.net.maizegenetics.util.TableReport import TableReport
from TASSELpy.net.maizegenetics.trait.MarkerPhenotypeAdapter import MarkerPhenotypeAdapter
from TASSELpy.net.maizegenetics.trait.MarkerPhenotype import MarkerPhenotype
from TASSELpy.net.maizegenetics.trait.CombinePhenotype import CombinePhenotype
from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype
from TASSELpy.net.maizegenetics.trait.Trait import Trait
from TASSELpy.net.maizegenetics.analysis.association.FixedEffectLMPlugin import FixedEffectLMPlugin
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
#dataList.add(Datum('trait',eardia,'eardia'))
dataList.add(Datum('allTraits', traits, 'traits'))
dataList.add(Datum('population',pop,'pop'))
dataList.add(Datum('alignment',b,'genotypes'))

ds = DataSet(dataList, None)
iap = IntersectionAlignmentPlugin(None, False)
joined = iap.performFunction(ds)

flm = FixedEffectLMPlugin(None, False)
resultSet = flm.performFunction(joined)
"""
