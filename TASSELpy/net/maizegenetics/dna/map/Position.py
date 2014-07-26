from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.net.maizegenetics.dna.WHICH_ALLELE import WHICH_ALLELE
from TASSELpy.java.lang.String import String
from TASSELpy.net.maizegenetics.util.GeneralAnnotation import GeneralAnnotation
from TASSELpy.net.maizegenetics.dna.map.Chromosome import Chromosome
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.java.lang.Enum import Enum
from TASSELpy.utils.helper import make_sig
import javabridge
import numpy as np

java_imports={'Chromosome':'net/maizegenetics/dna/map/Chromosome',
              'Position':'net/maizegenetics/dna/map/Position',
              'String':'java/lang/String',
              'WHICH_ALLELE':'net/maizegenetics/dna/WHICH_ALLELE'}

## Defines a genomic position and its known variants. Includes attributes
# of chromosome, position, strand, centiMorgans, name (or SNP ID), whether this
# position is a nucleotide, or includes an indel
class Position(Comparable, GeneralAnnotation):
    """
    Defines a genomic position and its known variants. Includes attributes
    of chromosome, position, strand, centiMorgans, name (or SNP ID), whether this
    position is a nucleotide, or includes an indel
    """
    _java_name = java_imports['Position']
    def __repr__(self):
        return "Position(chrom=%s,bp=%d,cM=%0.5g)" % (self.getChromosome().getName(),
                                                   self.getPosition(),
                                                   self.getCM())
    @javaConstructorOverload(java_imports['Position'])
    def __init__(self, *args, **kwargs):
        super(Position,self).__init__(*args, generic=(Position,), **kwargs)
        pass
    ## Return the locus (generally a chromosome) of a site
    # @return The locus of a site
    @javaOverload("getChromosome",
                  (make_sig([],java_imports['Chromosome']),(),
                  lambda x: Chromosome(obj=x)))
    def getChromosome(self, *args):
        """
        Return the locus (generally a chromosome) of a site

        Signatures:

        Chromosome getChromosome

        Returns:

        The locus of a site
        """
        pass
    ## Return the physical position of a site
    # @preturn the physical position of a site
    @javaOverload("getPosition",
                  (make_sig([],'int'),(),None))
    def getPosition(self, *args):
        """
        Return the physical position of a site

        Signatures:

        int getPosition()

        Returns:

        The physical position of a site
        """
        pass
    ## Return the strand for a site definition
    # @return The strand for a site definition
    @javaOverload("getStrand",
                  (make_sig([],'byte'),(),lambda x: np.int8(x)))
    def getStrand(self, *args):
        """
        Return the strand for a site definition

        Signatures:

        byte getStrand()

        Returns:

        The strand for a site definition
        """
        pass
    ## Return the genetic position for a site definition
    # @return The genetic position for a site definition
    @javaOverload("getCM",
                  (make_sig([],'float'),(),None))
    def getCM(self, *args):
        """
        Return the genetic position for a site definition

        Signatures:

        float getCM()

        Returns:

        The genetic position for a site definition
        """
        pass
    ## Return the ID (name) for a site
    # @return the ID (name) for a site
    @javaOverload("getSNPID",
                  (make_sig([],java_imports['String']),(),None))
    def getSNPID(self, *args):
        """
        Return the ID (name) for a site

        Signatures:

        String getSNPID()

        Returns:

        The ID (name) for a site
        """
        pass
    ## Whether the position is a nucleotide position or another marker type (SSR, AFLP, RAPD,
    # CNV, which are recorded with text states)
    # @return whether the position is a nucleotide position
    @javaOverload("isNucleotide",
                  (make_sig([],'boolean'),(),None))
    def isNucleotide(self, *args):
        """
        Whether the position is a nucleotide position or another marker type (SSR, AFLP, RAPD,
        CNV, which are recorded with text states)

        Signatures:

        boolean isNucleotide()

        Returns:

        Whether the position is a nucleotide position
        """
        pass
    ## Whether the position includes indels, which would be defined in the variants
    # @return Whether the position includes indels
    @javaOverload("isIndel",
                  (make_sig([],'boolean'),(),None))
    def isIndel(self, *args):
        """
        Whether the position includes indels, which would be defined in the variants

        Signatures:

        boolean isIndel()

        Returns:

        Whether the position includes indels
        """
        pass
    ## Returns the nature of the polymorphism ("ACTAT", "-"} or {"A","C","G"} or {"100","103","106"}
    # @return The nature of the polymorphism
    @javaOverload("getKnownVariants",
                  (make_sig([],java_imports['String']+'[]'),(),
                    lambda x: np.array(map(lambda y: String(obj=y).toString(),
                                  javabridge.get_env().get_object_array_elements(x)))))
    def getKnownVariants(self, *args):
        """
        Returns the nature of the polymorphism ("ACTAT", "-"} or {"A","C","G"} or {"100","103","106"}

        Signatures:

        String[] getKnownVariants()

        Returns:

        The nature of the polymorphism
        """
        pass
    ## Return the minor allele frequency in a global scope
    # @return the minor allele frequency in a global scope
    @javaOverload("getGlobalMAF",
                  (make_sig([],'float'),(),None))
    def getGlobalMAF(self, *args):
        """
        Return the minor allele frequency in a global scope

        Signatures:

        float getGlobalMAF()

        Returns:

        the minor allele frequency in a global scope
        """
        pass
    ## Returns the proportion of genotypes scored at a given site
    # @return the proportion of genotypes scored at a given site
    @javaOverload("getGlobalSiteCoverage",
                  (make_sig([],'float'),(),None))
    def getGlobalSiteCoverage(self, *args):
        """
        Returns the proportion of genotypes scored at a given site

        Signatures:

        float getGlobalSiteCoverage()

        Returns:

        The proportion of genotypes scored at a given site
        """
        pass
    ## Returns the allele specified by alleleType, if unkonwn Alignment.Unknown is returned
    # @param alleleType an AlleleType
    # @return The allele specified by alleleType
    @javaOverload("getAllele",
                  (make_sig([java_imports['WHICH_ALLELE']],'byte'),(WHICH_ALLELE.subclass,),
                   lambda x: np.int8(x)))
    def getAllele(self, *args):
        """
        Returns the allele specified by alleleType, if unkonwn Alignment.Unknown is returned

        Signatures:

        byte getAllele(Allele alleleType)

        Arguments:

        alleleType -- An alleleType

        Returns:

        The allele specified by alleleType
        """
        pass
