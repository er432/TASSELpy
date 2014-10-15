from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.net.maizegenetics.dna.snp.score.SiteScore import SiteScore
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.java.lang.Enum import Enum
import numpy as np

java_imports = {'Byte2D':'net/maizegenetics/dna/snp/byte2d/Byte2D',
                'SiteScore':'net/maizegenetics/dna/snp/score/SiteScore'
}
class Byte2D(Object):
    _java_name = java_imports['Byte2D']
    @javaConstructorOverload(java_imports['Byte2D'])
    def __init__(self, *args, **kwargs):
        pass
    @javaOverload("valueForAllele",
                  (make_sig(['int','int'],'byte'),(metaInteger,metaInteger),np.int8))
    def valueForAllele(self, *args):
        """ Gets the byte value for a particular allele in the matrix

        Signatures:

        byte valueForAllele(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:
        The byte value for the allele
        """
        pass
    @javaOverload("valuesForAllSites",
                  (make_sig(['int'],'byte[]'),(metaInteger,),
                   lambda x: javaPrimativeArray.make_array_from_obj('byte', x)))
    def valuesForAllSites(self, *args):
        """ Gets the byte values for all sites on a taxon

        Signatures:

        byte[] valuesForAllSites(int taxon)

        Arguments:

        taxon -- taxon

        Returns:

        The array of bytes for a taxon, where each entry is a genotype
        """
        pass
    @javaOverload("numTaxa",
                  (make_sig([],'int'),(),None))
    def numTaxa(self, *args):
        """ The number of taxa in the matrix

        Signatures:

        int numTaxa()

        Returns:

        The number of taxa in the matrix
        """
        pass
    @javaOverload("numSites",
                  (make_sig([],'int'),(),None))
    def numSites(self, *args):
        """ The number of sites in the matrix

        Signatures:

        int numSites()

        Returns:

        The number of sites in the matrix
        """
        pass
    @javaOverload("siteScoreType",
                  (make_sig([],java_imports['SiteScore']+'$SITE_SCORE_TYPE'),
                    (), lambda x: Enum(obj=x)))
    def siteScoreType(self, *args):
        """ The site score type for sites

        Signatures:

        SiteScore.SITE_SCORE_TYPE siteScoreType()

        Returns:

        The SITE_SCORE_TYPE
        """
        pass
