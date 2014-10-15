from TASSELpy.utils.helper import make_sig
from TASSELpy.java.lang.Enum import Enum
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.net.maizegenetics.dna.snp.score.SiteScore import SiteScore
from TASSELpy.java.lang.Integer import metaInteger

java_imports = {'AlleleProbability':'net/maizegenetics/dna/snp/score/AlleleProbability',
                'Byte2D':'net/maizegenetics/dna/snp/byte2d/Byte2D',
                'SiteScore':'net/maizegenetics/dna/snp/score/SiteScore'}

class AlleleProbability(SiteScore):
    """ Representation of allele probabilities
    """
    _java_name = java_imports['AlleleProbability']
    @javaConstructorOverload(java_imports['AlleleProbability'],
                             (make_sig([java_imports['Byte2D']],'void'),()))
    def __init__(self, *args, **kwargs):
        """ Instantiates an AlleleProbability object

        Signatures:

        AlleleProbability(Byte2D[] values)

        Arguments:

        values -- values
        """
        pass
    @javaOverload('value',
                  (make_sig(['int','int',java_imports['SiteScore']+'$SITE_SCORE_TYPE'],
                            'float'), (metaInteger, metaInteger, Enum), None))
    def value(self, *args):
        """ Gets the value of the probability at a site

        Signatures:

        float value(int taxon, int site, SITE_SCORE_TYPE scoreType)

        Arguments:

        taxon -- taxon
        site -- site
        scoreType -- score type

        Returns:

        The value of the score at the site for the taxon
        """
        pass
