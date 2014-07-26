from TASSELpy.java.util.FilterList import FilterList
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.javaObj import javaObj
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.java.lang.String import metaString

java_imports = {'String':'java/lang/String',
                'TaxaList':'net/maizegenetics/taxa/TaxaList',
                'Taxon':'net/maizegenetics/taxa/Taxon'}

class TaxaList(FilterList):
    _java_name = java_imports['TaxaList']
    @javaConstructorOverload(java_imports['TaxaList'])
    def __init__(self, *args, **kwargs):
        super(TaxaList, self).__init__(*args, generic=(Taxon,), **kwargs)
    ## Returns number of taxa
    # @return Number of taxa
    @javaOverload("numberOfTaxa",
                  (make_sig([],'int'),(),None))
    def numberOfTaxa(self, *args):
        """
        Returns number of taxa

        Signatures:

        int numberOfTaxa()

        Returns:

        Number of taxa
        """
        pass
    ## Returns taxa name at given index
    # @param index index
    # @return taxa name
    @javaOverload("taxaName",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def taxaName(self, *args):
        """
        Return taxa name at given index

        Signatures:

        String taxaName(int index)

        Arguments:

        index -- index

        Returns:

        taxa name
        """
        pass
    @javaOverload("indexOf",
                  (make_sig([java_imports['String']],'int'),(metaString,),None),
                  (make_sig([java_imports['Taxon']],'int'),(Taxon,),None))
    def indexOf(self, *args):
        """
        Return matching taxa index for given name

        Signatures:

        int indexOf(String name)
        int indexOf(Taxon taxon)

        Arguments:

        int indexOf(String name)
           name -- name
        int indexOf(Taxon taxon)
           taxon --- taxon

        Returns:

        Index for matching taxon (-1 if no match)
        """
        pass
