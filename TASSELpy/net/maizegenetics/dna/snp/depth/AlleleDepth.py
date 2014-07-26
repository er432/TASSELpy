from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
import numpy as np
import javabridge

java_imports={'AlleleDepth':'net/maizegenetics/dna/snp/depth/AlleleDepth'}

## Provides DNA read depth data for a genotype table.
class AlleleDepth(Object):
    """
    Provides DNA read depth data for a genotype data
    """
    @javaConstructorOverload(java_imports['AlleleDepth'])
    def __init__(self, *args, **kwargs):
        pass
    ## Returns depth count for each diploid allele at the given taxon and site
    # @param taxon taxon
    # @param site site
    # @return Array of counts
    @javaOverload("depthForAlleles",
                  (make_sig(['int','int'],'int[]'),(metaInteger,metaInteger),
                   lambda x: javabridge.get_env().get_int_array_elements(x)))
    def depthForAlleles(self, *args):
        """
        Returns depth count for each diploid allele at the given taxon and site
        The array of depths is sizes as determined by NUMBER_NUCLEOTIDE_ALLELES (6)
        and it is ordered as in NUCLEOTIDE_ALLELES (A, C, G, T, +(insertion),
        - (deletion))

        The depths from 0 to 127 are recorded exactly. Depths above 127 are stored as
        approximate logs (equation), and they are represented by negative numbers
        
        Signatures:

        int[] depthForAlleles(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        Array of counts
        """
        pass
    ## Returns depth count for given allele at given taxon and site
    # @param taxon taxon
    # @param site site
    # @param allele allele
    # @return Count
    @javaOverload("depthForAllele",
                  (make_sig(['int','int','int'],'int'),(metaInteger, metaInteger, metaInteger),
                   None))
    def depthForAllele(self, *args):
        """
        Returns depth count for given allele at given taxon and site

        Signatures:

        int depthForAllele(int taxon, int site, int allele)

        Arguments:

        taxon -- taxon
        site -- site
        allele -- allele

        Returns:

        Count
        """
        pass
    ## Returns depth count as byte for given allele at given taxon and site
    # @param taxon taxon
    # @param site site
    # @param allele allele
    # @return Count as byte
    @javaOverload("depthForAlleleByte",
                  (make_sig(['int','int','int'],'byte'),(metaInteger, metaInteger, metaInteger),
                   lambda x: np.int8(x)))
    def depthForAlleleByte(self, *args):
        """
        Returns depth count as byte for given allele at given taxon and site

        Signatures:

        byte depthForAlleleByte(int taxon, int site, int allele)

        Arguments:

        taxon -- taxon
        site -- site
        allele -- allele

        Returns:

        Count as byte
        """
        pass
    ## Returns allele depths for all alleles and sites for a taxon in byte format
    # @param taxon taxon
    # @return Allele depths for all alleles and sites
    @javaOverload("depthAllSitesByte",
            (make_sig(['int'],'byte[][]'),(metaInteger,),
             lambda x: javabridge.get_object_array_elements(x)))
    def depthAllSitesByte(self, *args):
        """
        Returns allele depths for all alleles and sites for a taxon in byte format
        (negative values are logs)

        Signatures:

        byte[][] depthAllSitesByte(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        Allele depths for all alleles and sites
        """
        pass
    ## Returns total depth for given taxon and site
    # @param taxon taxon
    # @param site site
    # @return total depth
    @javaOverload("depth",
        (make_sig(['int','int'],'int'),(metaInteger, metaInteger), None))
    def depth(self, *args):
        """
        Returns total depth for given taxon and site

        Signatures:

        int depth(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        total depth
        """
        pass
    ## Returns total depth of all alleles and sites for given taxon
    # @param taxon taxon
    # @return total depth for taxon
    @javaOverload("depthForTaxon",
        (make_sig(['int'],'int'),(metaInteger,),None))
    def depthForTaxon(self, *args):
        """
        Returns total depth of all alleles and sites for given taxon

        Signatures:

        int depthForTaxon(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        total depth for taxon
        """
        pass
    ## Returns total depth of all alleles and taxa for given site
    # @param site site
    # @return depth
    @javaOverload("depthForSite",
        (make_sig(['int'],'int'),(metaInteger,),None))
    def depthForSite(self, *args):
        """
        Returns total depth of all alleles and taxa for given site

        Signatures:

        int depthForSite(int site)

        Arguments:

        site -- site

        Returns:

        depth
        """
        pass
