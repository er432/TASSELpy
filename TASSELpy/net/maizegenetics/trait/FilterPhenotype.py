from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload, javaStaticOverload, javaOverload
from TASSELpy.net.maizegenetics.trait.AbstractPhenotype import AbstractPhenotype
from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype
from TASSELpy.net.maizegenetics.trait.SimplePhenotype import SimplePhenotype
from TASSELpy.net.maizegenetics.trait.Trait import Trait
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.java.util.List import List
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Double import metaDouble

java_imports = {'FilterPhenotype':'net/maizegenetics/trait/FilterPhenotype',
                'List':'java/util/List',
                'Phenotype':'net/maizegenetics/trait/Phenotype',
                'SimplePhenotype':'net/maizegenetics/trait/SimplePhenotype',
                'TaxaList':'net/maizegenetics/taxa/TaxaList',
                'Taxon':'net/maizegenetics/taxa/Taxon',
                'Trait':'net/maizegenetics/trait/Trait'}

class FilterPhenotype(AbstractPhenotype):
    """ Class used to filter through phenotypes
    """
    _java_name = java_imports['FilterPhenotype']
    @javaConstructorOverload(java_imports['FilterPhenotype'])
    def __init__(self, *args, **kwargs):
        pass
    @javaStaticOverload(java_imports['FilterPhenotype'],'getInstance',
                        (make_sig([java_imports['Phenotype'],'int[]','int[]'],
                                  java_imports['FilterPhenotype']),
                         (Phenotype,javaPrimativeArray.get_array_type('int'),
                          javaPrimativeArray.get_array_type('int')),
                         lambda x: FilterPhenotype(obj=x)),
                         (make_sig([java_imports['Phenotype'],java_imports['TaxaList'],
                                    java_imports['List']], java_imports['FilterPhenotype']),
                          (Phenotype,TaxaList,List), lambda x: FilterPhenotype(obj=x)))
    def getInstance(*args):
        """ Gets an instance of the filtered phenotype

        The indices for taxa and traits must be valid indexes in the original phenotype.
        That is, only taxa and traits in the original phenotype can be used. This function
        is not appropriate for union joins
        
        Signatures:

        static FilterPhenotype getInstance(Phenotype phenotype, int[] taxa, int[] traits)
        static FilterPhenotype getInstance(Phenotype phenotype, TaxaList taxa,
                               List<Trait> traits)

        Arguments:

        static FilterPhenotype getInstance(Phenotype phenotype, int[] taxa, int[] traits)
            phenotype -- the input Phenotype
            taxa -- an index of taxa to include in the filtered subset. If null,
                    all taxa will be included
            traits -- an index of traits to include in the filtered subset. If null,
                      all traits will be included
        static FilterPhenotype getInstance(Phenotype phenotype, TaxaList taxa,
                                   List<Trait> traits)
            phenotype -- the input Phenotype
            taxa -- the taxa to be included in the output FIlterPhenotype
            traits -- the traits to be included in the output FilterPhenotype
        
        Returns:

        A new FilterPhenotype
        """
        pass
    @javaStaticOverload(java_imports['FilterPhenotype'],"getInstanceRemoveIDs",
                        (make_sig([java_imports['Phenotype'],java_imports['TaxaList']],
                                  java_imports['FilterPhenotype']), (Phenotype, TaxaList),
                         lambda x: FilterPhenotype(obj=x)))
    def getInstanceRemoveIDs(*args):
        """ Gets a FilterPhenotype after removing certain taxa

        Signatures:

        static FilterPhenotype getInstanceRemoveIDs(Phenotype phenotype, TaxaList taxa)

        Arguments:

        phenotype -- the input Phenotype
        taxa -- the taxa to be excluded in the output FilterPhenotype

        Returns:

        A FilterPhenotype without excluded IDs
        """
        pass
    @javaOverload("setData",
                  (make_sig(['int','int','double'],'void'),
                   (metaInteger,metaInteger, metaDouble), None),
                   (make_sig([java_imports['Taxon'],java_imports['Trait'],
                              'double'],'void'),(Taxon, Trait, metaDouble), None))
    def setData(self, *args):
        """ Sets a particular datum

        Signatures:

        void setData(int taxon, int trait, double value)
        void setData(Taxon taxon, Trait trait, double value)

        Arguments:

        void setData(int taxon, int trait, double value)
            taxon -- taxon
            trait -- trait
            value -- value
        void setData(Taxon taxon, Trait trait, double value)
            taxon -- taxon
            trait -- trait
            value -- value
        """
        pass
    @javaOverload("simpleCopy",
                  (make_sig([],java_imports['SimplePhenotype']),(),
                   lambda x: SimplePhenotype(obj=x)))
    def simpleCopy(self, *args):
        """ Makes a copy of the FilterPhenotype object, returning a SimplePhenotype

        Signatures:

        SimplePhenotype simpleCopy()

        Returns:

        A SimplePhenotype
        """
        pass
