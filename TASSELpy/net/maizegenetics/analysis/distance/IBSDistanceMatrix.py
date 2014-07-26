from TASSELpy.net.maizegenetics.taxa.distance.DistanceMatrix import DistanceMatrix
from TASSELpy.net.maizegenetics.util.ProgressListener import ProgressListener
from TASSELpy.net.maizegenetics.util.BitSet import BitSet
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload,javaStaticOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray, meta_long_array
from TASSELpy.utils.helper import make_sig
import numpy as np

java_imports = {'BitSet':'net/maizegenetics/util/BitSet',
                'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'IBSDistanceMatrix':'net/maizegenetics/analysis/distance/IBSDistanceMatrix',
                'ProgressListener':'net/maizegenetics/util/ProgressListener',
                'String':'java/lang/String'}
class IBSDistanceMatrix(DistanceMatrix):
    """
    This class calculates an identity by state matrix. It is scaled so only
    non-missing comparison are used.  It conducts bit level calculations of IBS for genotypes.
    Only the two most common alleles are used in the distance calculations.

    Please note that when heterozygous genotypes are used, Het to Het distance is 0.5 NOT 0.0. The default
    along the identity diagonal is 0 (isTrueIBS = false), but changing isTrueIBS = true will calculate
    the identity.

    The distance estimates become wildly inaccurate when too few sites are used to calculate
    distance.  The minSiteComp parameter can be used to control the minimum number of sites
    used for a calculation.  If there are insufficient sites in the estimate, then Double.NaN
    is returned.
    """
    _java_name = java_imports['IBSDistanceMatrix']
    @javaConstructorOverload(java_imports['IBSDistanceMatrix'],
                             (make_sig([java_imports['GenotypeTable']],'void'),(GenotypeTable,)),
                            (make_sig([java_imports['GenotypeTable'],java_imports['ProgressListener']],
                                      'void'),(GenotypeTable,ProgressListener)),
                            (make_sig([java_imports['GenotypeTable'],'int',
                                       java_imports['ProgressListener']],
                                      'void'),(GenotypeTable,metaInteger,ProgressListener)),
                            (make_sig([java_imports['GenotypeTable'],'int','boolean',
                                       java_imports['ProgressListener']],
                                      'void'),(GenotypeTable,metaInteger,metaBoolean,ProgressListener)))
    def __init__(self,*args,**kwargs):
        """
        Compute observed distances for all taxa. Missing sites are ignored

        Signatures:

        IBSDistanceMatrix(GenotypeTable theAlignment)
        IBSDistanceMatrix(GenotypeTable theAlignment, ProgressListener listener)
        IBSDistanceMatrix(GenotypeTable theAlignment, int minSiteComp, ProgressListener listener)
        IBSDistanceMatrix(GenotypeTable theAlignment, int minSiteComp, boolean trueIBS,
                         ProgressListener listener)

        Arguments:

        IBSDistanceMatrix(GenotypeTable theAlignment)
            theAlignment -- Alignment used to compute distances
        IBSDistanceMatrix(GenotypeTable theAlignment, ProgressListener listener)
            theAlignment -- Alignment used to compute distances
            listener -- Listener to track progress in calculations
        IBSDistanceMatrix(GenotypeTable theAlignment, int minSiteComp, ProgressListener listener)
            theAlignment -- Alignment used to compute distances
            minSiteComp -- Minimum number of sites needed to estimate distance
            listener -- Listener to track progress in calculations
        IBSDistanceMatrix(GenotypeTable theAlignment, int minSiteComp, boolean trueIBS,
                         ProgressListener listener)
            theAlignment -- Alignment used to compute distances
            minSiteComp -- Minimum number of sites needed to estimate distance
            trueIBS -- Estimate diagonal distance based IBS (default = false, i=i=0.0)
            listener -- Listener to track progress in calculations
        """
        pass
    ## Compute distance for a pair of taxa
    # @param theTBA input alignment
    # @param taxon1 index of taxon1
    # @param taxon2 index of taxon2
    # @return Array of {distance, number of sites used in comparison}
    @javaStaticOverload(java_imports['IBSDistanceMatrix'],"computeHetBitDistances",
                        (make_sig([java_imports['GenotypeTable'],'int','int'],'double[]'), # First
                         (GenotypeTable,metaInteger,metaInteger),
                         lambda x: javaPrimativeArray.make_array_from_obj('double',x)),
                         (make_sig([java_imports['GenotypeTable'],'int','int','int','boolean'], # Second
                                   'double[]'),
                         (GenotypeTable,metaInteger,metaInteger,metaInteger,metaBoolean),
                         lambda x: javaPrimativeArray.make_array_from_obj('double',x)),
                         (make_sig([java_imports['GenotypeTable'],'int','int','int','int','int', # Third
                                    java_imports['BitSet']], 'double[]'),
                         (GenotypeTable,metaInteger,metaInteger,metaInteger,metaInteger,metaInteger,
                          BitSet),
                         lambda x: javaPrimativeArray.make_array_from_obj('double',x)),
                         (make_sig(['long[]','long[]','long[]','long[]','int'], 'double[]'), # Fourth
                         (meta_long_array,
                          meta_long_array,
                          meta_long_array,
                          meta_long_array,metaInteger),
                         lambda x: javaPrimativeArray.make_array_from_obj('double',x)),
                         (make_sig(['long[]','long[]','long[]','long[]','int','int','int'], # Fifth
                                   'double[]'),
                         (meta_long_array,
                          meta_long_array,
                          meta_long_array,
                          meta_long_array,metaInteger,
                          metaInteger,metaInteger),
                         lambda x: javaPrimativeArray.make_array_from_obj('double',x)))
    def computeHetBitDistances(*args):
        """
        Compute distance for a pair of taxa

        Signatures:

        static double[] computeHetBitDistances(GenotypeTable theTBA, int taxon1, int taxon2)
        static double[] computeHetBitDistances(GenotypeTable theTBA, int taxon1, int taxon2,
                                                  int minSitesCompared, boolean isTrueIBS)
        static double[] computeHetBitDistances(GenotypeTable theTBA, int taxon1, int taxon2, 
            int minSitesCompared, int firstWord, int lastWord, BitSet maskBadSet)
        static double[] computeHetBitDistances(long[] iMj, long[] iMn, long[] jMj, long[] jMn, 
            int minSitesCompared)
        static double[] computeHetBitDistances(long[] iMj, long[] iMn, long[] jMj, long[] jMn, 
            int minSitesCompared, int firstWord, int lastWord)
        
        Arguments:

        static double[] computeHetBitDistances(GenotypeTable theTBA, int taxon1, int taxon2)
            theTBA -- input alignment
            taxon1 -- index of taxon 1
            taxon2 -- index of taxon 2
        static double[] computeHetBitDistances(GenotypeTable theTBA, int taxon1, int taxon2,
                                                  int minSitesCompared, boolean isTrueIBS)
            theTBA -- input alignment
            taxon1 -- index of taxon 1
            taxon2 -- index of taxon 2
            minSitesCompared -- Minimum number of sites needed to estimate distance
            isTrueIBS -- estimate diagonal distance based IBS (default = False, i=i=0.0)
        static double[] computeHetBitDistances(GenotypeTable theTBA, int taxon1, int taxon2, 
            int minSitesCompared, int firstWord, int lastWord, BitSet maskBadSet)
            theTBA -- input alignment
            taxon1 -- index of taxon 1
            taxon2 -- index of taxon 2
            minSitesCompared -- Minimum number of sites needed to estimate distance
            firstWord -- Starting word for calculating distance site=(firstWord*64)
            lastWord -- Ending word for calculating distance inclusive site=(lastWord*64+63)
            maskBadSet -- Optional mask for sites (those set to 1 are kept)
        static double[] computeHetBitDistances(long[] iMj, long[] iMn, long[] jMj, long[] jMn, 
            int minSitesCompared)
            iMj -- Vector of major alleles for taxon i
            iMn -- Vector of minor alleles for taxon i
            jMj -- Vector of major alleles for taxon j
            jMn -- Vector of minor alleles for taxon j
            minSitesCompared -- Minimum number of sites needed to estimate distance
        static double[] computeHetBitDistances(long[] iMj, long[] iMn, long[] jMj, long[] jMn, 
            int minSitesCompared, int firstWord, int lastWord)
            iMj -- Vector of major alleles for taxon i
            iMn -- Vector of minor alleles for taxon i
            jMj -- Vector of major alleles for taxon j
            jMn -- Vector of minor alleles for taxon j
            minSitesCompared -- Minimum number of sites needed to estimate distance
            firstWord -- Starting word for calculating distance site=(firstWord*64)
            lastWord -- Ending word for calculating distance inclusive site=(lastWord*64+63)
        
        Returns:

        Array of {distance, number of sites used in comparison}
        """
        pass
    ## Gets the average number of sites used in calculating the distance matrix
    # @return Average number of sites used in calculating the distance matrix
    @javaOverload("getAverageTotalSites",
                  (make_sig([],'double'),(),np.float64))
    def getAverageTotalSites(self, *args):
        """
        Gets average number of sites used in calculating the distance matrix

        Signatures:

        double getAverageTotalSits()

        Returns:

        Average number of sites used in calculating the distance matrix
        """
        pass
    ## Gets string representation of this matrix with 'd' displayed digits
    # @param d The number of digits to display
    # @return String representation of this matrix
    @javaOverload("toString",
                  (make_sig([],java_imports['String']),(),None),
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def toString(self, *args):
        """
        Gets string representation of this matrix with 'd' displayed digits

        Signatures:

        String toString()
        String toString(int d)

        Arguments:

        String toString(int d)
            d -- The number of digits to display

        Returns:

        String representation of this matrix
        """
        pass
    ## Returns whether true IBS is calculated for the diagonal
    # @return Whether true IBS is calculated for the diagonal
    @javaOverload("isTrueIBS",
                  (make_sig([],'boolean'),(),None))
    def isTrueIBS(self, *args):
        """
        Returns whether true IBS is calculated for the diagonal

        Signatures:

        boolean IsTrueIBS()

        Returns:

        Whether true IBS is calculated for the diagonal
        """
        pass
