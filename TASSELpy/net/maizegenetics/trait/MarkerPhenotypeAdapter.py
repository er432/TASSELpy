from TASSELpy.java.lang.Object import Object
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.java.lang.String import String
from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.net.maizegenetics.trait.MarkerPhenotype import MarkerPhenotype
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.javaObj import javaArray
from TASSELpy.java.lang.Integer import metaInteger
import numpy as np

java_imports = {'MarkerPhenotype':'net/maizegenetics/trait/MarkerPhenotype',
                'MarkerPhenotypeAdapter':'net/maizegenetics/trait/MarkerPhenotypeAdapter',
                'Phenotype':'net/maizegenetics/trait/Phenotype',
                'Object':'java/lang/Object',
                'String':'java/lang/String',
                'Taxon':'net/maizegenetics/taxa/Taxon'}

class MarkerPhenotypeAdapter(Object):
    """ Class used to easily access information on MarkerPhenotype objects
    """
    _java_name = java_imports['MarkerPhenotypeAdapter']
    @javaConstructorOverload(java_imports['MarkerPhenotypeAdapter'],
                             (make_sig([java_imports['Phenotype']],'void'),
                              (Phenotype,)),
                              (make_sig([java_imports['MarkerPhenotype']],'void'),
                               (MarkerPhenotype,)))
    def __init__(self, *args, **kwargs):
        """ Instantiates a MarkerPhenotypeAdapter object

        Signatures:

        MarkerPhenotypeAdapter(Phenotype aPhenotype)
        MarkerPhenotypeAdapter(MarkerPhenotype aMarkerPhenotype)

        Arguments:

        MarkerPhenotypeAdapter(Phenotype aPhenotype)
            aPhenotype -- A Phenotype object, if there is no set of markers
        MarkerPhenotypeAdapter(MarkerPhenotype aMarkerPhenotype)
            aMarkerPhenotype -- A MarkerPhenotype object
        """
        pass
    @javaOverload("areTraitFactorsConsistent",
                  (make_sig([],'boolean'),(),None))
    def areTraitFactorsConsistent(self, *args):
        """ Returns true if traits all have the same factors or no factors

        Signatures:

        boolean areTraitFactorsConsistent()

        Returns:

        true if all traits have the same factors or no factors
        """
        pass
    @javaOverload("checkFactorCovariateEnvironments",
                  (make_sig([],java_imports['String']),(),None))
    def checkFactorCovariateEnvironments(self, *args):
        """ Factor columns should either have no phenotype factors, or the ones
        they have should match at least one data column.

        Signatures:

        String checkFactorCovariateEnvironments()

        Returns:

        A message giving consistency information
        """
        pass
    # TODO : wrap getTraitLevel
    @javaOverload("getNumberOfRows",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def getNumberOfRows(self, *args):
        """ Gets the number of rows for a phenotype

        Signatures:

        int getNumberOfRows(int phenotype)

        Argument:

        phenotype -- The index of a phenotype
        
        Returns:

        The number of rows
        """
        pass
    @javaOverload("getNumberOfBlocks",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def getNumberOfBlocks(self, *args):
        """ Gets the number of blocks for a phenotype

        Signatures:

        int getNumberOfBlocks(int phenotype)

        Argument:

        phenotype -- The index of a phenotype
        
        Returns:

        The number of blocks
        """
        pass
    @javaOverload("getNumberOfPhenotypes",
                  (make_sig([],'int'),(),None))
    def getNumberOfPhenotypes(self, *args):
        """ Gets the number of Phenotypes

        Signatures:

        int getNumberOfPhenotypes()

        Returns:

        The number of Phenotypes
        """
        pass
    @javaOverload("getPhenotypeValues",
                  (make_sig(['int'],'double[]'),(metaInteger,),
                   lambda x: javaPrimativeArray.make_array_from_obj('double', x)))
    def getPhenotypeValues(self, *args):
        """ Gets the values for a Phenotype

        Signatures:

        double[] getPhenotypeValues(int i)

        Arguments:

        i -- The index of a Phenotype

        Returns:

        The values for a Phenotype
        """
        pass
    @javaOverload("getMissingPhenotypes",
                  (make_sig(['int'],'boolean[]'),(metaInteger,),
                   lambda x: javaPrimativeArray.make_array_from_obj('boolean', x)))
    def getMissingPhenotypes(self, *args):
        """ Gets array of booleans indicating which taxa have missing phenotypes

        Signatures:

        boolean[] getMissingPhenotypes(int phenotype)

        Arguments:

        phenotype -- The index of a phenotype

        Returns:

        Array of booleans indicating which taxa have missing phenotypes
        """
        pass
    @javaOverload("getPhenotypeName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def getPhenotypeName(self, *args):
        """ Gets the name of a phenotype

        Signatures:

        String getPhenotypeName(int i)

        Arguments:

        i -- The index of a phenotype

        Returns:

        The name of the phenotype
        """
        pass
    @javaOverload("getNumberOfFactors",
                  (make_sig([],'int'),(),None))
    def getNumberOfFactors(self, *args):
        """ Gets the number of factors

        Signatures:

        int getNumberOfFactors()

        Returns:

        The number of factors
        """
        pass
    @javaOverload("getFactorValues",
                  (make_sig(['int','int'],java_imports['String']+'[]'),
                   (metaInteger,metaInteger),
                   lambda x: javaArray.to_wrapped_array(x, pyType=String)))
    def getFactorValues(self, *args):
        """ Gets the factor values for a factor

        Signatures:

        String[] getFactorValues(int phenotype, int factor)

        Arguments:

        phenotype -- The index of a phenotype
        factor -- The index of a factor

        Returns:

        The names of the values for the factor
        """
        pass
    @javaOverload("getMissingFactors",
                  (make_sig(['int','int'],'boolean[]'),(metaInteger,metaInteger),
                   lambda x: javaPrimativeArray.make_array_from_obj('boolean', x)))
    def getMissingFactors(self, *args):
        """ Gets the missing factors for a phenotype

        Signatures:

        boolean[] getMissingFactors(int phenotype, int factor)

        Arguments:

        phenotype -- The index of a phenotype
        factor -- The index of a factor

        Returns:

        Boolean array indicating factor values are missing for a taxon
        """
        pass
    @javaOverload("getFactorName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),
                   None))
    def getFactorName(self, *args):
        """ Gets a factor name

        Signatures:

        String getFactorName(int i)

        Arguments:

        i -- The index of a factor

        Returns:

        The name of the factor
        """
        pass
    @javaOverload("getNumberOfCovariates",
                  (make_sig([],'int'),(),None))
    def getNumberOfCovariates(self, *args):
        """ Gets the number of covariates

        Signatures:

        int getNumberOfCovariates()

        Returns:

        The number of covariates
        """
        pass
    @javaOverload("getCovariateValues",
                  (make_sig(['int','int'],'double[]'),(metaInteger,metaInteger),
                   lambda x: javaPrimativeArray.make_array_from_obj('double',x)))
    def getCovariateValues(self, *args):
        """ Gets the values of a covariate

        Signatures:

        double[] getCovariateValues(int phenotype, int covariate)

        Arguments:

        phenotype -- The index of a phenotype
        covariate -- The index of a covariate

        Returns:

        The values of the covariate
        """
        pass
    @javaOverload("getMissingCovariates",
                  (make_sig(['int','int'],'boolean[]'),(metaInteger,metaInteger),
                   lambda x: javaPrimativeArray.make_array_from_obj('boolean',x)))
    def getMissingCovariates(self, *args):
        """ Gets a boolean array indicating whether covariate values are missing

        Signatures:

        boolean[] getMissingCovariates(int phenotype, int covariate)

        Arguments:

        phenotype -- The index of a phenotype
        covariate -- The index of a covariate

        Returns:

        Boolean array indicating whether covariate values are missing
        """
        pass
    @javaOverload("getCovariateName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,), None))
    def getCovariateName(self, *args):
        """ Gets the name of a covariate

        Signatures:

        String getCovariateName(int i)

        Arguments:

        i -- The index of a covariate

        Returns:

        The name of the covariate
        """
        pass
    @javaOverload("getNumberOfMarkers",
                  (make_sig([],'int'),(), None))
    def getNumberOfMarkers(self, *args):
        """ Gets the number of markers

        Signatures:

        int getNumberOfMarkers()

        Returns:

        The number of markers
        """
        pass
    @javaOverload("isMarkerDiscrete",
                  (make_sig(['int'],'boolean'),(metaInteger,),None))
    def isMarkerDiscrete(self, *args):
        """ Returns whether a given marker is discrete

        Signatures:

        boolean isMarkerDiscrete(int i)

        Arguments:

        i -- The index of a marker

        Returns:

        Whether the given marker is discrete
        """
        pass
    @javaOverload("getMarkerName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def getMarkerName(self, *args):
        """ Gets a marker name

        Signatures:

        String getMarkerName(int i)

        Arguments:

        i -- The index of a marker

        Returns:

        The name of the marker
        """
        pass
    @javaOverload("getMarkerChromosome",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def getMarkerChromosome(self, *args):
        """ Gets the chromosome of a marker

        Signatures:

        String getMarkerChromosome(int marker)

        Arguments:

        marker -- The index of a marker

        Returns:

        The chromosome of the marker
        """
        pass
    @javaOverload("getMarkerChromosomePosition",
                  (make_sig(['int'],'double'),(metaInteger,),np.float64))
    def getMarkerChromosomePosition(self, *args):
        """ Gets the position of a marker on the chromosome

        Signatures:

        double getMarkerChromosomePosition(int marker)

        Arguments:

        marker -- The index of a marker

        Returns:

        The position of the marker on a chromosome
        """
        pass
    @javaOverload("getLocusName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def getLocusName(self, *args):
        """ Gets the name of a locus

        Signatures:

        String getLocusName(int marker)

        Arguments:

        marker -- The index of a marker

        Returns:

        The name of the locus
        """
        pass
    @javaOverload("getLocusPosition",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def getLocusPosition(self, *args):
        """ Gets the position of a locus

        Signatures:

        int getLocusPosition(int marker)

        Arguments:

        marker -- The index of a marker

        Returns:

        The position of the locus
        """
        pass
    @javaOverload("getMarkerValue",
                  (make_sig(['int','int'],java_imports['Object']+'[]'),
                   (metaInteger,metaInteger),
                   lambda x: javaArray.wrap_existing_array(x, pyType=Object)))
    def getMarkerValue(self, *args):
        """ Gets the value of a marker over the taxa

        Signatures:

        Object[] getMarkerValue(int phenotype, int marker)

        Arguments:

        phenotype -- The index of a phenotype
        marker -- The index of a marker

        Returns:

        The value of a marker over the taxa
        """
        pass
    @javaOverload("getMissingMarkers",
                  (make_sig(['int','int'],'boolean[]'),
                   (metaInteger,metaInteger),
                   lambda x: javaPrimativeArray.make_array_from_obj('boolean',x)))
    def getMissingMarkers(self, *args):
        """ Gets a boolean array indicating which taxa have a marker missing

        Signatures:

        boolean[] getMissingMarkers(int phenotype, int marker)

        Arguments:

        phenotype -- The index of a phenotype
        marker -- The index of a marker

        Returns:

        Boolean array indicating which taxa have a marker missing
        """
        pass
    @javaOverload("getTaxa",
                  (make_sig(['int'],java_imports['Taxon']+'[]'),(metaInteger,),
                   lambda x: javaArray.wrap_existing_array(x, pyType=Taxon)))
    def getTaxa(self, *args):
        """ Gets the taxa that are present for a phenotype

        Signatures:

        Taxon[] getTaxa(int phenotype)

        Arguments:

        phenotype -- The index of a Phenotype

        Returns:

        The taxa that are present for a Phenotype
        """
        pass
    @javaOverload("hasMarkerNames",
                  (make_sig([],'boolean'),(),None))
    def hasMarkerNames(self, *args):
        """ Gets whether there are marker names present

        Signatures:

        boolean hasMarkerNames()

        Returns:

        Whether marker names are present
        """
        pass
