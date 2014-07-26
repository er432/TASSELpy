from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.net.maizegenetics.dna.map.Chromosome import Chromosome
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.net.maizegenetics.taxa.TaxaListBuilder import TaxaListBuilder
from TASSELpy.java.lang.String import String, metaString
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload,javaStaticOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import javaArray
import numpy as np
import javabridge

from TASSELpy.utils.primativeArray import meta_int_array

java_imports = {'Chromosome':'net/maizegenetics/dna/map/Chromosome',
                'FilterGenotypeTable':'net/maizegenetics/dna/snp/FilterGenotypeTable',
                'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'String':'java/lang/String',
                'TaxaList':'net/maizegenetics/taxa/TaxaList'}

class FilterGenotypeTable(GenotypeTable):
    _java_name = java_imports['FilterGenotypeTable']
    @javaConstructorOverload(java_imports['FilterGenotypeTable'])
    def __init__(self, *args, **kwargs):
        pass
    ## This returns filterGenotypeTable with only specified subTaxaList. Defaults
    # to retain unknown taxa. If retainUnknownTaxa is true then Alignment will return
    # unknown values for missing taxa
    # @param a alignment
    # @param subTaxaList subset id group
    # @param retainUnknownTaxa whether to retain unknown taxa
    @javaStaticOverload(java_imports['FilterGenotypeTable'],"getInstance",
            (make_sig([java_imports['GenotypeTable'],java_imports['TaxaList']],
                      java_imports['GenotypeTable']),(GenotypeTable, TaxaList),
                      lambda x: GenotypeTable(obj=x)),
            (make_sig([java_imports['GenotypeTable'],java_imports['TaxaList'],'boolean'],
                      java_imports['GenotypeTable']),(GenotypeTable,TaxaList,metaBoolean),
                      lambda x: GenotypeTable(obj=x)),
            (make_sig([java_imports['GenotypeTable'],'int[]'],java_imports['FilterGenotypeTable']),
                (GenotypeTable, meta_int_array), lambda x: FilterGenotypeTable(obj=x)),
            (make_sig([java_imports['GenotypeTable'],java_imports['String']+'[]'],
                      java_imports['FilterGenotypeTable']),
            (GenotypeTable,javaArray.get_array_type(String)),
            lambda x: FilterGenotypeTable(obj=x)),
            (make_sig([java_imports['GenotypeTable'],java_imports['String'],'int','int'],
                      java_imports['FilterGenotypeTable']),(GenotypeTable, metaString,
                      metaInteger, metaInteger),
                      lambda x: FilterGenotypeTable(obj = x)),
            (make_sig([java_imports['GenotypeTable'],java_imports['Chromosome'],'int','int'],
                      java_imports['FilterGenotypeTable']),(GenotypeTable,Chromosome,metaInteger,metaInteger),
                      lambda x: FilterGenotypeTable(obj = x)),
            (make_sig([java_imports['GenotypeTable'],java_imports['Chromosome']],
                      java_imports['FilterGenotypeTable']),(GenotypeTable,Chromosome),
                      lambda x: FilterGenotypeTable(obj = x)),
            (make_sig([java_imports['GenotypeTable'],'int','int'],java_imports['FilterGenotypeTable']),
                      (GenotypeTable,metaInteger,metaInteger), lambda x: FilterGenotypeTable(obj=x))
            )
    def getInstance(*args):
        """
        This returns FilterGenotypeTable with only specified subTaxaList. Defaults
        to retain unknown taxa. If retainUnkownTaxa is true then Alignment will return
        unknown values for missing taxa

        Signatures:

        static GenotypeTable getInstance(GenotypeTable a, TaxaList subTaxaList)
        static GenotypeTable getInstance(GenotypeTable a, TaxaList subTaxaList, boolean retainUnknownTaxa)
        static FilterGenotypeTable getInstance(GenotypeTable a, int[] subSites)
        static FilterGenotypeTable getInstance(GenotypeTable a, String[] siteNamesToKeep)
        static FilterGenotypeTable getInstance(GenotypeTable a, String chromosome,
                                                int startPhysicalPos, int endPhysicalPos)
        static FilterGenotypeTable getInstance(GenotypeTable a, Chromosome chromosome,
                                                int startPhysicalPos, int endPhysicalPos)
        static FilterGenotypeTable getInstance(GenotypeTable a, Chromosome chromosome)
        static FilterGenotypeTable getInstance(GenotypeTable a, int startSite, int endSite)
        
        Arguments:

        GenotypeTable getInstance(GenotypeTable a, TaxaList subTaxaList)
           a -- alignment
           subTaxaList -- subset id group
        GenotypeTable getInstance(GenotypeTable a, TaxaList subTaxaList, boolean retainUnknownTaxa)
           a -- alignment
           subTaxaList -- subset id group
           retainUnknownTaxa -- whether to retain unknown taxa
        static FilterGenotypeTable getInstance(GenotypeTable a, int[] subSites)
           a -- alignment
           subSites -- subset of sites you want
        static FilterGenotypeTable getInstance(GenotypeTable a, String[] siteNamesToKeep)
           a -- alignment
           siteNamesToKeep -- names of the sites to keep
        static FilterGenotypeTable getInstance(GenotypeTable a, String chromosome,
                                                int startPhysicalPos, int endPhysicalPos)
           a -- alignment
           chromosome -- name of chromosome
           startPhysicalPos -- starting physical position
           endPhysicalPos -- ending physical position
        static FilterGenotypeTable getInstance(GenotypeTable a, Chromosome chromosome,
                                                int startPhysicalPos, int endPhysicalPos)
           a -- alignment
           chromosome -- instance of a chromosome to keep
           startPhysicalPos -- starting physical position
           endPhysicalPos -- ending physical position
        static FilterGenotypeTable getInstance(GenotypeTable a, Chromosome chromosome)
           a -- alignment
           chromosome -- instance of a chromosome to keep
        static FilterGenotypeTable getInstance(GenotypeTable a, int startSite, int endSite)
           a -- alignment
           startSite -- start site (inclusive)
           endSite -- end site (inclusive)
        
        Returns:

        filter alignment
        """
        pass
    ## Removes specific IDs
    # @param a alignment to filer
    # @param subTaxaList specified IDs
    # @return Filtered Alignment
    @javaStaticOverload(java_imports['FilterGenotypeTable'],"getInstanceRemoveIDs",
            (make_sig([java_imports['GenotypeTable'],java_imports['TaxaList']],
                      java_imports['GenotypeTable']),(GenotypeTable, TaxaList),
                      lambda x: GenotypeTable(obj = x)))
    def getInstanceRemoveIDs(*args):
        """
        Removes specific IDs

        Signatures:

        static GenotypeTable getInstanceRemoveIDs(GenotypeTable a, TaxaList subTaxaList)

        Arguments:

        a -- alignment to filter
        subTaxaList -- specified IDs

        Returns:

        Filtered Alignment
        """
        pass
    ## Removes specific named sites
    # @param a alignment
    # @param siteNamesToRemove names of the sites to remove
    # @return Filtered alignment
    @javaStaticOverload(java_imports['FilterGenotypeTable'],"getInstanceRemoveSiteNames",
            (make_sig([java_imports['GenotypeTable'],java_imports['String']+'[]'],
                      java_imports['FilterGenotypeTable']),(GenotypeTable, np.ndarray),
                      lambda x: FilterGenotypeTable(obj = x)))
    def getInstanceRemoveSiteNames(self, *args):
        """
        Removes specific named sites
        
        Signatures:

        static FilterGenotypeTable getInstanceRemoveSiteNames(GenotypeTable a, String[] siteNamesToRemove)

        Arguments:
        
        static FilterGenotypeTable getInstanceRemoveSiteNames(GenotypeTable a, String[] siteNamesToRemove)
           a -- alignment
           siteNamesToRemove -- names of the sites to remove

        Returns:

        Filtered Alignment
        """
        pass
    @javaOverload("translateSite",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def translateSite(self, *args):
        """
        Signatures:

        int translateSite(int site)

        Arguments:

        site -- site
        """
        pass
    ## Returns site of this FilterGenotypeTable based on given site from
    # embedded alignment
    @javaOverload("reverseTranslateSite",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def reverseTranslateSite(self, *args):
        """
        Returns site of this FilterGenotypeTable based on given site from
        embedded Alignment

        Signatures:

        int reverseTranslateSite(int site)

        Arguments:

        site -- site

        Returns:

        site of this FilterGenotypeTable based on given site from
        embedded Alignment
        """
        pass
    ## Returns sites from original alignment that are viewable (not filtered) by
    # this filter alignment
    # @return list of sites
    @javaOverload("getBaseSitesShown",
                  (make_sig([],'int[]'),(),
                   lambda x: javabridge.get_env().get_int_array_elements(x)))
    def getBaseSitesShown(self, *args):
        """
        Returns sites from original alignment that are viewable (not filtered) by
        this filter alignment

        Signatures:

        int[] getBaseSitesShown()

        Returns:

        list of sites
        """
        pass
    @javaOverload("translateTaxon",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def translateTaxon(self, *args):
        """
        Signatures:

        int translateTaxon(int taxon)

        Arguments:

        taxon -- taxon
        """
        pass
    @javaOverload("getBaseAlignment",
                  (make_sig([],java_imports['GenotypeTable']),(),
                   lambda x: GenotypeTable(obj=x)))
    def getBaseAlignment(self, *args):
        """
        Signatures:

        GenotypeTable getBaseAlignment()
        """
        pass
    @javaOverload("isTaxaFilter",
                  (make_sig([],'boolean'),(),None))
    def isTaxaFilter(self, *args):
        """
        Signatures:

        boolean isTaxaFilter()
        """
    @javaOverload("isSiteFilter",
                  (make_sig([],'boolean'),(),None))
    def isSiteFilter(self, *args):
        """
        Signatures:

        boolean isSiteFilter()
        """
    @javaOverload("isSiteFilterByRange",
                  (make_sig([],'boolean'),(),None))
    def isSiteFilterByRange(self, *args):
        """
        Signatures:

        boolean isSiteFilterByRange()
        """
    @staticmethod
    def functionalFilters(genoTable, sitesFilter=None,
                          taxaFilter=None):
        if sitesFilter:
            # Filter the sites
            subSites = list(genoTable.positions().filterEnumerator(sitesFilter))
            subSites = np.array(map(lambda x: x[0],subSites),dtype=np.int32)
            genoTable = FilterGenotypeTable.getInstance(genoTable, subSites)
        if taxaFilter:
            # Filter the taxa into a python list as taxa objects
            keeper_taxa = list(genoTable.taxa().filterIterator(taxaFilter))
            # Turn the python list into a wrapped java array of taxa objects
            taxon_arr = Taxon.getArray(len(keeper_taxa))
            for i,taxon in enumerate(keeper_taxa):
                taxon_arr[i] = taxon
            # Create the taxaList builder
            builder = TaxaListBuilder()
            # Add all taxa to builder
            builder = builder.addAll(taxon_arr)
            # Create the new taxaList
            subTaxaList = builder.build()
            # Return the new GenotypeTable
            genoTable = FilterGenotypeTable.getInstance(genoTable, subTaxaList)
        return genoTable
