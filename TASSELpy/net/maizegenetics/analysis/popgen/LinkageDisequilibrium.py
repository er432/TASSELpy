from TASSELpy.net.maizegenetics.stats.statistics.FisherExact import FisherExact
from TASSELpy.net.maizegenetics.util.BitSet import BitSet
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.net.maizegenetics.analysis.popgen.LDResult import LDResult
from TASSELpy.net.maizegenetics.util.ProgressListener import ProgressListener
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Float import metaFloat
from TASSELpy.java.lang.Enum import enum as java_enum
from TASSELpy.java.lang.Enum import Enum
from TASSELpy.java.lang.Thread import Thread
from TASSELpy.net.maizegenetics.util.TableReport import TableReport
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload,javaStaticOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray, meta_int_array
from TASSELpy.utils.helper import make_sig
import numpy as np

java_imports = {'BitSet':'net/maizegenetics/util/BitSet',
                'FisherExact':'net/maizegenetics/stats/statistics/FisherExact',
                'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'LDResult':'net/maizegenetics/analysis/popgen/LDResult',
                'LinkageDisequilibrium':'net/maizegenetics/analysis/popgen/LinkageDisequilibrium',
                'ProgressListener':'net/maizegenetics/util/ProgressListener'}
class LinkageDisequilibrium(Thread, TableReport):
    """
    This class calculates D' and r^2 estimates of linkage disequilibrium. It also
    calculates the significance of the LD by either Fisher Exact or the
    multinomial permutation test. This class can work with either normal
    alignments of annotated alignments. The alignments should be stripped of
    invariable numSites.
        {@link testDesign} sets matrix design for LD calculation. Either all by
    all, sliding window, site by all, or site list.
       
    There are multiple approaches for dealing with heterozygous sites.
    {@link HetTreatment} sets the way these are treated. Haplotype assumes fully
    phased heterozygous sites (any hets are double counted). This is the best
    approach for speed when things are fully phased. Homozygous converted all
    hets to missing. Genotype does a 3x3 genotype analysis (to be implemented)
       
    2 state estimates of D' and r^2 can be found reviewed and discussed in Weir
    1996
       
    Multi-state loci (>=3) require an averaging approach. In TASSEL 3 in 2010,
    Buckler removed these approach as the relative magnitudes and meaningfulness
    of these approaches has never been clear. Additionally with the moving away
    from SSR to SNPs these methods are less relevant. Researchers should convert
    to biallelic - either by ignoring rarer classes or collapsing rarer states.
    """
    _java_name = java_imports['LinkageDisequilibrium']
    ## testDesign enum
    testDesign = java_enum(java_imports['LinkageDisequilibrium']+'$testDesign',
                           'All','SlidingWindow','SiteByAll','SiteList',
                           subclass='testDesign')
    ## HetTreatment enum
    HetTreatment = java_enum(java_imports['LinkageDisequilibrium']+'$HetTreatment',
                             'Haplotype','Homozygous','Genotype',
                             subclass='HetTreatment')
    @javaConstructorOverload(java_imports['LinkageDisequilibrium'],
            (make_sig([java_imports['GenotypeTable'],'int',
                       java_imports['LinkageDisequilibrium']+'$testDesign','int',
                       java_imports['ProgressListener'],'boolean','int','int[]',
                       java_imports['LinkageDisequilibrium']+'$HetTreatment'],'void'),
            (GenotypeTable,metaInteger,testDesign.subclass,metaInteger,ProgressListener,
                metaBoolean,metaInteger,meta_int_array,
            HetTreatment.subclass)))
    def __init__(self, *args, **kwargs):
        """
        Constructor for doing LD analysis

        Signatures:
        
        LinkageDisequilibrium(GenotypeTable alignment, int windowSize, testDesign LDType,
                                 int testSite, ProgressListener listener, boolean isAccumulativeReport,
                                 int numAccumulateIntervals, int[] sitesList, HetTreatment hetTreatment)

        Arguments:

        alignment -- Input alignment with segregating sites
        windowSize -- Size of sliding window
        LDType --One of the testDesign enum types (All, SlidingWindow, SiteByAll, SiteList)
        testSite
        listener
        isAccumulativeReport
        numAccumulateIntervals
        sitesList
        hetTreatment
        """
        pass
    @javaStaticOverload(java_imports['LinkageDisequilibrium'],"calculateBitLDForHaplotype",
            (make_sig(['boolean','int',java_imports['GenotypeTable'],'int','int'],
                      java_imports['LDResult']),(metaBoolean,metaInteger,GenotypeTable,
                                                 metaInteger,metaInteger),
                                                 lambda x: LDResult(obj=x)))
    def calculateBitLDForHaplotype(*args):
        """
        Calculates the Bit LD between two sites

        Signatures:

        static LDResult calculateBitLDForHaplotype(boolean ignoreHets,
                                int minTaxaForEstimate, GenotypeTable alignment,
                                int site1, int site2)

        Arguments:

        ignoreHets -- Whether to ignore heterozygous sites
        minTaxaForEstimate -- The minimum number of taxa required to estimate LD
        alignment -- A GenotypeTable containing the sites
        site1 -- The index of the first site
        site2 -- The index of the second site

        Returns:

        LDResult containing the LD info
        """
        pass
    ## Calculates the normalized D' from Weir Genetic Analysis II 1986 pg. 120
    # @param countAB Count of AB alleles
    # @param countAb Count of Ab alleles
    # @param countaB Count of aB alleles
    # @param countab Count of ab alleles
    # @return Value of D'
    @javaStaticOverload(java_imports['LinkageDisequilibrium'],"calculateDPrime",
                        (make_sig(['int','int','int','int','int'],'double'),
                         (metaInteger,metaInteger,metaInteger,metaInteger,metaInteger),
                         np.float64))
    def calculateDPrime(*args):
        """
        Calculates the normalized D' from Weir Genetic Analysis II 1986 pg. 120

        Signatures:

        static double calculateDPrime(int countAB, int countAb, int countaB, int countab, int minTaxaForEstimate)

        Arguments:

        countAB -- Count of AB alleles
        countAb -- Count of Ab alleles
        countaB -- Count of aB alleles
        countab -- Count of ab alleles
        minTaxaForEsimate -- The minimum number of taxa required for the estimate

        Returns:

        Value of D'
        """
        pass
    ## Calculates the normalized r2 from Awadella Science 1999 286:2524
    # @param countAB Count of AB alleles
    # @param countAb Count of Ab alleles
    # @param countaB Count of aB alleles
    # @param countab Count of ab alleles
    # @return Value of r2
    @javaStaticOverload(java_imports['LinkageDisequilibrium'],"calculateRSqr",
                        (make_sig(['int','int','int','int','int'],'double'),
                         (metaInteger,metaInteger,metaInteger,metaInteger,metaInteger),
                         np.float64))
    def calculateRSqr(*args):
        """
        Calculates the normalized r2 from Awadella Science 1999 286:2524

        Signatures:

        static double calculateRSqr(int countAB, int countAb, int countaB, int countab, int minTaxaForEstimate)

        Arguments:

        countAB -- Count of AB alleles
        countAb -- Count of Ab alleles
        countaB -- Count of aB alleles
        countab -- Count of ab alleles
        minTaxaForEsimate -- The minimum number of taxa required for the estimate

        Returns:

        Value of r2
        """
        pass
    ## Method for estimating LD between a pair of bit sets. Since there can be tremendous
    # missing data, minimum minor and minimum site counts ensure that meaningful results
    # are estimated. Site indices are merely there for annotating the LDresult
    # @param rMj site 1 major alleles
    # @param rMn site 1 minor alleles
    # @param cMj site 2 major alleles
    # @param cMn site 2 minor alleles
    # @param minMinorCnt minimum minor allele count after intersection
    # @param minCnt minimum count after intersection
    # @param minR2 results below this r2 are ignored for p-value calculation (save time)
    # @param myFisherExact Instance of FisherExact to do Fisher Exact test
    # @param site1Index Annotation of LDResult with site indices
    # @param site2Index Annotation of LDResult with site indices
    # @return An LDResult for the pair of sites
    @javaStaticOverload(java_imports["LinkageDisequilibrium"],"getLDForSitePair",
        (make_sig([java_imports['BitSet'],java_imports['BitSet'],java_imports['BitSet'],
                   java_imports['BitSet'],'int','int','float',java_imports['FisherExact'],
                   'int','int'],java_imports['LDResult']),
        (BitSet,BitSet,BitSet,BitSet,metaInteger,metaInteger,metaFloat,FisherExact,
         metaInteger,metaInteger),lambda x: LDResult(obj=x)))
    def getLDForSitePair(*args):
        """
        Method for estimating LD between a pair of bit sets. Since there can be tremendous missing
        data, minimum minor and minimum site counts ensure that meaningful results are estimated. Site
        indices are merely there for annotating the LDResult.

        Signatures:

        static LDResult getLDForSitePair(BitSet rMj, BitSet rMn,
                                         BitSet cMj, BitSet cMn,
                                        int minMinorCnt, int minCnt,
                                        float minR2, FisherExact myFisherExact,
                                        int site1Index, int site2Index)

        Arguments:

        rMj -- site 1 major alleles
        rMn -- site 1 minor alleles
        cMj -- site 2 major alleles
        cMn -- site 2 minor alleles
        minMinorCnt -- minimum minor allele count after intersection
        minCnt -- minimum count after intersection
        minR2 -- results below this r2 are ignored for p-value calculation (save time)
        myFisherExact -- Instance of FisherExact to do Fisher Exact test
        site1Index -- Annotation of LDResult with site indices
        site2Index -- Annotation of LDResult with site indices

        Returns:

        An LDResult for the pair of sites
        """
        pass
    ## Returns P-value estimate for a given pair of numPSites. If there were only 2 alleles
    # at each locus, then the Fisher Exact P-value (one-tail) is returned. If more states, then
    # the permuted Monte Carlo test is used
    # @param r site 1
    # @param c site 2
    # @return p-value
    @javaOverload("getPVal",
        (make_sig(['int','int'],'double'),(metaInteger,metaInteger),np.float64))
    def getPval(self, *args):
        """
        Returns P-value estimate for a given pair of numPSites. If there were only
        2 alleles at each locus, then the Fisher Exact P-value (one-tail) is returned.
        If more states, then the permuted Monte Carlo test is used

        Signatures:

        double getPVal(int r, int c)

        Arguments:

        r -- site 1
        c -- site 2

        Returns:

        P-value
        """
        pass
    ## Gets number of gametes included in LD calculations (after missing data was excluded)
    # @param r site 1
    # @param c site 2
    # @return p-value
    @javaOverload("getSampleSize",
            (make_sig(['int','int'],'int'),(metaInteger,metaInteger),None))
    def getSampleSize(self, *args):
        """
        Get number of gametes included in LD calculations (after missing data
        was excluded)

        Signatures:

        int getSampleSize(int r, int c)

        Arguments:

        r -- site 1
        c -- site 2

        Returns:

        Number of gametes
        """
        pass
    ## Gets the D' estimate for a given pair of numSites
    # @param r site 1
    # @param c site 2
    # @return D' 
    @javaOverload("getDPrime",
            (make_sig(['int','int'],'float'),(metaInteger,metaInteger),None))
    def getDPrime(self, *args):
        """
        Gets the D' estimate for a given pair of numSites

        Signatures:

        float getDPrime(int r, int c)

        Arguments:

        r -- site 1
        c -- site 2

        Returns:

        D'
        """
        pass
    ## Gets the r2 estimate for a given pair of numSites
    # @param r site 1
    # @param c site 2
    # @return r2
    @javaOverload("getRSqr",
            (make_sig(['int','int'],'float'),(metaInteger,metaInteger),None))
    def getRSqr(self, *args):
        """
        Gets the r2 estimate for a given pair of numSites

        Signatures:

        float getRSqr(int r, int c)

        Arguments:

        r -- site 1
        c -- site 2

        Returns:

        r2
        """
        pass
    @javaOverload("getX",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def getX(self, *args):
        """
        Signatures:

        int getX(int row)

        Arguments:

        row -- row

        Returns:

        X
        """
        pass
    @javaOverload("getY",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def getY(self, *args):
        """
        Signatures:

        int getY(int row)

        Arguments:

        row -- row

        Returns:

        Y
        """
        pass
    ## Gets the counts of the numSites in the alignment
    # @return The counts of the numSites in the alignment
    @javaOverload("getSiteCount",
        (make_sig([],'int'),(),None))
    def getSiteCount(self, *args):
        """
        Gets the counts of the numSites in the alignment

        Signatures:

        int getSiteCount()

        Returns:

        The counts of the numSites in the alignment
        """
        pass
    ## Returns an annotated alignment if one was used for this LD. This could
    # be used to access information of locus position
    # @return The GenotypeTable
    @javaOverload("getAlignment",
                  (make_sig([],java_imports['GenotypeTable']),(),
                   lambda x: GenotypeTable(obj=x)))
    def getAlignment(self, *args):
        """
        Returns an annotated alignment if one was used for this LD. This could
        be used to access information of locus position

        Signatures:

        GenotypeTable getAlignment

        Returns:

        The GenotypeTable
        """
        pass
