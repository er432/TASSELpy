import numpy as np
from TASSELpy.java.util.List import List
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.trait.Trait import Trait
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload, javaGenericOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.utils.helper import make_sig
from TASSELpy.net.maizegenetics.util.TableReport import TableReport

java_imports = {'List':'java/util/List',
                'Phenotype':'net/maizegenetics/trait/Phenotype',
                'Taxon':'net/maizegenetics/taxa/Taxon',
                'TaxaList':'net/maizegenetics/taxa/TaxaList',
                'Trait':'net/maizegenetics/trait/Trait'}
class Phenotype(TableReport):
    """
    A collection of data for a set of Taxa. Each taxon is expected to appear only
    once in the data. 
    Data is represented as a two dimensional table of doubles, with taxa as rows
    and traits as columns. 
    """
    _java_name = java_imports['Phenotype']
    @javaConstructorOverload(java_imports['Phenotype'])
    def __init__(self, *args, **kwargs):
        pass
    ## Gets data from the phenotype
    # @param taxon Either the integer or an instance of a taxon
    # @param trait Either the integer or the instance of a trait
    # @return The data stored for the given trait and taxon
    @javaOverload("getData",
            (make_sig(['int','int'],'double'),(metaInteger,metaInteger),np.float64),
            (make_sig([java_imports['Taxon'],java_imports['Trait']],'double'),
             (Taxon,Trait),np.float64),
             (make_sig([],'double[][]'),(),
              lambda x: javaPrimativeArray.get_array_type('double').wrap_existing_array(x)))
    def getData(self, *args):
        """
        Gets data from the phenotype

        Signatures:

        double getData(int taxon, int trait)
        double getData(Taxon taxon, Trait trait)
        double[][] getData()

        Arguments:

        double getData(int taxon, int trait)
            taxon -- an integer i, representing the ith row in the data set
            trait -- an integer j, representing the jth column in the data set
        double getData(Taxon taxon, Trait trait)
            taxon -- A taxon in the data set
            trait -- A trait in the data set

        Returns:

        The data stored for the given trait and taxon
        """
        pass
    ## Sets the double value for this trait and taxon
    # @param taxon An integer i, representing the ith row in the data set
    # @param trait An integer j, representing the jth column in the data set
    # @param value The data to be stored in the ith taxon, jth trait
    @javaOverload("setData",
                  (make_sig(['int','int','double'],'void'),(metaInteger,metaInteger,metaDouble),None))
    def setData(self, *args):
        """
        Sets the double value for this trait and taxon

        Signatures:

        void setData(int taxon, int trait, double value)

        Arguments:

        taxon -- An integer i, representing the ith row in the data set
        trait -- An ineger j, representing the jth column in the data set
        value -- The data to be stored for the ith taxon, jth trait
        """
        pass
    ## Gets the index of a trait
    # @param trait trait
    # @return The index of the trait, representing the column in which the data for this trait is stored
    @javaOverload("whichTrait",
                  (make_sig([java_imports['Trait']],'int'),(Trait,),None))
    def whichTrait(self, *args):
        """
        Gets the index of a trait

        Signatures:

        int whichTrait(Trait trait)

        Arguments:

        trait -- trait

        Returns:

        The index of the trait, representing the column in which the data for this trait is stored
        """
        pass
    ## Gets the index of a taxon
    # @param taxon taxon
    # @return The index of the taxon, representing the row in which the data for this taxon is stored
    @javaOverload("whichTaxon",
                  (make_sig([java_imports['Taxon']],'int'),(Taxon,),None))
    def whichTaxon(self, *args):
        """
        Gets the index of a taxon

        Signatures:

        int whichTaxon(Taxon taxon)

        Arguments:

        taxon -- taxon

        Returns:

        The index of the taxon, representing the row in which the data for this taxon is stored
        """
        pass
    ## Gets a trait
    # @param trait an integer j, representing the jth column in the data set
    # @return The Trait for this column
    @javaOverload("getTrait",
                  (make_sig(['int'],java_imports['Trait']),(metaInteger,),lambda x: Trait(obj=x)))
    def getTrait(self, *args):
        """
        Gets a trait

        Signatures:

        Trait getTrait(int trait)

        Arguments:

        trait -- An integer j, representing the jth column in the data set

        Returns:

        The Trait for this column
        """
        pass
    ## Gets a taxon
    # @param taxon An integer j, representing the jth row in the data set
    # @return The Taxon for this row
    @javaOverload("getTaxon",
                  (make_sig(['int'],java_imports['Taxon']),(metaInteger,), lambda x: Taxon(obj=x)))
    def getTaxon(self, *args):
        """
        Gets a taxon

        Signatures:

        Taxon getTaxon(int taxon)

        Arguments:

        taxon -- An integer j, representing the jth row in the data set

        Returns:

        The Taxon for this row
        """
        pass
    ## Gets the number of taxa or rows in this data set
    # @return The number of taxa or rows in this data set
    @javaOverload("getNumberOfTaxa",
                  (make_sig([],'int'),(),None))
    def getNumberOfTaxa(self, *args):
        """
        Gets the number of taxa or rows in this data set

        Signatures:

        int getNumberOfTaxa()

        Returns:

        The number of taxa or rows in this data set
        """
        pass
    ## Gets the number of traits or columns in this data set
    # @return The number of traits or columns in this data set
    @javaOverload("getNumberOfTraits",
                  (make_sig([],'int'),(),None))
    def getNumberOfTraits(self, *args):
        """
        Gets the number of traits or columns in this data set

        Signatures:

        int getNumberOfTraits()

        Returns:

        The number of traits or columns in this data set
        """
        pass
    ## Gets the traits or columns of this dataset, in order by column number
    # @return traits or columns of this dataset, in order by column number
    @javaOverload("getTraits",
                        (make_sig([],java_imports['List']),(),
                         lambda x: List(obj=x,generic=(Trait,))))
    def getTraits(self, *args):
        """
        Gets the traits or columns of this dataset, in order by column number

        Signatures:

        List<Trait> getTraits()

        Returns:

        The traits or columns of this dataset, in order by column number
        """
        pass
    ## Get the taxa in this data set in order by row number
    # @return The taxa in this data set in order by row number
    @javaOverload("getTaxa",
                  (make_sig([],java_imports['TaxaList']),(),
                   lambda x: TaxaList(obj=x)))
    def getTaxa(self, *args):
        """
        Get the taxa in this data set in order by row number

        Signatures:

        TaxaList getTaxa()

        Returns:

        The taxa in this data set in order by row number
        """
        pass
