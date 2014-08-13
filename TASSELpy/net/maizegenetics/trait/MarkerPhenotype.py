from TASSELpy.utils.helper import make_sig
from TASSELpy.net.maizegenetics.util.TableReport import TableReport
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaStaticOverload
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from abc import ABCMeta

java_imports = {'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'MarkerPhenotype':'net/maizegenetics/trait/MarkerPhenotype',
                'Phenotype':'net/maizegenetics/trait/Phenotype',
                'TaxaList':'net/maizegenetics/taxa/TaxaList'}

class metaMarkerPhenotype:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C, MarkerPhenotype):
            return True
        else:
            return False

class MarkerPhenotype(TableReport):
    """ Class combining a GenotypeTable and a Phenotype. Enters into
    quantitative genetics models
    """
    _java_name = java_imports['MarkerPhenotype']
    @javaConstructorOverload(java_imports['MarkerPhenotype'])
    def __init__(self, *args, **kwargs):
        pass
    @javaStaticOverload(java_imports['MarkerPhenotype'],"getInstance",
                        (make_sig([java_imports['GenotypeTable'], java_imports['Phenotype'],
                                   'boolean'],java_imports['MarkerPhenotype']),
                         (GenotypeTable, Phenotype, metaBoolean),
                         lambda x: MarkerPhenotype(obj=x)),
                         (make_sig([java_imports['MarkerPhenotype'],java_imports['TaxaList']],
                                   java_imports['MarkerPhenotype']),
                          (metaMarkerPhenotype,TaxaList), lambda x: MarkerPhenotype(obj=x)))
    def getInstance(*args):
        """ Gets an instance of a MarkerPhenotype class

        Signatures:

        static MarkerPhenotype getInstance(GenotypeTable aa, Phenotype ca, boolean union)
        static MarkerPhenotype getInstance(MarkerPhenotype aac, TaxaList group)

        Arguments:

        static MarkerPhenotype getInstance(GenotypeTable aa, Phenotype ca, boolean union)
            aa -- the GenotypeTable containing the markers
            ca -- The phenotype object containing 1 or more phenotype
            union -- Whether to take all taxa present in aa and/or ca. If false, uses the intersection
                     of everything
        static MarkerPhenotype getInstance(MarkerPhenotype aac, TaxaList group)
            aac -- An existing MarkerPhenotype object to use
            group -- TaxaList containing the taxa to keep

        Returns:

        A MarkerPhenotype data containing the desired data
        """
        pass
    @javaOverload("getAlignment",
                  (make_sig([],java_imports['GenotypeTable']),(),
                   lambda x: GenotypeTable(obj=x)))
    def getAlignment(self, *args):
        """ Gets the alignment

        Signatures:

        GenotypeTable getAlignment()

        Returns:

        The alignment
        """
        pass
    @javaOverload("getPhenotype",
                  (make_sig([],java_imports['Phenotype']),
                   (),lambda x: Phenotype(obj=x)))
    def getPhenotype(self, *args):
        """ Gets the phenotype

        Signatures:

        Phenotype getPhenotype()

        Returns:

        The Phenotype
        """
        pass
