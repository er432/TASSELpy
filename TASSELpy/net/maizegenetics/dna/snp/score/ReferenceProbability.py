from TASSELpy.utils.helper import make_sig
from TASSELpy.net.maizegenetics.dna.snp.score.SiteScore import SiteScore
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.net.maizegenetics.dna.snp.byte2d import Byte2D
from TASSELpy.java.lang.Integer import metaInteger

java_imports = {'Byte2D':'net/maizegenetics/dna/snp/byte2d/Byte2D',
                'ReferenceProbability':'net/maizegenetics/dna/snp/score/ReferenceProbability'}
class ReferenceProbability(SiteScore):
    """ ReferenceProbability
    """
    @javaConstructorOverload(java_imports['ReferenceProbability'],
                             (make_sig([java_imports['Byte2D']],'void'),(Byte2D,)))
    def __init__(self, *args, **kwargs):
        """ Instantiates a ReferenceProbability

        Signatures:

        ReferenceProbability(Byte2D value)

        Arguments:

        value -- value
        """
        pass
    @javaOverload("value",
                  (make_sig(['int','int'],'float'), (metaInteger,metaInteger),
                   None))
    def value(self, *args):
        """ Gets the value of the Reference probability for a given site and taxon

        Signatures:

        float value(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        value for the site/taxon
        """
        pass
