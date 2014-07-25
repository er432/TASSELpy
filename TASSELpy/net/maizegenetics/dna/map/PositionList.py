from TASSELpy.java.util.FilterList import FilterList
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Byte import Byte
from TASSELpy.net.maizegenetics.dna.map.Position import Position
from TASSELpy.net.maizegenetics.dna.map.Chromosome import Chromosome
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
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
                'TaxaList':'net/maizegenetics/taxa/TaxaList'}

## List of positions in the genome
class PositionList(FilterList):
    """
    List of Positions in the genome. This type is used by every GenotypeTable,
    but it can also be used as list of GWAS results and other genomic annotations
    """
    _java_name = java_imports['PositionList']
    @javaConstructorOverload(java_imports['PositionList'])
    def __init__(self, *args, **kwargs):
        super(PositionList,self).__init__(*args,generic=(Position,),**kwargs)
    ## Return the reference diploid allele values at given site
    # @return First 4 bits are the first allele value and second four bits are
    # the second allele value
    @javaOverload("referenceGenotype",
                  (make_sig(['int'],'byte'),(metaInteger,),lambda x: Byte(x)))
    def referenceGenotype(self, *args):
        """
        Return the reference diploid allele values at given site

        Signatures:

        byte referenceGenotype(int site)

        Arguments:

        site -- site

        Returns:

        First 4 bits are the first allele value and second four bits are the
        second allele value
        """
        pass
    ## Returns reference sequence of diploid allele values for given taxon in specified range
    # (end site not included). Each value in array contains both diploid values. First 4 bits
    # holds the first allele, and the second 4 bits holds the second allele
    # @param startSite start site
    # @param endSite end site
    @javaOverload("referenceGenotypes",
                  (make_sig(['int','int'],'byte[]'),(metaInteger, metaInteger),None))
    def referenceGenotypes(self, *args):
        """
        Returns reference sequence of diploid allele values for given taxon in specified
        range (end site not included). Each value in array contains both diploid values. First 4
        bits holds the first allele, and the second 4 bits holds the second allele

        Signatures:

        byte[] referenceGenotypes(int startSite, int endSite)

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
    @javaOverload("referenceGenotypeForAllSites",
                  (make_sig([],'byte[]'),(),None))
    def referenceGenotypeForAllSites(self, *args):
        """
        Returns reference sequence of diploid allele values. Each value
        in array contains both diploid values. First 4 bits holds the first allele,
        and the second 4 bits holds the second allele
        
        Signatures:

        byte[] referenceGenotypeForAllSites()

        Returns:

        Reference sequence of diploid allele values
        """
        pass
    ## Returns whether this alignment has defined reference sequence
    # @return True if this alignment has reference sequence
    @javaOverload("hasReference",
                  (make_sig([],'boolean'),(),None))
    def hasReference(self, *args):
        """
        Returns whether this alignment has defined reference sequence.

        Signatures:

        boolean hasReference()

        Returns:

        True if this alignment has reference sequence
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
    @javaOverload("startAndEndOfChromosome",
                  (make_sig([java_imports['Chromosome']],'int[]'),(Chromosome,),
                   lambda x: javabridge.get_env().get_int_array_elements(x)))
    def startAndEndOfChromosome(self, *args):
        """
        Get the first (inclusive) and last (exclusive) site of the specified
        chromosome in this genotype table

        Signatures:

        int[] startAndEndOfChromosome(Chromosome chromosome)

        Arguments:

        chromosome -- chromosome

        Returns:

        first and last site
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
                   lambda x: map(lambda y: Chromosome(obj=y),
                                 javabridge.get_env().get_object_array_elements(x))))
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
                   lambda x: javabridge.get_env().get_int_array_elements(x)))
    def chromosomesOffsets(self, *args):
        """
        Returns starting site for each chromosome

        Signatures:

        int[] chromosomesOffsets()

        Returns:

        Starting site for each chromosome
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
