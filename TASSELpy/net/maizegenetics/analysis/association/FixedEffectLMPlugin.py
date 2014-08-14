from TASSELpy.net.maizegenetics.plugindef.AbstractPlugin import AbstractPlugin
from TASSELpy.net.maizegenetics.analysis.data.IntersectionAlignmentPlugin import IntersectionAlignmentPlugin
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.util.LinkedList import LinkedList
from TASSELpy.net.maizegenetics.plugindef.DataSet import DataSet
from TASSELpy.net.maizegenetics.plugindef.Datum import Datum
from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype
from TASSELpy.net.maizegenetics.util.TableReport import TableReport
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

    Example
    -------

    >>> from TASSELpy import TASSELbridge
    >>> TASSELbridge.start()
    >>> from TASSELpy.data.data_constants import *
    >>> from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
    >>> from TASSELpy.net.maizegenetics.trait.ReadPhenotypeUtils import ReadPhenotypeUtils
    >>> from TASSELpy.net.maizegenetics.analysis.association.FixedEffectLMPlugin import easy_GLM
    >>> inputAlign = ImportUtils.readFromHapmap(HAPMAP_FILE)
    Reading :/Users/eli/Development/TASSELpy/TASSELpy/data/mdp_genotype.hmp.txt  finished
    >>> traits = ReadPhenotypeUtils.readGenericFile(TRAITS_FILE)
    >>> pop = ReadPhenotypeUtils.readGenericFile(POP_STRUCTURE_FILE)
    >>> glm = easy_GLM()
    >>> glm.addPhenotype(traits,'traits')
    >>> glm.addMarkers(inputAlign,'markers')
    >>> glm.addCovariate(pop,'populations')
    >>> marker_effects, allele_effects = glm.run_glm(phenotypes=('traits',),markers='markers',covariates=('populations',))    
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
        # Create dictionaries of Datum_name -> Datum for phenotypes, covariates,
        # and alignments
        self.phenotypes = {}
        self.covariates = {}
        self.alignments = {}
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
    def addPhenotype(self, pheno, name, comment=None):
        """ Adds a Phenotype object to the analysis

        Parameters
        ----------
        pheno : Phenotype object
            Phenotype object consisting of 1 or more traits to analyze
        name : str
            The name to give to this Phenotype datum
        comment : str, optional
            A comment on the Phenotype. If None, will be the same as name

        Raises
        ------
        TypeError:
            if pheno is not a Phenotype or name is not a string
        """
        if not isinstance(pheno, Phenotype):
            raise TypeError("pheno is not a Phenotype object")
        if not isinstance(name, metaString):
            raise TypeError("name is not a string")
        if not comment:
            comment = str(name)
        elif not isinstance(comment, metaString):
            raise TypeError("comment is not a string")
        self.phenotypes[name] = Datum(name, pheno, comment)
    def addCovariate(self, covar, name, comment=None):
        """ Adds a covariate to the analysis

        Parameters
        ----------
        covar : Phenotype object
            Phenotype object consisting of 1 or more covariates
        name : str
            The name to give to this covariate datum
        comment : str, optional
            A comment on the covariate. If None, will be the same as name

        Raises
        ------
        TypeError:
            if covariate is not a Phenotype or name is not a string
        """
        if not isinstance(covar, Phenotype):
            raise TypeError("covar is not a Phenotype object")
        if not isinstance(name, metaString):
            raise TypeError("name is not a string")
        if not comment:
            comment = str(name)
        elif not isinstance(comment, metaString):
            raise TypeError("comment is not a string")
        # Ensure all traits are covariates
        for i in xrange(covar.getNumberOfTraits()):
            if covar.getTrait(i).getType() != 'covariate':
                covar.getTrait(i).setType('covariate')
        self.covariates[name] = Datum(name, covar, comment)
    def addMarkers(self, markers, name, comment=None):
        """ Adds markers to the analysis

        Parameters
        ----------
        markers : GenotypeTable object
            Genotype table givng the genetic markers
        name : str
            The name to give to this set of markers
        comment : str, optional
            A comment on the markers. If None, will be the same as name

        Raises
        ------
        TypeError
            If markers is not a GenotypeTable or name not a string
        """
        if not isinstance(markers, GenotypeTable):
            raise TypeError("markers is not a GenotypeTable object")
        if not isinstance(name, metaString):
            raise TypeError("name is not a string")
        if not comment:
            comment = str(name)
        elif not isinstance(comment, metaString):
            raise TypeError("comment is not a string")
        self.alignments[name] = Datum(name, markers, comment)
    def run_glm(self, phenotypes, markers, covariates = None):
        """ Runs the GLM and returns the results as a TableReport

        Parameters
        ----------
        phenotypes : iterable of strings
            The names of the phenotypes you want to run
        markers : str
            The name of the marker set you want to use
        covariates : iterable of strings, optional
            The names of the covariates you want to use

        Raises
        ------
        KeyError
            If names not present
        
        Returns
        -------
        TableReport of marker effects, TableReport of allelic effects
        """
        dataList = LinkedList(generic=(Datum,))
        for pheno in phenotypes:
            dataList.add(self.phenotypes[pheno])
        dataList.add(self.alignments[markers])
        if covariates:
            for covar in covariates:
                dataList.add(self.covariates[covar])
        # Make the dataset, and turn into MarkerPhenotype object
        ds = DataSet(dataList, None)
        ds = IntersectionAlignmentPlugin(None, False).performFunction(ds)
        resultSet = FixedEffectLMPlugin(None, False).performFunction(ds)
        marker_effects = resultSet.getData(0).getData().castTo(TableReport)
        allele_effects = resultSet.getData(1).getData().castTo(TableReport)
        return marker_effects, allele_effects
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
