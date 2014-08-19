from TASSELpy.net.maizegenetics.util.OpenBitSet import OpenBitSet
from TASSELpy.javaObj import javaObj
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import String
from TASSELpy.java.lang.Long import Long
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Byte import metaByte
from TASSELpy.java.lang.Integer import metaInteger
import javabridge
import numpy as np



## Dictionary to hold java imports
java_imports = {'genotypecall':'net/maizegenetics/dna/snp/genotypecall', 
        'GenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/GenotypeCallTable',
        'String':'java/lang/String',
        'Object':'java/lang/Object',
        'Boolean':'java/lang/Boolean'}

class GenotypeCallTable(Object):
    """ Interface for genotype calls for a table of taxa and sites.
    GenotypeCallTable only contain information on the genotype calls. The call
    table does not have the TaxaList or PositionList. The calls are diploid genotype
    calls stored and retrieved as bytes. Conversions to string are also provided.

    Generally these methods are accessed through the GenotypeTable interface
    """
    _java_name = java_imports['GenotypeCallTable']
    @javaConstructorOverload(java_imports['GenotypeCallTable'])
    def __init__(self, *args, **kwargs):
        pass
    @javaOverload("genotype", (make_sig(['int', 'int'], 'byte'), (metaInteger, metaInteger), None))
    def genotype(self, *args):
        """ Returns diploid value (genotype) for a given taxon and site

        Signatures:

        byte genotype(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        High 4 bites generally encode the more frequent allele, and the lower
        4 bits encode the less frequent allele
        """
        pass
    @javaOverload("genotypeArray", (make_sig(['int', 'int'], 'byte[]'), (metaInteger, metaInteger), None))
    def genotypeArray(self, *args):
        """ Returns the diploid values for given taxon and site

        Same values as genotype(), except two values are already separated into two bytes

        Signatures:

        byte[] genotypeArray(int taxon, int site)

        Returns:

        First byte (index 0) hold sfirst allele value in right-most 4 bits. Second byte (index 1)
        holds second value in right-most 4 bits
        """
        pass
    @javaOverload("genotypeRange",(make_sig(['int','int','int'],'byte[]'),(metaInteger, metaInteger, metaInteger),None))
    def genotypeRange(self, *args):
        """ Returns sequence of diploid allele values for given taxon in specified range (end site excluded).
        Each value in array is what would be returned by genotype().

        Signatures:

        byte[] genotypeRange(int taxon, int startSite, int endSite)

        Arguments:

        taxon -- taxon
        startSite -- start site
        endSite -- end site

        Returns:

        sequence of diploid allele values     
        """
        pass
    @javaOverload("genotypeAllSites",(make_sig(['int'],'byte[]'),(metaInteger,),None))
    def genotypeAllSites(self, *args):
        """ Returns sequence of diploid allele values for all sites for given taxon

        Each value in array is what would be returned by genotype()

        Signatures:

        byte[] genotypeAllSites(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        Sequence of diploid allele values
        """
        pass
    @javaOverload("genotypeAsString",(make_sig(['int','int'],java_imports['String']),(metaInteger,metaInteger),None),
                  (make_sig(['int','byte'],java_imports['String']),(metaInteger,metaByte),None))
    def genotypeAsString(self, *args):
        """ Returns string representation of diploid allele values returned
        by genotype() for given taxon and site. The two allele values will be
        separated by a colon(:) delimiter

        Signatures:

        String genotypeAsString(int taxon, int site)
        String genotypeAsString(int site, byte value)

        Arguments:

        String genotypeAsString(int taxon, int site)
            taxon -- taxon
            site -- site
        String genotypeAsString(int site, byte value)
            site -- site
            value -- diploid allele value

        Returns:

        String representation
        """
        pass
    @javaOverload("genotypeAsStringRange",(make_sig(['int','int','int'],java_imports['String']),    
            (metaInteger,metaInteger,metaInteger),None))
    def genotypeAsStringRange(self, *args):
        """ Returns string representation of diploid alleles for given taxon in
        specified range (end site excluded). Each vlaue in string is what would
        be returned by genotypeAsString

        Signatures:

        String genotypeAsStringRange(int taxon, int startSite, int endSite)

        Arguments:

        taxon -- taxon
        startSite -- start site
        endSite -- end site

        Returns:

        String representation of alleles in range
        """
        pass
    @javaOverload("genotypeAsStringRow",(make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def genotypeAsStringRow(self, *args):
        """ Returns string representation of diploid alleles for given taxon for all sites.

        Each value in string is what would be returned by genotypeAsString()

        Signatures:

        String genotypeAsStringRow(int taxon)
        
        Arguments:

        taxon -- taxon

        Returns:

        String representation of alleles
        """
        pass
    @javaOverload("genotypeAsStringArray",(make_sig(['int','int'],java_imports['String']+'[]'),
            (metaInteger,metaInteger),lambda x: map(lambda y: javabridge.get_env().get_string(y),
                                 javabridge.get_env().get_object_array_elements(x))))
    def genotypeAsStringArray(self, *args):
        """ Returns string representation of diploid values returned by genotypeArray() for
        given taxon and site. Same 2 allele values as genotypeAsString(), except already separated
        into 2 Strings

        Signatures:

        String[] genotypeAsStringArray(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        String representation of diploid vlaues
        """
        pass
    @javaOverload("isHeterozygous", (make_sig(['int', 'int'], 'boolean'),(metaInteger, metaInteger),    
            None))
    def isHeterozygous(self, *args):
        """ Returns whether allele values at given taxon and site are heterozygous.
        If 2 values returned by genotype() are different, this will return false

        Signatures:

        boolean isHeterozygous(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        Whether heterozygous
        """
        pass
    @javaOverload("heterozygousCount",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def heterozygousCount(self, *args):
        """ Returns the number of heterozygous taxa at given site

        Signatures:

        int heterozygousCount(int site)

        Arguments:

        site -- site

        Returns:

        Number of heterozygous taxa
        """
        pass
    @javaOverload("isAllPolymorphic",
                  (make_sig([],'boolean'),(),None))
    def isAllPolymorphic(self, *args):
        """ Returns whether all sites are polymorphic

        Signatures:

        boolean isAllPolymorphic()

        Returns:

        true if all sites are polymorphic
        """
        pass
    @javaOverload("isPolymorphic", (make_sig(['int'], 'boolean'),(metaInteger,),None))
    def isPolymorphic(self, *args):
        """ Returns whether a given site is polymorphic

        Signatures:

        boolean isPolymorphic(int site)

        Arguments:

        site -- site

        Returns:

        true if given site is polymorphic
        """
        pass
    @javaOverload("isPhased", (make_sig([],'boolean'),(),None))
    def isPhased(self, *args):
        """ Returns whether this alignment is phased

        Signatures:

        boolean isPhased()

        Returns:

        true if phased
        """
        pass
    @javaOverload("retainsRareAlleles", (make_sig([],'boolean'),(),None))
    def retainsRareAlleles(self, *args):
        """ Returns true if this Alignment retains rare alleles. If false,
        rare alleles are recorded as unknown

        Signatures:

        boolean retainsRareAlleles()

        Returns:

        Whether rare alleles are retained
        """
        pass
    @javaOverload("alleleDefinitions",(make_sig([],java_imports['String']+'[][]'),(), 
            lambda x: javaArray.get_array_type(String).wrap_existing_array(x)),
                (make_sig(['int'],java_imports['String']+'[]'),(metaInteger,),
            lambda x: String.wrap_existing_array(x)))
    def alleleDefinitions(self, *args):
        """ Returns allele values as strings for all sites or for only one site.

        For the all sites definition, the first dimension of the array indexes
        the sites. The second dimension indexes the allele values for a given site.
        The indices for the allele vlaues are used as the codes to store data. These
        codes (indices) are returned by the genotypes() methods. If only one array of allele
        values is returned, that is the encoding for all sites

        Signatures:

        String[][] alleleDefinitions()
        String[] alleleDefinitions(int site)

        Arguments:

        String[] alleleDefinitions(int site)
            site -- site

        Returns:

        Allele values for given site
        """
        pass
    @javaOverload("diploidAsString",(make_sig(['int','byte'],java_imports['String']),(metaInteger,metaByte),
                   None))
    def diploidAsString(self, *args):
        """ Returns String representation of diploid allele vlaue at site

        Signatures:

        String diploidAsString(int site, byte value)

        Arguments:

        site -- site
        value -- diploid allele value

        Returns:

        String representation
        """
        pass
    @javaOverload("maxNumAlleles",(make_sig([],'int'),(),None))
    def maxNumAlleles(self, *args):
        """ Return maximum number of alleles defined for any given site

        Signatures:

        int maxNumAlleles()

        Returns:

        max number of alleles
        """
        pass
    @javaOverload("totalGametesNonMissingForSite",(make_sig(['int'],'int'),(metaInteger,),None))
    def totalGametesNonMissingForSite(self, *args):
        """ Returns total number of non-missing allele values for given site. This can
        be twice the number of taxa, as diploid vlaues are supported

        Signatures:

        int totalGametesNonMissingForSite(int site)


        Arguments:

        site -- site
        
        Returns:

        number of non-missing allele values
        """
        pass
    @javaOverload("totalNonMissingForSite",(make_sig(['int'],'int'),(metaInteger,),None))
    def totalNonMissingForSite(self, *args):
        """ Returns total number of non-missing taxa for given site. Taxa are considered
        missing only if both allele values are Unknown (N).

        Signatures:

        int totalNonMissingForSite(int site)

        Arguments:

        site -- site

        Returns:

        number of non-missing taxa
        """
        pass
    @javaOverload("minorAllele",(make_sig(['int'],'byte'),(metaInteger,),None))
    def minorAllele(self, *args):
        """ Return most common minor allele at given site.
        Gap is included as state. Heterozygous count one for each allele value.
        Homozygous counts 2 for the allele value

        Signatures:

        byte minorAllele(int site)

        Arguments:

        site -- site

        Returns:

        most common minor allele
        """
        pass
    @javaOverload("minorAlleleCount",(make_sig(['int'],'int'),(metaInteger,),None))
    def minorAlleleCount(self, *args):
        """ Returns the minor allele count for the given site

        Signatures:

        int minorAlleleCount(int site)

        Arguments:

        site -- site

        Retuns:

        minor allele count
        """
        pass
    @javaOverload("majorAlleleCount",(make_sig(['int'],'int'),(metaInteger,),None))
    def majorAlleleCount(self, *args):
        """ Returns the major allele count for given site

        Signatures:

        int majorAlleleCount(int site)

        Arguments:

        site -- site

        Returns:

        major allele count
        """
        pass
    @javaOverload("genoCounts",(make_sig([],java_imports['Object']+'[][]'),(),
                lambda x: javaArray.get_array_type(Object).wrap_existing_array(x)))
    def genoCounts(self, *args):
        """ Returns counts of all diploid combinations from highest frequency to lowest
        for whole alignment. Resulting double dimension array holds diploids (Strings)
        in result[0]. And the counts are in result[1] (Longs)

        Signatures:

        Object[][] genoCount()

        Returns:

        diploid counts
        """
        pass

    @javaOverload("majorMinorCounts",(make_sig([],java_imports['Object']+'[][]'),(),
                lambda x: javaArray.get_array_type(Object).wrap_existing_array(x)))
    def majorMinorCounts(self, *args):
        """ Returns counts of all major/minor allele combinations from highest
        frequency to lowest for whole alignment. Resulting double dimension array
        holds major/minor allele (Strings) in result[0]. And the counts are in
        result[1] (Longs)

        Signatures:

        Object[][] majorMinorCounts()

        Returns:

        diploid counts
        """
        pass
    @javaOverload("totalGametesNonMissingForTaxon",(make_sig(['int'],'int'),(metaInteger,),None))
    def totalGametesNonMissingForTaxon(self, *args):
        """ Returns number of non-missing allele values for given taxon. This can be
        twice the number of sites, as diploid values are supported

        Signatures:

        int totalGametesNonMissingForTaxon(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        number of non-missing allele values
        """
        pass
    @javaOverload("heterozygousCountForTaxon",(make_sig(['int'],'int'),(metaInteger,),None))
    def heterozygousCountForTaxon(self, *args):
        """ Returns number of heterozygous sites at given taxon

        Signatures:

        int heterozygousCountForTaxon(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        number of heterozygous sites
        """
        pass
    @javaOverload("totalNonMissingForTaxon",(make_sig(['int'],'int'),(metaInteger,),None))
    def totalNonMissingForTaxon(self, *args):
        """ Returns total number of non-missing sites for given taxon.

        Sites are considered missing only if both allele values are unknown (N).

        Signatures:

        int totalNonMissingForTaxon(int taxon)

        Arguments:

        taxon -- taxon
        """
        pass
    @javaOverload("allelesSortedByFrequency",(make_sig(['int'],'int[][]'),(metaInteger,),
                   lambda x: javaPrimativeArray.get_array_type('int').wrap_existing_array(x)))
    def allelesSortedByFrequency(self, *args):
        """ Returns sorted list of alleles from highest frequency to lowest at given
        site in alignment. Resulting double dimension array holds alleles (bytes) in
        result[0]. And the counts are in result[1]. Counts haploid values twice and
        diploid values once. Higher ploidies are not supported

        Signatures:

        int[][] allelesSortedByFrequency(int site)

        Arguments:

        site -- site

        Returns:

        Sorted list of alleles and counts
        """
        pass
    @javaOverload("genosSortedByFrequency",(make_sig(['int'],java_imports['Object']+'[][]'),(metaInteger,),
                   lambda x: javaArray.get_array_type(Object).wrap_existing_array(x)))
    def genosSortedByFrequency(self, *args):
        """ Return sorted list of diploid values from highest frequency to lowest at
        given site in alignment. Resulting double dimension array holds diploids (Strings)
        in result[0]. And the counts are in result[1] (Integers).

        Signatures:

        Object[][] genosSortedByFrequency(int site)

        Arguments:

        site -- site

        Returns:

        sorted list of diploids and counts
        """
        pass
    @javaOverload("alleles",(make_sig(['int'],'byte[]'),(metaInteger,),None))
    def alleles(self, *args):   
        """ Returns all alleles at given site in order of frequency. Gap
        is included as state. Heterozygous count one for each allele value. Homozygous
        counts 2 for the allele value

        Signatures:

        byte[] alleles(int site)

        Arguments:

        site -- site

        Returns:

        all alleles
        """
        pass
    @javaOverload("majorAlleleForAllSites", (make_sig([], 'byte[]'), (), None))
    def majorAlleleForAllSites(self, *args):
        """ Returns major allele for all sites

        Signatures:

        byte[] majorAlleleForAllSites()

        Returns:

        all major alleles
        """
        pass
    @javaOverload("minorAlleleForAllSites", (make_sig([], 'byte[]'), (), None))
    def minorAlleleForAllSites(self, *args):
        """ Returns minor allele for all sites

        Signatures:

        byte[] minorAlleleForAllSites()

        Returns:

        all minor alleles
        """
        pass
    @javaOverload("majorAllele",(make_sig(['int'],'byte'),(metaInteger,),None))
    def majorAllele(self, *args):
        """ Returns most common allele at given site.

        Gap is included as state. Heterozygous count one for each allele value.
        Homozygous count 2 two for the allele value

        Signatures:

        byte majorAllele(int site)

        Arguments:

        site -- site

        Returns:

        most common allele
        """
        pass    
    @javaOverload("majorAlleleAsString",(make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def majorAlleleAsString(self, *args):
        """ Returns most common allele at given site. Gap is included as state. Heterozygous
        count one for each allele vlaue. Homozygous counts 2 for the allele value

        Signatures:

        String majorAlleleAsString(int site)

        Arguments:

        site -- site

        Returns:

        most common allele as String
        """
        pass
    @javaOverload("minorAlleleAsString",(make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def minorAlleleAsString(self, *args):
        """ Return most common minor allele at given site. Gap is included as state.
        Heterozygous count one for each allele value. Homozygous counts 2 for the allele value

        Arguments:

        site -- site

        Returns:

        Most common minor allele as String
        """
        pass
    @javaOverload("minorAlleles",(make_sig(['int'],'byte[]'),(metaInteger,),None))
    def minorAlleles(self, *args):
        """ Return all minor alleles at given site.

        Gap is included as state. Heterozygous count 1 for each allele value. Homozygous
        counts 2 for the allele value

        Arguments:

        site -- site

        Returns:

        all minor alleles
        """
        pass
    @javaOverload("minorAlleleFrequency",(make_sig(['int'],'double'),(metaInteger,),np.float64))
    def minorAlleleFrequency(self, *args):
        """ Return frequency for the most common minor allele at given site. Gap is
        included as state. Heterozygous count 1 for each allele value. Homozygous count
        2 for the allele value

        Signatures:

        double minorAlleleFrequency(int site)

        Arguments:

        site -- site

        Returns:

        frequency
        """
        pass
    @javaOverload("majorAlleleFrequency",(make_sig(['int'],'double'),(metaInteger,),np.float64))
    def majorAlleleFrequency(self, *args):
        """ Returns frequency for major allele at given site. Gap is included as state.
        Heterozygous count 1 for each allele value. Homozygous count 2 for the allele value

        Signatures:

        double majorAlleleFrequency(int site)

        Arguments:

        site -- site

        Returns:

        frequency
        """
        pass
    @javaOverload("numberOfSites",(make_sig([],'int'),(),None))
    def numberOfSites(self, *args):
        """ Returns number of sites in this genotype

        Signatures:

        int numberOfSites()

        Returns:

        number of sites
        """
        pass
    @javaOverload("numberOfTaxa",(make_sig([],'int'),(),None))
    def numberOfTaxa(self, *args):
        """ Returns number of taxa (samples) in this genotype

        Signatures:

        int numberOfTaxa()

        Returns:

        number of taxa
        """
        pass
    @javaOverload("genotypeForAllSites",(make_sig(['int'],'byte[]'),(metaInteger,),None))
    def genotypeForAllSites(self, *args):
        """ Get all genotypes for given taxon

        Signatures:

        byte[] genotypeForAllSites(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        genotypes
        """
        pass
    @javaOverload("genotypeForSiteRange",(make_sig(['int', 'int', 'int'],'byte[]'),(metaInteger, metaInteger, 
        metaInteger),None))
    def genotypeForSiteRange(self, *args):
        """ Get all genotypes for given taxon from start site (inclusive) to end site
        (exclusive)

        Signatures:

        byte[] genotypeForSiteRange(int taxon, int start, int end)

        Arguments:

        taxon -- taxon
        start --- start
        end -- end

        Returns:

        genotypes
        """
        pass
    @javaOverload("genotypeForAllTaxa",(make_sig(['int'],'byte[]'),(metaInteger,),None))
    def genotypeForAllTaxa(self, *args):
        """ Get all genotypes for given site

        Signatures:

        byte[] genotypeForAllTaxa(int site)

        Arguments:

        site -- site

        Returns:

        genotypes
        """
        pass
    @javaOverload("transposeData", (make_sig(['boolean'],'void'), (metaBoolean,), None))
    def transposeData(self, *args):
        """ Tells this Genotype to transpose its data to optimize performance for
        given iteration nesting. If siteInnerloop is true, performance better
        when looping through sites inside taxa loop. If false, performance better
        when looping through taxa inside site loop

        Signatures:

        void transposeData(boolean siteInnerLoop)

        Arguments:

        siteInnerLoop -- flag for which iteration
        """
        pass











