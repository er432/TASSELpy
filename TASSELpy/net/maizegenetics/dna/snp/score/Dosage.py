from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.net.maizegenetics.dna.snp.score.SiteScore import SiteScore
from TASSELpy.net.maizegenetics.dna.snp.byte2d.Byte2D import Byte2D
from TASSELpy.java.lang.Integer import metaInteger
import numpy as np

java_imports = {'Byte2D':'net/maizegenetics/dna/snp/byte2d/Byte2D',
                'Dosage':'net/maizegenetics/sna/snp/score/Dosage'}

class Dosage(SiteScore):
    _java_name = java_imports['Dosage']
    @javaConstructorOverload(java_imports['Dosage'],
                             (make_sig([java_imports['Byte2D']],'void'),
                              (Byte2D,)))
    def __init__(self, *args, **kwargs):
        """ Instantiates Dosage

        Signatures:

        Dosage(Byte2D value)

        Arguments:

        value -- storage of dosage values
        """
        pass
    @javaOverload('value',
                  (make_sig(['int','int'],'byte'), (metaInteger, metaInteger),
                   np.int8))
    def value(self, *args):
        """ Gets the dosage value for a site/taxon

        Signatures:

        byte value(int taxon, int site)

        Arguments:

        taxon -- taxon
        site -- site

        Returns:

        The value for a taxon/site
        """
        pass
