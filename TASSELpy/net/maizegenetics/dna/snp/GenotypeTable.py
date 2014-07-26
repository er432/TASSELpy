from TASSELpy.net.maizegenetics.util.OpenBitSet import OpenBitSet
from TASSELpy.net.maizegenetics.dna.WHICH_ALLELE import WHICH_ALLELE
from TASSELpy.net.maizegenetics.dna.map.Chromosome import Chromosome
from TASSELpy.net.maizegenetics.dna.snp.depth.AlleleDepth import AlleleDepth
from TASSELpy.net.maizegenetics.dna.map.PositionList import PositionList
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.java.lang.Enum import enum as java_enum
from TASSELpy.java.lang.Enum import Enum
from TASSELpy.java.lang.String import String
from TASSELpy.java.lang.Long import Long
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Byte import metaByte
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
import numpy as np
import javabridge


## Dictionary to hold java imports
java_imports = {'AlleleDepth':'net/maizegenetics/dna/snp/depth/AlleleDepth',
                'BitSet':'net/maizegenetics/util/BitSet',
                'BitStorage':'net/maizegenetics/dna/snp/bit/BitStorage',
                'Chromosome':'net/maizegenetics/dna/map/Chromosome',
                'CoreGenotypeTable':'net/maizegenetics/dna/snp/CoreGenotypeTable',
                'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'GenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/GenotypeCallTable',
                'Object':'java/lang/Object',
                'PositionList':'net/maizegenetics/dna/map/PositionList',
                'SiteScore':'net/maizegenetics/dna/snp/score/SiteScore',
                'String':'java/lang/String',
                'TaxaList':'net/maizegenetics/taxa/TaxaList',
                'WHICH_ALLELE':'net/maizegenetics/dna/WHICH_ALLELE'}

## Class only used to allow GenotypeTable to refer to itself
class MetaGenotypeTable(Object):
    pass

class GenotypeTable(MetaGenotypeTable):
    """
    A representation of the SNP and indel variation for a set of taxa
    and genomic positions.

    GenotypeTable always consists of a TaxaList, PositionList, and
    GenotypeCallTable. Additionally, as needed they also represent alleles
    in bit form, with sequencing depth, or other scores (e.g. quality scores).

    Use GenotypeTableBuilder to create GenotypeTable
    """
    ## SITE_SCORE_TYPE enum
    SITE_SCORE_TYPE=java_enum(java_imports['GenotypeTable']+'$SITE_SCORE_TYPE',
                              "None","MixedScoreTypes","QualityScore",
                              "ImputedProbablity","Dosage",
                              subclass='SITE_SCORE_TYPE')
    ## ALLELE_SORT_TYPE enum
    ALLELE_SORT_TYPE=java_enum(java_imports['GenotypeTable']+'$ALLELE_SORT_TYPE',
                            "Frequency","Depth","Global_Frequency","Reference",
                            subclass='ALLELE_SORT_TYPE')
    _java_name = java_imports['GenotypeTable']
    @javaConstructorOverload(java_imports['GenotypeTable'])
    def __init__(self,*args,**kwargs):
        pass
    ## Returns the immutable genotype matrix. Taxa and positions are
    # not part of the matrix. This method is used for copying genotype tables,
    # when either the taxa or positions have changed
    # @return genotype matrix
    @javaOverload("genotypeMatrix",
                  (make_sig([],java_imports['GenotypeCallTable']),(),None))
    def genotypeMatrix(self, *args):
        """
        Returns the immutable genotype matrix. Taxa and positions are not
        part of the matrix. This method is used for copying genotype tables,
        when either the taxa or positions have changed

        Signatures:

        GenotypeCallTable genotypeMatrix()
        
        Returns:

        Genotype matrix
        """
        pass
    ## Returns diploid values for given taxon and site. Same values as
    # genotype(), except two values are already separated into two bytes
    # @param taxon taxon
    # @param site site
    # @return First byte (index 0) holds first allele value in right-most four
    # bits. Second byte (index 1) holds second allele value in right-most four
    # bits
    @javaOverload("genotypeArray",
                  (make_sig(['int','int'],'byte[]'),(metaInteger, metaInteger),None))
    def genotypeArray(self, *args):
        """
        Returns diploid values for given taxon and site. Same values as
        genotype(), except two values are already separated into two bytes.

        Signatures:

        byte[] genotypeArray(int taxon, int site)
        
        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        First byte (index 0) holds first allele value in right-most four
        bits. Second byte (index 1) holds second allele value in right-most four
        bits
        """
        pass
    ## Returns diploid value (genotype) for a given taxon and site
    # @param taxon taxon
    # @param site site
    # @return High four bits generally encode the more frequent allele and
    # the lower four bits encode the less frequent allele
    @javaOverload("genotype",
                  (make_sig(['int','int'],'byte'), (metaInteger, metaInteger),np.int8),
                  (make_sig(['int',java_imports['Chromosome'],'int'],'byte'),
                    (metaInteger, Chromosome, metaInteger),np.int8))
    def genotype(self, *args):
        """
        Returns diploid value (genotype) for a given taxon and site

        Signatures:

        byte genotype(int taxon, int site)
        byte genotype(int taxon, Chromosome chromosome, int physicalPosition)
        
        Arguments:
           genotype(int taxon, int site):
              taxon -- taxon
              site -- site
           genotype(int taxon, Chromosome chromosome, int physicalPosition):
              taxon -- taxon
              chromosome -- chromosome
              physicalPosition -- physicalPosition

        Returns:

        High four bits generally encode more frequent allele and lower
        four bits encode the less frequent allele
        """
        pass
    ## Returns sequence of diploid allele values for given taxon in
    # specified range (end site excluded). Each value in array is what
    # would be returned by genotype().
    # @param taxon taxon
    # @param startSite start site
    # @param endSite end site
    # @return sequence of diploid allele values
    @javaOverload("genotypeRange",
                  (make_sig(['int','int','int'],'byte[]'),(metaInteger, metaInteger, metaInteger),
                   None))
    def genotypeRange(self, *args):
        """
        Returns sequence of diploid allele values for given taxon in specified
        range (end site excluded). Each value in array is what would be returned
        by genotype()

        Signatures:

        byte[] genotypeRange(int taxon, int startSite, int endSite)
        
        Arguments:

        taxon -- taxon
        startSite -- start site
        endSite -- end site

        Returns:

        Sequence of diploid allele values
        """
        pass
    ## Returns sequence of diploid allele values for all sites for given
    # taxon. Each value is what would be returned by genotype().
    # @param site site
    # @return Sequence of diploid allele values
    @javaOverload("genotypeAllSites",
                  (make_sig(['int'],'byte[]'),(metaInteger,),None))
    def genotypeAllSites(self, *args):
        """
        Returns sequence of diploid allele values for all taxa for given site.
        Each value in array is what would be returned by genotype().

        Signatures:

        byte[] genotypeAllSites(int taxon)
        
        Arguments:

        site -- site

        Returns:

        Sequence of diploid allele values
        """
        pass
    ## Returns sequence of diploid allele values for all taxa for
    # a given site. Each value in array is what would be returned by
    # genotype().
    # @param site site
    # @return Sequence of diploid allele values
    @javaOverload("genotypeAllTaxa",
                  (make_sig(['int'],'byte[]'),(metaInteger,),None))
    def genotypeAllTaxa(self, *args):
        """
        Returns sequence of diploid allele values for all taxa for given
        site. Each value in array is what would be returned by genotype().

        Signatures:

        byte[] genotypeAllTaxa(int site)
        
        Arguments:

        site -- site

        Returns:

        Sequence of diploid allele values
        """
        pass
    ## Returns sequence of true/false values indicating whether taxon at
    # each site matches a specific allele (based on frequency). Allele
    # number of value 0 would be the major allele. Allele number of value 1
    # would be the minor allele. Allele number of value 2 would be the third
    # most frequent allele value and so on.
    # @param taxon taxon
    # @param allele allele
    # @return Sequence of true/false value
    @javaOverload("allelePresenceForAllSites",
                  (make_sig(['int',java_imports['WHICH_ALLELE']],java_imports['BitSet']),
                   (metaInteger,WHICH_ALLELE.subclass),lambda x: OpenBitSet(obj=x)))
    def allelePresenceForAllSites(self, *args):
        """
        Returns sequence of true/false values indicating whether taxon at
        each site matches a specific allele (based on frequency). Allele
        number of value 0 would be the major allele. Allele number of value 1
        would be the minor allele. Allele number of value 2 would be the third
        most frequent allele value and so on.

        Signatures:

        BitSet allelePresenceForAllSites(int taxon, WHICH_ALLELE allele)
        
        Arguments:

        taxon -- taxon (int)
        allele -- allele (WHICH_ALLELE)

        Returns:

        Sequence of true/false value (BitSet)
        """
        pass
    ## Returns sequence of true/false values indicating whether taxon at site
    # (in given blocks, 64 sites per block including start block but excluding
    # end block) matches a specific allele
    # @param taxon taxon
    # @param allele allele
    # @param startBlock starting block
    # @param endBlock end block
    # @return sequence of true/false values
    @javaOverload("allelePresenceForSitesBlock",
                  (make_sig(['int',java_imports['WHICH_ALLELE'],
                             'int','int'],'long[]'),
                   (metaInteger,WHICH_ALLELE.subclass,metaInteger,metaInteger),
                  lambda x: javaPrimativeArray.make_array_from_obj('long',x)))
    def allelePresenceForSitesBlock(self, *args):
        """
        Returns sequence of true/false values indicating whether taxon at site
        (in given blocks, 64 sites per block including start block but excluding
        end block) matches a specific allele

        Signatures:

        long[] allelePresenceForSitesBlock(int taxon, WHICH_ALLELE allele, int startBlock, int endBlock)
        
        Arguments:

        taxon -- taxon (int)
        allele -- allele (WHICH_ALLELE)
        startBlock -- starting block (int)
        endBlock -- end block (int)

        Returns:

        Sequence of true/false values (long[])
        """
        pass
    ## Returns sequence of true/false values indicating whether taxon at each site
    # for given parent matches a specific allele
    # @param taxon taxon
    # @param firstParent true for first parent (false for second parent)
    # @param allele allele
    # @return sequence of true/false values
    @javaOverload("haplotypeAllelePresenceForAllSites",
                  (make_sig(['int','boolean',java_imports['WHICH_ALLELE']],
                            java_imports['BitSet']),
                   (metaInteger,bool,WHICH_ALLELE.subclass),lambda x: OpenBitSet(obj=x)))
    def haplotypeAllelePresenceForAllSites(self, taxon, firstParent, allele):
        """
        Returns sequence of true/false values indicating whether taxon at each
        site for given parent matches a specific allele

        Signatures:

        BitSet haplotypeAllelePresenceForAllSites(int taxon, boolean firstParent, WHICH_ALLELE allele)
        
        Arguments:

        taxon -- taxon (int)
        firstParent -- true for first parent (false for second parent)
        allele -- allele (WHICH_ALLELE)

        Returns:

        Sequence of true/false values (BitSet)
        """
        pass
    ## Returns sequence of true/false values indicating whether site at each taxon
    # for given parent matches a specific allele (based on frequency). Allele number
    # of value 0 would be the major allele. Allele number of value 1 would be the
    # minor allele. Allele number of value 2 would be the third most frequent allele
    # value and so on
    # @param site site (int)
    # @param firstParent true for first parent (false for second parent) (boolean)
    # @param allele allele (WHICH_ALLELE)
    # @return sequence of true/false values (BitSet)
    @javaOverload("haplotypeAllelePresenceForAllTaxa",
                  (make_sig(['int','boolean',java_imports['WHICH_ALLELE']],
                            java_imports['BitSet']),
                   (metaInteger,bool,WHICH_ALLELE.subclass),lambda x: OpenBitSet(obj=x)))
    def haplotypeAllelePresenceForAllTaxa(self, *args):
        """
        Returns a sequence of true/false values indicating whether site at each
        taxon for given parent matches a specific allele (based on frequency).
        Allele number of value 0 would be the major allele. Allele number of value
        1 would be the minor allele. Allele number of value 2 would be the third
        most frequent allele value and so on

        Signatures:

        BitSet haplotypeAllelePresenceForAllTaxa(int site, boolean firstParent, WHICH_ALLELE allele)
        
        Arguments:

        site -- site (int)
        firstParent -- true for first parent (false for second parent)
        allele -- allele (WHICH_ALLELE)

        Returns:

        Sequence of true/false values (BitSet)
        """
        pass
    ## Returns sequence of true/false values indicating whether taxon at sites
    # (in given blocks, 64 sites per block including start block but excluding
    # end block) for given parent matches a specific allele (based on frequency).
    # Allele number of value 0 would be the major allele. Allele number of value 1
    # would be the minor allele. Allele number of value 2 would be the third most
    # frequent allele value and so on.
    # @param taxon taxon (int)
    # @param firstParent true for first parent (false for second parent)
    # @param allele allele (WHICH_ALLELE)
    # @param startBlock starting block (int)
    # @param endBlock ending block (int)
    @javaOverload("haplotypeAllelePresenceForSitesBlock",
                  (make_sig(['int','boolean',java_imports['WHICH_ALLELE'],
                             'int','int'],'long[]'),
                   (metaInteger,bool,WHICH_ALLELE.subclass,metaInteger,metaInteger),
                  lambda x: javaPrimativeArray.make_array_from_obj('long',x)))
    def haplotypeAllelePresenceForSitesBlock(self, *args):
        """
        Returns sequence of true/false values indicating whether taxon at sites
        (in given blocks, 64 sites per block including start block but excluding
        end block) for given parent matches a specific allele (based on frequency).
        Allele number of value 0 would be the major allele. Allele number of value 1
        would be the minor allele. Allele number of value 2 would be the third most
        frequent allele value and so on.

        Signatures:

        long[] haplotypeAllelePresenceForSitesBlock(int taxon, boolean firstParent,
              WHICH_ALLELE allele, int startBlock, int endBlock)
        
        Arguments:

        taxon -- taxon (int)
        firstParent -- true for first parent (false for second parent)
        allele -- allele (WHICH_ALLELE)
        startBlock -- starting block (int)
        endBlock -- ending block (int)
        """
        pass
    ## Returns a string representation of diploid values returned by genotype()
    # for given taxon and site. The two allele values will be separated by colon (:)
    # delimiter
    # @param taxon taxon (int)
    # @param site site (int)
    # @return string representation of diploid values
    @javaOverload("genotypeAsString",
                  (make_sig(['int','int'],java_imports['String']),(metaInteger,metaInteger),None),
                  (make_sig(['int','byte'],java_imports['String']),(metaInteger,metaByte),None))
    def genotypeAsString(self, *args):
        """
        Returns string representation of diploid values returned by genotype()
        for given taxon and site. The two allele values will be separated by a
        colon (:) delimiter.

        Signatures:

        String genotypeAsString(int taxon, int site)
        String genotypeAsString(int site, byte value)
        
        Arguments:

        String genotypeAsString(int taxon, int site)
           taxon -- taxon (int)
           site -- site (int)
        String genotypeAsString(int site, byte value)
           site -- site
           value -- allele value

        Returns:

        string representation of diploid values
        """
        pass
    ## Returns string representation of diploid alleles for given taxon
    # in specified range (end site excluded). Each value in string is what would
    # be returned by genotypeAsString()
    # @param taxon taxon (int)
    # @param startSite start site (int)
    # @param endSite end site (int)
    # @return string representation of alleles in range
    @javaOverload("genotypeAsStringRange",
                  (make_sig(['int','int','int'],java_imports['String']),(metaInteger,metaInteger,
                                                                         metaInteger),None))
    def genotypeAsStringRange(self, *args):
        """
        Returns string representation of diploid alleles for given taxon
        in specified range (end site excluded). Each value in string is what would
        be retuned by genotypeAsString()

        Signatures:

        String genotypeAsStringRange(int taxon, int startSite, int endSite)
        
        Arguments:

        taxon -- taxon (int)
        startSite -- start site (int)
        endSite -- end site (int)

        Returns:

        string representation of alleles in range
        """
        pass
    ## Returns string representation of diploid alleles for given taxon for all
    # sites. Each value in string is what would be returned by genotypeAsString()
    # @param taxon taxon (int)
    # @return string representation of alleles
    @javaOverload("genotypeAsStringRow",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def genotypeAsStringRow(self, *args):
        """
        Returns string representation of diploid alleles for given taxon for all
        sites. Each value in string is what would be returned by genotypeAsString()

        Signatures:

        String genotypeAsStringRow(int taxon)
        
        Arguments:

        taxon -- taxon (int)

        Returns:

        string representaiton of alleles
        """
        pass
    ## Returns string representation of diploid values returned by genotypeArray() for
    # given taxon and site. Same two allele values as genotypeAsString(), except
    # already separated into two Strings.
    # @param taxon taxon (int)
    # @param site site (int)
    # @return string representations of diploid values
    @javaOverload("genotypeAsStringArray",
                  (make_sig(['int','int'],java_imports['String']+'[]'),(metaInteger,metaInteger),
                   lambda x: String.wrap_existing_array(x)))
    def genotypeAsStringArray(self, *args):
        """
        Returns string representation of diploid values returned by genotypeArray() for
        given taxon and site. Same two allele values as genotypeAsString(), except
        already separated by two Strings.

        Signatures:

        String[] genotypeAsStringArray(int taxon, int site)
        
        Arguments:

        taxon -- taxon (int)
        site -- site (int)

        Returns:

        string representation of diploid values
        """
        pass
    ## Return reference diploid allele values at given site
    # @param site site
    # @return First 4 bits are the first allele value and the second 4 bits
    # are the second allele value
    @javaOverload("referenceAllele",
                  (make_sig(['int'],'byte'),(metaInteger,),np.int8))
    def referenceAllele(self, *args):
        """
        Returns reference diploid allele values at given site.

        Signatures:

        byte referenceAllele(int site)

        Arguments:

        site -- site

        Returns:

        First 4 bits are the first allele value and the second 4 bits are the second allele
        value.
        """
        pass
    ## Returns reference sequence of diploid allele values for given taxon in specified range
    # (end site not included). Each value in array contains both diploid values. First 4 bits
    # holds the first allele, and the second 4 bits holds the second allele
    # @param startSite start site
    # @param endSite end site
    @javaOverload("referenceAlleles",
                  (make_sig(['int','int'],'byte[]'),(metaInteger,metaInteger),None))
    def referenceAlleles(self, *args):
        """
        Returns reference sequence of diploid allele values for given taxon in specified
        range (end site not included). Each value in array contains both diploid values. First 4
        bits holds the first allele, and the second 4 bits holds the second allele

        Signatures:

        byte[] referenceAlleles(int startSite, int endSite)

        Arguments:

        startSite -- start site
        endSite -- end site

        Returns:

        Reference sequence of diploid allele values
        """
        pass
    ## Returns reference sequence of diploid allele values. Each value
    # in array contains both diploid values. First 4 bits holds the first allele
    # and second 4 bits holds the second allele
    # @return Reference sequence of diploid allele values
    @javaOverload("referenceAlleleForAllSites",
                  (make_sig([],'byte[]'),(),None))
    def referenceAlleleForAllSites(self, *args):
        """
        Returns reference sequence of diploid allele values. Each value
        in array contains both diploid values. First 4 bits holds the first allele,
        and the second 4 bits holds the second allele
        
        Signatures:

        byte[] referenceAlleleForAllSites()

        Returns:

        Reference sequence of diploid allele values
        """
        pass
    ## Returns whether this genotype table has defined reference sequence
    # @return True if this genotype table has reference sequence
    @javaOverload("hasReference",
                  (make_sig([],'boolean'),(),None))
    def hasReference(self, *args):
        """
        Returns whether this genotype table has defined reference sequence.

        Signatures:

        boolean hasReference()

        Returns:

        True if this genotype table has reference sequence
        """
        pass
    ## Returns whether allele values at given taxon and site are heterozygous
    # @param taxon taxon
    # @param site site
    @javaOverload("isHeterozygous",
                  (make_sig(['int','int'],'boolean'),(metaInteger,metaInteger),None))
    def isHeterozygous(self, *args):
        """
        Returns whether allele values at given taxon and site are heterozygous.

        Signatures:

        boolean isHeterozygous(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site
        
        Returns:

        Whether heterozygous
        """
        pass
    ## Returns number of heterozygous taxa at given site
    # @param site site
    # @return Number of heterozygous taxa
    @javaOverload("heterozygousCount",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def heterozygousCount(self,*args):
        """
        Returns number of heterozygous taxa at given site
        
        Signatures:

        int heterozygousCount(int site)

        Arguments:

        site -- site

        Returns:

        Number of heterozygous taxa
        """
        pass
    ## Get SNP ID for specified site
    # @param site site
    # @return Site name
    @javaOverload("siteName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def siteName(self, *args):
        """
        Get SNP ID for specified site

        Signature:

        String siteName(int site)

        Arguments:

        site -- site

        Returns:

        Site name
        """
        pass
    ## Returns total number of sites in this genotype table
    # @return number of sites
    @javaOverload("numberOfSites",
                  (make_sig([],'int'),(),None))
    def numberOfSites(self, *args):
        """
        Returns total number of sites of this genotype table

        Signatures:

        int numberOfSites()

        Returns:

        Number of sites
        """
        pass
    ## Return number of sites for given chromosome
    # @param chromosome chromosome
    # @return Number of sites
    @javaOverload("chromosomeSiteCount",
                  (make_sig([java_imports['Chromosome']],'int'),(Chromosome,),None))
    def chromosomeSiteCount(self, *args):
        """
        Return number of sites for given chromosome

        Signatures:

        int chromosomeSiteCount(Chromosome chromosome)

        Arguments:

        chromosome -- chromosome
        
        Returns:

        Number of sites
        """
        pass
    ## Get the first (inclusive) and last (exclusive) site of the specified
    # chromosome in this genotype table
    # @param chromosome chromosome
    # @return first and last site
    @javaOverload("firstLastSiteOfChromosome",
                  (make_sig([java_imports['Chromosome']],'int[]'),(Chromosome,),
                   lambda x: javaPrimativeArray.make_array_from_obj('int',x)))
    def firstLastSiteOfChromosome(self, *args):
        """
        Get the first (inclusive) and last (exclusive) site of the specified
        chromosome in this genotype table

        Signatures:

        int[] firstLastSiteOfChromosome(Chromosome chromosome)

        Arguments:

        chromosome -- chromosome

        Returns:

        first and last site
        """
        pass
    ## Returns the number of taxa
    # @return Number of taxa
    @javaOverload("numberOfTaxa",
                  (make_sig([],'int'),(),None))
    def numberOfTaxa(self, *args):
        """
        Returns the number of taxa
        
        Signatures:

        int numberOfTaxa()

        Returns:

        Number of taxa
        """
        pass
    ## Return the position list for the genotype table
    # @return PositionList for all sites
    @javaOverload("positions",
                  (make_sig([],java_imports['PositionList']),(),
                   lambda x: PositionList(obj=x)))
    def positions(self, *args):
        """
        Return the position list for the gneotype table

        Signatures:

        PositionList positions()

        Returns:

        PositionList for all sites
        """
        pass
    ## Returns the physical position at given site
    # @param site site
    # @return physical position
    @javaOverload("chromosomalPosition",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def chromosomalPosition(self, *args):
        """
        Returns the physical position at given site
        
        Signatures:
        
        int chromosomalPosition(int site)

        Arguments:

        site -- site

        Returns:

        physical position
        """
        pass
    ## Returns sites of given physical position/SNP ID in chromosome. If the physical
    # position doesn't exist (-(insertion point) -1) is returned. If chromosome is not found,
    # an exception is thrown. This can support multiple sites with the same physical position
    # but different SNP IDs
    # @param physicalPosition physical position
    # @param chromosome chromsoome. If null, the first chromosome is used
    # @param snpName SNP ID
    # @return index
    @javaOverload("siteOfPhysicalPosition",
                  (make_sig(['int',java_imports['Chromosome']],'int'),(metaInteger,Chromosome),None),
                  (make_sig(['int',java_imports['Chromosome'],java_imports['String']],'int'),
                   (metaInteger,Chromosome,str),None))
    def siteOfPhysicalPosition(self, *args):
        """
        Returns sites of given physical position/SNP ID in chromosome. If the
        physical position doesn't exist, (-(insertion point) -1) is returned. If chromosome
        is not found, an exception is thrown. This can support multiple sites with the same
        physical position but different SNP IDs

        Signatures:

        int siteOfPhysicalPosition(int physicalPosition, Chromosome chromosome)
        int siteOfPhysicalPosition(int physicalPosition, Chromosome chromosome, String snpName)

        Arguments:

        physicalPosition -- physical position
        chromosome -- chromosome. If null, the first chromosome is used
        snpName -- SNP ID

        Returns:

        Index
        """
        pass
    ## Returns all physical positions.
    # @return physical positions
    @javaOverload("physicalPositions",
                  (make_sig([],'int[]'),(),
                   lambda x: javabridge.get_env().get_int_array_elements(x)))
    def physicalPositions(self, *args):
        """
        Returns all physical positions

        Signatures:

        int[] physicalPositions()

        Returns:

        physical positions
        """
        pass
    ## Return chromosome name for given site
    # @param site site
    # @return Chromosome name
    @javaOverload("chromosomeName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def chromosomeName(self, *args):
        """
        Return chromosome name for given site

        Signatures:

        String chromosomeName(int site)

        Arguments:

        site -- site
        
        Returns:

        Chromosome name
        """
        pass
    ## Returns chromosome for given site or with matching name
    # @param site site
    # @param name name
    # @return Chromosome
    @javaOverload("chromosome",
                  (make_sig(['int'],java_imports['Chromosome']),(metaInteger,),lambda x:Chromosome(obj=x)),
                  (make_sig([java_imports['String']],java_imports['Chromosome']),(str,),
                   lambda x: Chromosome(obj=x)))
    def chromosome(self, *args):
        """
        Returns Chromosome for given site or with matching name
        (first to match will be returned)

        Signatures:

        Chromosome chromosome(int site)
        Chromosome chromosome(String name)

        Arguments:

        Chromosome chromosome(int site):
           site -- site
        Chromosome chromosome(String name):
           name -- name

        Returns:

        Chromosome
        """
        pass
    ## Return all chromosomes
    # @return chromosomes
    @javaOverload("chromosomes",
                  (make_sig([],java_imports['Chromosome']+'[]'),(),
                   lambda x: Chromosome.wrap_existing_array(x)))
    def chromosomes(self, *args):
        """
        Return all chromosomes

        Signatures:

        Chromosome[] chromosomes()

        Returns:

        chromosomes
        """
        pass
    ## Returns number of chromosomes
    # @return Number of chromosomes
    @javaOverload("numChromosomes",
                  (make_sig([],'int'),(),None))
    def numChromosomes(self, *args):
        """
        Return number of chromosomes

        Signatures:

        int numChromosomes()

        Returns:

        Number of chromosomes
        """
        pass
    ## Returns starting site for each chromosome
    # @return starting site for each chromosome
    @javaOverload("chromosomesOffsets",
                  (make_sig([],'int[]'),(),
                   lambda x: javaPrimativeArray.make_array_from_obj('int',x)))
    def chromosomesOffsets(self, *args):
        """
        Returns starting site for each chromosome

        Signatures:

        int[] chromosomesOffsets()

        Returns:

        Starting site for each chromosome
        """
        pass
    ## Returns the site score of the given taxon and site
    # @param taxon taxon index
    # @param site site
    # @return site score
    @javaOverload("siteScore",
                  (make_sig(['int','int'],'float'),(metaInteger,metaInteger),None))
    def siteScore(self, *args):
        """
        Returns the site score of the given taxon and site

        Signatures:

        float siteScore(int taxon, int site)

        Arguments:

        taxon -- taxon index
        site -- site

        Returns:

        site score
        """
        pass
    ## Returns the site scores
    # @return site scores
    @javaOverload("siteScores",
                  (make_sig([],'float[][]'),(),
                   lambda x: javaPrimativeArray.get_array_type('float').wrap_existing_array(x)))
    def siteScores(self, *args):
        """
        Returns the site scores

        Signatures:

        float[][] siteScores()
        
        Returns:

        site scores
        """
        pass
    ## Returns true if this genotype table has sequencing depth
    # @return True if this genotype table has sequencing depth
    @javaOverload("hasDepth",
                  (make_sig([],'boolean'),(),None))
    def hasDepth(self, *args):
        """
        Returns true if this genotype table has sequencing depth

        Signatures:

        boolean hasDepth()

        Returns:

        True if this genotype table has sequencing depth
        """
        pass
    ## Returns true if this genotype table has site scores
    # @return True if this genotype table has site scores
    @javaOverload("hasSiteScores",
                  (make_sig([],'boolean'),(),None))
    def hasSiteScores(self, *args):
        """
        Returns true if this genotype table has site scores
        
        Signatures:

        boolean hasSiteScores()

        Returns:

        True if this genotype table has site scores
        """
        pass
    ## Return what type of site scores this genotype table has
    # @return Site score type
    @javaOverload("siteScoreType",
                  (make_sig([],java_imports['GenotypeTable']+'$SITE_SCORE_TYPE'),
                   (),lambda x: Enum(obj=x)))
    def siteScoreType(self, *args):
        """
        Return what type of site scores this genotype table has

        Signatures:

        GenotypeTable.SITE_SCORE_TYPE siteScoreType()
        
        Returns:

        Site score type
        """
        pass
    ## Returns size of indel at given site
    # @param site site
    # @return indel size
    @javaOverload("indelSize",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def indelSize(self, *args):
        """
        Returns size of indel at given site.

        Signatures:

        int indelSize(int site)

        Arguments:

        site -- site

        Returns:

        indel size
        """
        pass
    ## Returns whether given site is an indel
    # @param site site
    # @return true if indel
    @javaOverload("isIndel",
                  (make_sig(['int'],'boolean'),(metaInteger,),None))
    def isIndel(self, *args):
        """
        Returns whether given site is an indel

        Signatures:

        boolean isIndel(int site)

        Arguments:

        site -- site

        Returns:

        true if indel
        """
        pass
    ## Returns whether all sites are polymorphic
    # @return true if all sites polymorphic
    @javaOverload("isAllPolymorphic",
                  (make_sig([],'boolean'),(),None))
    def isAllPolymorphic(self, *args):
        """
        Returns whether all sites are polymorphic

        Signatures:

        boolean isAllPolymorphic()

        Returns:

        true if all sites are polymorphic
        """
        pass
    ## Returns whether given site is polymorphic
    # @param site site
    # @return true if given site is polymorphic
    @javaOverload("isPolymorphic",
                  (make_sig(['int'],'boolean'),(metaInteger,),None))
    def isPolymorphic(self, *args):
        """
        Returns whether given site is polymorphic

        Signatures:

        boolean isPolymorphic(int site)

        Arguments:

        site -- site

        Returns:

        true if given site is polymorphic
        """
        pass
    ## Returns most common allele at given site. Gap is included as state.
    # Heterozygous count one for each allele value. Homozygous counts two for
    # the allele value
    # @param site site
    # @return most common allele
    @javaOverload("majorAllele",
                  (make_sig(['int'],'byte'),(metaInteger,),np.int8))
    def majorAllele(self, *args):
        """
        Returns most common allele at given site. Gap is included as state.
        Heterozygous count one for each allele value. Homozygous counts two for
        the allele value

        Signatures:

        byte majorAllele(int site)

        Arguments:

        site -- site

        Returns:

        most common allele
        """
        pass
    ## Returns most common allele at given site. Gap is included as state.
    # Heterozygous count one for each allele value. Homozygous counts two for
    # the allele value
    # @param site site
    # @return most common allele as String
    @javaOverload("majorAlleleAsString",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def majorAlleleAsString(self, *args):
        """
        Returns most common allele at given site. Gap is included as state.
        Heterozygous count one for each allele value. Homozygous counts two for
        allele value

        Signatures:

        String majorAlleleAsString(int site)

        Arguments:

        site -- site

        Returns:

        most common allele as String
        """
        pass
    ## Returns most common minor allele at given site. Gap is included as state.
    # Heterozygous count one for each allele value. Homozygous counts two for
    # the allele value
    # @param site site
    # @return most common minor allele
    @javaOverload("minorAllele",
                  (make_sig(['int'],'byte'),(metaInteger,),np.int8))
    def minorAllele(self, *args):
        """
        Returns most common minor allele at given site. Gap is included as state.
        Heterozygous count one for each allele value. Homozygous counts two for
        the allele value

        Signatures:

        byte minorAllele(int site)

        Arguments:

        site -- site

        Returns:

        most common minor allele
        """
        pass
    ## Returns most common minor allele at given site. Gap is included as state.
    # Heterozygous count one for each allele value. Homozygous counts two for
    # the allele value
    # @param site site
    # @return most common minor allele as String
    @javaOverload("minorAlleleAsString",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def minorAlleleAsString(self, *args):
        """
        Returns most common minor allele at given site. Gap is included as state.
        Heterozygous count one for each allele value. Homozygous counts two for
        allele value

        Signatures:

        String minorAlleleAsString(int site)

        Arguments:

        site -- site

        Returns:

        most common minor allele as String
        """
        pass
    ## Returns all minor alleles at given site. Gap is included as state.
    # Heterozygous count one for each allele value. Homozygous counts two
    # for the allele value
    # @param site site
    # @return All minor alleles
    @javaOverload("minorAlleles",
                  (make_sig(['int'],'byte[]'),(metaInteger,),None))
    def minorAlleles(self, *args):
        """
        Returns all minor alleles at given site. Gap is included as state
        Heterozygous count one for each allele value. Homozygous counts two
        for the allele value

        Signatures:

        byte[] minorAlleles(int site)

        Arguments:

        site -- site

        Returns: All minor alleles
        """
        pass
    ## Returns all alleles at given site in order of frequency. Gap
    # is included as state. Heterozygous count one for each allele value.
    # Homozygous counts two for the allele value
    # @param site site
    # @return All alleles
    @javaOverload("alleles",
                  (make_sig(['int'],'byte[]'),(metaInteger,),None))
    def alleles(self, *args):
        """
        Returns all alleles at given site in order of frequency. Gap
        is included as state. Heterozygous count one for each allele value.
        Homozygous counts two for the allele value

        Signatures:

        byte[] alleles(int site)

        Arguments:

        site -- site

        Returns:

        All alleles
        """
        pass
    ## Returns frequency for most common minor allele at given site.
    # Gap is included as state. Heterozygous count one for each allele value.
    # Homozygous counts two for the allele value
    # @param site site
    # @return frequency
    @javaOverload("minorAlleleFrequency",
                  (make_sig(['int'],'double'),(metaInteger,),np.float64))
    def minorAlleleFrequency(self, *args):
        """
        Returns frequency for most common minor allele at given site.
        Gap is included as state. Heterozygous count one for each allele value.
        Homozygous counts two for the allele value

        Signatures:

        double minorAlleleFrequency(int site)

        Arguments:

        site -- site

        Returns:

        frequency
        """
        pass
    ## Returns frequency for major allele at given site. Gap is included as state
    # Heterozygous count one for each allele value. Homozygous counts two for the
    # allele value
    # @param site site
    # @return frequency
    @javaOverload("majorAlleleFrequency",
                  (make_sig(['int'],'double'),(metaInteger,),np.float64))
    def majorAlleleFrequency(self, *args):
        """
        Returns frequency for major allele at given site. Gap is included as
        state. Heterozygous count one for each allele value. Homozygous counts
        two for the allele value

        Signatures:

        double majorAlleleFrequency(int site)

        Arguments:

        site -- site

        Returns:

        frequency
        """
        pass
    ## Returns taxa list of this genotype table
    # @return taxa list
    @javaOverload("taxa",
                  (make_sig([],java_imports['TaxaList']),(),
                   lambda x: TaxaList(obj=x)))
    def taxa(self, *args):
        """
        Return taxa list of this genotype table

        Signatures:

        TaxaList taxa()

        Returns:

        taxa list
        """
        pass
    ## Returns taxa name at given index
    # @param index index
    # @return taxa name
    @javaOverload("taxaName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def taxaName(self, *args):
        """
        Returns taxa name at given index

        Signatures:

        String taxaName(int index)

        Arguments:

        index -- index

        Returns:

        taxa name
        """
        pass
    ## Gets the genome assembly
    # @return the genome assembly
    @javaOverload("genomeVersion",
                  (make_sig([],java_imports['String']),(),None))
    def genomeVersion(self, *args):
        """
        Gets the Genome Assembly

        Signatures:

        String genomeVersion()

        Returns:

        The genome assembly
        """
        pass
    ## Returns whether is positive strand at given site
    # @return whether is positive strand
    @javaOverload("isPositiveStrand",
                  (make_sig(['int'],'boolean'),(metaInteger,),None))
    def isPositiveStrand(self, *args):
        """
        Returns whether is positive strand at given site

        Signatures:

        boolean isPositiveStrand(int site)

        Arguments:

        site -- site
        
        Returns:

        whether is positive strand
        """
        pass
    ## Returns individual genotype tables within this genotype table
    # @return list of genotype tables
    @javaOverload("compositeAlignments",
                  (make_sig([],java_imports['GenotypeTable']+'[]'),(),
                   lambda x: GenotypeTable.wrap_existing_array(x)))
    def compositeAlignments(self, *args):
        """
        Returns individual genotype tables within this genotype table
    
        Signatures:
    
        GenotypeTable[] compositeAlignments()
    
        Returns:
    
        list of genotype tables
        """
        pass
    ## Returns sorted list of allels from highest frequency to lowest
    # at given site in genotype table. Resulting double dimension array
    # holds alleles (bytes) in result[0]. And the counts are in result[1].
    # Counts haploid values twice and diploid values once. Higher ploids
    # are not supported
    # @param site site
    # @return sorted list of alleles and counts
    @javaOverload("allelesSortedByFrequency",
                  (make_sig(['int'],'int[][]'),(metaInteger,),
                   lambda x: javaPrimativeArray.get_array_type('int').wrap_existing_array(x)))
    def allelesSortedByFrequency(self, *args):
        """
        Return sorted list of alleles from highest frequency to lowest
        at given site in genotype table. Resulting double dimension array
        holds alleles (bytes) in result[0]. And the counts are in result[1].
        Counts haploid values twice and diploid values once. Higher ploids
        are not supported

        Signatures:

        int[][] allelesSortedByFrequency(int site)

        Arguments:

        site -- site

        Returns:

        sorted list of alleles and counts
        """
        pass
    ## Returns sorted list of diploid values from highest frequency to
    # lowest at given site in genotype table. Resulting double dimension array
    # holds diploids (Strings) in result[0]. And the counts are in result[1]
    # (Integers)
    # @param site site
    # @return Sorted list of diploids and counts
    @javaOverload("genosSortedByFrequency",
                  (make_sig(['int'],java_imports['Object']+'[][]'),(metaInteger,),
                   lambda x: [np.array(map(lambda y: javabridge.call(y,"toString","()Ljava/lang/String;"),
                                  javabridge.get_env().get_object_array_elements(\
                            javabridge.get_env().get_object_array_elements(x)[0]))),
                            np.array(map(lambda y: javabridge.call(y,"intValue","()I"),
                                javabridge.get_env().get_object_array_elements(\
                                javabridge.get_env().get_object_array_elements(x)[1])))]))
    def genosSortedByFrequency(self, *args):
        """
        Returns sorted list of diploid values from highest frequency to
        lowest at given site in genotype table. Resulting double dimension array
        holds diploids (Strings) in result[0]. And the counts are in result[1]
        (Integers).

        Signatures:

        Object[][] genosSortedByFrequency(int site)

        Arguments:

        site -- site

        Returns:

        Sorted list of diploids and counts
        """
        pass
    ## Returns whether this genotype table is phased
    # @return true if phased
    @javaOverload("isPhased",
                  (make_sig([],'boolean'),(),None))
    def isPhased(self, *args):
        """
        Returns whether this genotype table is phased

        Signatures:

        boolean isPhased()

        Returns:

        true if phased
        """
        pass
    ## Returns true if this genotype table retains rare alleles. If false, rare
    # alleles are recorded as unknown
    # @return whether rare alleles are retained
    @javaOverload("retainsRareAlleles",
                  (make_sig([],'boolean'),(),None))
    def retainsRareAlleles(self, *args):
        """
        Returns true if this genotype table retains rare alleles.
        If false, rare alleles are recorded as unknown

        Signatures:

        boolean retainsRareAlleles()

        Returns:

        Whether rare alleles are retained
        """
        pass
    ## Returns allele values as strings for all sites (first signature) or for
    # a specific site (second signature)
    # @param site site
    # @return Eiether the allele values for all sites or for a given site
    @javaOverload("alleleDefinitions",
            (make_sig([],java_imports['String']+'[][]'),(), # First signature
        lambda x: javaArray.get_array_type(String).wrap_existing_array(x)),
            (make_sig(['int'],java_imports['String']+'[]'),(metaInteger,),
        lambda x: String.wrap_existing_array(x)))
    def alleleDefinitions(self, *args):
        """
        For the first signature:
           Returns allele values as strings for all sites. The first dimension
           of this array indexes the sites. The second dimension indexes the allele
           values for the given site. The indices for the allele values are used as
           the codes to store data. These codes (indices) are returned by the genotype()
           methods. If only one array of allele values is returned, that is the
           encoding for all sites
        For the second signature:
           Same as alleleDefinitions() for only one site

        Signatures:

        String[][] alleleDefinitions()
        String[] alleleDefinitions(int site)

        Arguments:

        String[] alleleDefinitions(int site)
           site -- site

        Returns:

        String[][] alleleDefinitions()
           allele values for all sites
        String[] alleleDefinitions(int site)
           allele values for given site
        """
        pass
    ## Returns String representation of diploid allele value at site
    # @param site site
    # @param value diploid allele value (byte)
    # @return String representation
    @javaOverload("diploidAsString",
                  (make_sig(['int','byte'],java_imports['String']),(metaInteger,metaByte),
                   None))
    def diploidAsString(self, *args):
        """
        Returns String representation of diploid allele value at site.

        Signatures:

        String diploidAsString(int site, byte value)

        Arguments:

        site -- site
        value -- diploid allele value

        Returns:

        String representation
        """
        pass
    ## Returns max number of alleles defined for any given site
    # @return max number of alleles
    @javaOverload("maxNumAlleles",
                  (make_sig([],'int'),(),None))
    def maxNumAlleles(self, *args):
        """
        Returns max number of alleles defined for any given site

        Signatures:

        int maxNumAlleles()
        
        Returns:

        max number of alleles
        """
        pass
    ## Returns total number of non-missing allele values for given site. This can
    # be twice the number of taxa, as diploid values are supported
    # @param site site
    # @return Number of non-missing allele values
    @javaOverload("totalGametesNonMissingForSite",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def totalGametesNonMissingForSite(self, *args):
        """
        Returns total number of non-missing allele values for given site. This can
        be twice the number of taxa, as diploid values are supported

        Signatures:

        int totalGametesNonMissingForSite(int site)

        Arguments:

        site -- site

        Returns:

        Number of non-missing allele values
        """
        pass
    @javaOverload("totalNonMissingForSite",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def totalNonMissingForSite(self, *args):
        """
        Returns total number of non-missing taxa for given site. Taxa are
        considered missing only if both allele values are Unknown (N).

        Signatures:

        int totalNonMissingForSite(int site)

        Arguments:

        site -- site
        
        Returns:

        Number of non-missing taxa
        """
        pass
    ## Returns the minor allele count for given site
    # @param site site
    # @return minor allele count
    @javaOverload("minorAlleleCount",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def minorAlleleCount(self, *args):
        """
        Returns the minor allele count for given site

        Signatures:

        int minorAlleleCount(int site)

        Arguments:

        site -- site

        Returns:

        minor allele count
        """
        pass
    ## Returns the major allele count for given site
    # @param site site
    # @return major allele count
    @javaOverload("majorAlleleCount",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def majorAlleleCount(self, *args):
        """
        Returns the major allele count for given site

        Signatures:

        int majorAlleleCount(int site)

        Arguments:

        site -- site

        Returns:

        major allele count
        """
        pass
    ## Returns counts of all diploid combinations from highest frequency
    # to lowest for whole genotype table. Resulting double dimension array
    # holds diploids (Strings) in result[0]. And the counts are in result[1] (Longs)
    @javaOverload("genoCounts",
                  (make_sig([],java_imports['Object']+'[][]'),(),
                lambda x: [np.array(map(lambda y: String(obj=y).toString(),
                      javabridge.get_env().get_object_array_elements(\
                javabridge.get_env().get_object_array_elements(x)[0]))),
                np.array(map(lambda y: Long(obj=y).longValue(),
                javabridge.get_env().get_object_array_elements(\
                javabridge.get_env().get_object_array_elements(x)[1])))]))
    def genoCounts(self, *args):
        """
        Returns counts of all diploid combinations from highest frequency
        to lowest for whole genotype table. Resulting double dimension array
        holds diploids (Strings) in result[0]. And the counts are in result[1] (Longs)

        Signatures:

        Object[][] genoCounts()

        Returns:

        diploid counts
        """
        pass
    ## Returns counts of all major/minor allele combinations from highest
    # frequency to lowest for whole genotype table. Resulting double dimension
    # array holds major/minor allele (Strings) in result[0]. And the counts are
    # in result[1] (Longs)
    # @return diploid counts
    @javaOverload("majorMinorCounts",
                  (make_sig([],java_imports['Object']+'[][]'),(),
                lambda x: [np.array(map(lambda y: String(obj=y).toString(),
                      javabridge.get_env().get_object_array_elements(\
                javabridge.get_env().get_object_array_elements(x)[0]))),
                np.array(map(lambda y: Long(obj=y).longValue(),
                javabridge.get_env().get_object_array_elements(\
                javabridge.get_env().get_object_array_elements(x)[1])))]))
    def majorMinorCounts(self, *args):
        """
        Returns counts of all major/minor allele combinations from highest
        frequency to lowest for whole genotype table. Resulting double dimension
        array holds major/minor allele (Strings) in result[0]. And the counts are
        in result[1] (Longs)

        Signatures:

        Object[][] majorMinorCounts()

        Returns:

        diploid counts
        """
        pass
    ## Retursn total number of non-missing allele values for given taxon. This
    # can be twice the number of sites, as diploid values are supported
    # @param taxon taxon
    # @return Number of non-missing allele values
    @javaOverload("totalGametesNonMissingForTaxon",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def totalGametesNonMissingForTaxon(self, *args):
        """
        Returns total number of non-missing allele values for given taxon. This
        can be twice the number of sites, as diploid values are supported

        Signatures:

        int totalGametesNonMissingForTaxon(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        Number of non-missing allele values
        """
        pass
    ## Returns number of heterozygous sites at given taxon
    # @param taxon taxon
    # @return number of heterozygous sites
    @javaOverload("heterozygousCountForTaxon",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def heterozygousCountForTaxon(self, *args):
        """
        Returns number of heterozygous sites at given taxon

        Signatures:

        int heterozygousCountForTaxon(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        number of heterozygous sites
        """
        pass
    ## Returns total number of non-missing sites for given taxon. Sites
    # are considered missing only if both allele values are Unknown (N).
    # @param taxon taxon
    # @return number of non-missing sites
    @javaOverload("totalNonMissingForTaxon",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def totalNonMissingForTaxon(self, *args):
        """
        Returns total number of non-missing sites for given taxon. Sites
        are considered missing only if both allele values are Unknown (N).

        Signatures:

        int totalNonMissingForTaxon(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        number of non-missing sites
        """
        pass
    ## Returns allele depth object (null if not present)
    # @return allele depth associated with genotypeTable
    @javaOverload("depth",
                  (make_sig([],java_imports['AlleleDepth']),(),
                   lambda x: AlleleDepth(obj=x) if x is not None else x))
    def depth(self, *args):
        """
        Returns allele depth object (null if not present)

        Signatures:

        AlleleDepth depth()

        Returns:

        allele depth associated with genotypeTable
        """
        pass
    ## Returns depth count for each diploid allele at the given taxon and site
    # @param taxon taxon
    # @param site site
    # @return two counts
    @javaOverload("depthForAlleles",
                  (make_sig(['int','int'],'int[]'),(metaInteger,metaInteger),
                   lambda x: primativeArray.make_object_array('int',x)))
    def depthForAlleles(self, *args):
        """
        Returns depth count for each diploid allele at the given taxon and site

        Signatures:

        int[] depthForAlleles(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        two counts
        """
        pass
    ## Returns all alleles at given site in order defined by scope
    # @param scope scope
    # @param site site
    # @return alleles
    @javaOverload("allelesBySortType",
                  (make_sig([java_imports['GenotypeTable']+'$ALLELE_SORT_TYPE','int'],
                            'byte[]'),(ALLELE_SORT_TYPE.subclass,metaInteger),None))
    def allelesBySortType(self, *args):
        """
        Returns all alleles at given site in order defined by scope

        Signatures:

        byte[] allelesBySortType(GenotypeTable.ALLELE_SORT_TYPE scope, int site)

        Arguments:

        scope -- scope
        site -- site

        Returns:

        alleles
        """
        pass
    ## Returns sequence of true/false values indicating whether site at each
    # taxon matches a specific allele
    # @param site site
    # @param allele allele
    # @return sequence of true/false values
    @javaOverload("allelePresenceForAllTaxa",
                  (make_sig(['int',java_imports['WHICH_ALLELE']],
                            java_imports['BitSet']),(metaInteger,WHICH_ALLELE.subclass),
                            lambda x: OpenBitSet(obj=x)))
    def allelePresenceForAllTaxa(self, *args):
        """
        Returns sequence of true/false values indicating whether site at
        each taxon matches a specific allele

        Signatures:

        BitSet allelePresenceForAllTaxa(int site, WHICH_ALLELE allele)

        Arguments:

        site -- site
        allele -- allele

        Returns:

        sequence of true/false values
        """
        pass
    ## Returns BitStorage for this Genotype
    # @param allele allele
    # @return BitStorage
    @javaOverload("bitStorage",
                  (make_sig([java_imports['WHICH_ALLELE']],
                            java_imports['BitStorage']),(WHICH_ALLELE.subclass,),None))
    def bitStorage(self, *args):
        """
        Returns BitStorage for this Genotype

        Signatures:

        BitStorage bitStorage(GenotypeTable.WHICH_ALLELE allele)

        Arguments:
        
        allele -- allele

        Returns:

        BitStorage
        """
        pass
