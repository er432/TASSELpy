from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.java.util.Collection import Collection
from TASSELpy.javaObj import javaObj
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
import numpy as np
from TASSELpy.java.lang.String import String

java_imports = {'Collection':'java/util/Collection',
                'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'String':'java/lang/String',
                'TaxaListBuilder':'net/maizegenetics/taxa/TaxaListBuilder',
                'TaxaList':'net/maizegenetics/taxa/TaxaList',
                'Taxon':'net/maizegenetics/taxa/Taxon'}

## A builder for creating immutable TaxaList instances
class TaxaListBuilder(javaObj):
    """
    A builder for creating immutable TaxaList instances

    Example:

    tlb = TaxaListBuilder()
    for i in xrange(10):
        at = Taxon.Builder("Z"+i+":Line:mays:Zea").inbreedF(0.99)\
             .parents("B73","B97")\
             .pedigree("(B73xB97)S6I1")\
             .build()
        tlb.add(at)
    tl = tlb.build()
    """
    _java_name = java_imports['TaxaListBuilder']
    @javaConstructorOverload(java_imports['TaxaListBuilder'],
                (make_sig([],'void'),()))
    def __init__(self, *args, **kwargs):
        pass
    ## Adds a taxon to the builder
    # @param taxon taxon
    # @return TaxaListBuilder with taxon added
    @javaOverload("add",
                  (make_sig([java_imports['Taxon']],java_imports['TaxaListBuilder']),
                   (Taxon,),lambda x: TaxaListBuilder(obj=x)))
    def add(self, *args):
        """
        Adds a taxon to the builder
        
        Signatures:

        TaxaListBuilder add(Taxon taxon)

        Arguments:

        taxon -- taxon

        Returns:

        TaxaListBuilder with taxon added
        """
        pass
    ## Adds multiple taxa to the builder
    # @param taxa A collection of taxa (either collection of Taxons or Strings)
    # @param a GenotypeTable from which to add taxa
    # @return TaxaListBuilder with taxa added
    @javaOverload("addAll",
            (make_sig([java_imports['Collection']],java_imports['TaxaListBuilder']),
                (Collection,),lambda x: TaxaListBuilder(obj=x)),
            (make_sig([java_imports['GenotypeTable']],java_imports['TaxaListBuilder']),
                (GenotypeTable,),lambda x: TaxaListBuilder(obj=x)),
            (make_sig([java_imports['String']+'[]'],java_imports['TaxaListBuilder']),
                (javaArray.get_array_type(String),),lambda x: TaxaListBuilder(obj=x)),
            (make_sig([java_imports['Taxon']+'[]'],java_imports['TaxaListBuilder']),
                (javaArray.get_array_type(Taxon),), lambda x: TaxaListBuilder(obj=x)))
    def addAll(self, *args):
        """
        Adds multiple taxa to the builder

        Signatures:

        TaxaListBuilder addAll(Collection<Taxon> taxa)
        TaxaListBuilder addAll(GenotypeTable a)
        
        Arguments:

        TaxaListBuilder addAll(Collection<Taxon> taxa)
           taxa -- taxa
        TaxaListBuilder addAll(GenotypeTable a)
           a -- GenotypeTable from which to add taxa
        TaxaListBuilder addAll(String[] taxa)
           taxa -- taxa
        TaxaListBuilder addAll(Taxon[] taxa)
           taxa -- taxa
        
        Returns:

        TaxaListBuilder with taxa added
        """
        pass
    ## Builds the TaxaList
    # @return A TaxaList
    @javaOverload("build",
        (make_sig([],java_imports['TaxaList']),(),lambda x: TaxaList(obj=x)))
    def build(self, *args):
        """
        Builds the TaxaList

        Signatures:

        TaxaList build()

        Returns:

        A TaxaList
        """
        pass
