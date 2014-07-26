from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Enum import Enum
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
import numpy as np
import javabridge

java_imports={'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
            'SiteScore':'net/maizegenetics/dna/snp/score/SiteScore'}

## SiteScore
class SiteScore(Object):
    """
    SiteScore
    """
    @javaConstructorOverload(java_imports['SiteScore'])
    def __init__(self, *args, **kwargs):
        pass
    ## Returns the site score of the given sequence and site
    # @param taxon taxon
    # @param site site
    # @return site score
    @javaOverload("siteScore",
            (make_sig(['int','int'],'float'),(metaInteger, metaInteger),None))
    def siteScore(self, *args):
        """
        Returns the site score of the given sequence and site

        Signatures:

        float siteScore(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        site score
        """
        pass
    ## Returns the site scores
    # @return site scores
    @javaOverload("siteScores",
            (make_sig([],'float[][]'),(),
             lambda x: map(lambda y: javabridge.get_env().get_float_array_elements(y),
                           javabridge.get_env().get_object_array_elements(x))))
    def siteScores(self, *args):
        """
        Returns the site scores

        Signatures:

        float[][] siteScores()

        Returns:

        site scores
        """
        pass
    ## Returns true if this alignment has site scores
    # @return true if this alignment has site scores
    @javaOverload("hasSiteScores",
                  (make_sig([],'boolean'),(),None))
    def hasSiteScores(self, *args):
        """
        Returns true if this alignment has site scores

        Signatures:

        boolean hasSiteScores()

        Returns:

        true if this alignment has site scores
        """
        pass
    ## Return what type of site scores this alignment has
    # @return site score type
    @javaOverload("siteScoreType",
            (make_sig([],java_imports['GenotypeTable']+'$SITE_SCORE_TYPE'),(),
             lambda x: Enum(obj=x)))
    def siteScoreType(self, *args):
        """
        Return what type of site scores this alignment has

        Signatures:

        GenotypeTable.SITE_SCORE_TYPE siteScoreType()

        Returns:

        site score type
        """
        pass
