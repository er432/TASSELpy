from TASSELpy.net.maizegenetics.taxa.distance.TaxaListMatrix import TaxaListMatrix
from TASSELpy.java.lang.String import metaString
from TASSELpy.java.lang.Integer import Integer, metaInteger
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.util.TableReport import TableReport
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray,meta_int_array
from TASSELpy.javaObj import javaArray
from abc import ABCMeta
import numpy as np

java_imports = {'DistanceMatrix':'net/maizegenetics/taxa/distance/DistanceMatrix',
                'String':'java/lang/String',
                'Taxon':'net/maizegenetics/taxa/Taxon',
                'TaxaList':'net/maizegenetics/taxa/TaxaList'}

class metaDistanceMatrix:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C, DistanceMatrix):
            return True
        else:
            return False

class DistanceMatrix(TaxaListMatrix, TableReport):
    """
    Storage for pairwise distance matrices
    """
    _java_name = java_imports['DistanceMatrix']
    ## Constructs DistanceMatrix
    @javaConstructorOverload(java_imports['DistanceMatrix'],
                (make_sig([],'void'),()),
                (make_sig(['double[][]',java_imports['TaxaList']],'void'),
                 (javaArray.get_array_type(javaPrimativeArray.get_array_type('double')),
                  TaxaList)),
                (make_sig([java_imports['DistanceMatrix']],'void'),(metaDistanceMatrix,)),
                (make_sig([java_imports['DistanceMatrix'], java_imports['TaxaList']],'void'),
                 (metaDistanceMatrix, TaxaList)))
    def __init__(self, *args, **kwargs):
        """
        Constructs DistanceMatrix

        Signatures:

        DistanceMatrix()
        DistanceMatrix(double[][] distance, TaxaList taxaList)
        DistanceMatrix(DistanceMatrix dm)
        DistanceMatrix(DistanceMatrix dm, TaxaList subset)

        Arguments:

        DistanceMatrix(double[][] distance, TaxaList taxaList)
            distance -- distances between taxa
            taxaList -- The taxa in the matrix
        DistanceMatrix(DistanceMatrix dm)
            dm -- DistanceMatrix to clone
        DistanceMatrix(DistanceMatrix dm, TaxaList subset)
            dm -- Distance matrix from which to clone some distances
            subset -- The taxa that you want in the resulting matrix
        """
        pass
    ## Compute squared distance to second distance matrix
    # @param mat -- Second DistanceMatrix
    # @param weighted -- Whethter to weight with Fitch-margoliash weights
    # @return Squared distance to second distance matrix
    @javaOverload("squaredDistance",
                  (make_sig([java_imports['DistanceMatrix'],'boolean'],'double'),
                   (metaDistanceMatrix,metaBoolean),np.float64))
    def squaredDistance(self, *args):
        """
        Compute squared distance to second distance matrix

        Signatures:

        double squaredDistance(DistanceMatrix mat, boolean weighted)

        Arguments:

        mat -- Second DistanceMatrix
        weighted -- Whether to weight with Fitch margoliash weights

        Returns:

        Squared distance to second distance matrix
        """
        pass
    ## Compute absolute distance to second distance matrix
    # @param mat Second DistanceMatrix
    # @return Absolute distance to second distance matrix
    @javaOverload("absoluteDistance",
                  (make_sig([java_imports['DistanceMatrix']],'double'),(metaDistanceMatrix,),
                   np.float64))
    def absoluteDistance(self, *args):
        """
        Compute absolute distance to second distance matrix

        Signatures:

        double absoluteDistance(DistanceMatrix mat)

        Arguments:

        mat -- Second DistanceMatrix

        Returns:

        Absolute distance to second distance matrix
        """
        pass
    ## Returns the distances as a 2-dimensional array of doubles (in the actual array used
    # to store the distances)
    # @return A clone of the array used to store distances
    @javaOverload("getDistances",
                  (make_sig([],'double[][]'),(),
                    lambda x: javaPrimativeArray.get_array_type('double').wrap_existing_array(x)))
    def getDistances(self, *args):
        """
        Returns the distances as a 2-dimensional array of doubles (in the actual array used
        to store the distances)

        Signatures:

        final double[][] getDistances()

        Returns:

        A clone of the array used to store distances
        """
        pass
    ## Gets a taxon
    # @param i The index of the taxon
    # @return The taxon at index i
    @javaOverload("getTaxon",
                  (make_sig(['int'],java_imports['Taxon']),(metaInteger,),
                    lambda x: Taxon(obj=x)))
    def getTaxon(self, *args):
        """
        Gets a Taxon

        Signatures:

        Taxon getTaxon(int i)

        Arguments:

        i -- The index of the taxon
        
        Returns:

        The taxon at index i
        """
        pass
    ## Gets the number of taxa
    # @return The number of taxa
    @javaOverload("numberOfTaxa",
            (make_sig([],'int'),(),None))
    def numberOfTaxa(self, *args):
        """
        Gets the number of taxa

        Signatures:

        int numberOfTaxa()

        Returns:

        The number of taxa
        """
        pass
    ## Gets the id number of a taxon
    # @param name The name of the taxon as a string
    # @param id The taxon as a Taxon
    # @return The id number of the taxon
    @javaOverload("whichIdNumber",
            (make_sig([java_imports['String']],'int'),(metaString,),None),
            (make_sig([java_imports['Taxon']],'int'),(Taxon,),None))
    def whichIdNumber(self, *args):
        """
        Gets the id number of a taxon

        Signatures:

        int whichIdNumber(String name)
        int whichIdNumber(Taxon id)

        Arguments:

        int whichIdNumber(String name)
            name -- The name of the taxon as a string
        int whichIdNumber(Taxon id)
            id -- The taxon as a Taxon

        Returns:

        The id number of the taxon
        """
        pass
    ## Gets the index of the taxon closest to a given taxon
    # @param fromIndex The index of the thing (taxa, sequence) from which we want to
    # find the closest (excluding self)
    # @param exclusion Indexes of things that should not be considered, may be null
    # @return The index of the member closest to the specified
    @javaOverload("getClosestIndex",
            (make_sig(['int','int[]'],'int'),(metaInteger,
                                              meta_int_array),
                                              None))
    def getClosestIndex(self, *args):
        """
        Gets the index of the taxon closest to a given taxon

        Signatures:

        int getClosestIndex(int fromIndex, int[] exclusion)

        Arguments:

        fromIndex -- the index of the thing (taxa, sequence) from which we want to find the closest
                     (excluding self)
        exclusion -- Indexes of things that should not be considered, may be null

        Returns:

        The index of the member closest to the specified
        """
        pass
    ## Gets a column name
    # @param col Index of the column
    # @return Name of the column
    @javaOverload("getColumnName",
            (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def getColumnName(self, *args):
        """
        Gets a column name

        Signatures:

        String getColumnName(int col)

        Arguments:

        col -- Index of the column

        Returns:

        Name of the column
        """
        pass
