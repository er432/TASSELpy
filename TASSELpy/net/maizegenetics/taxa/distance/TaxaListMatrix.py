from TASSELpy.net.maizegenetics.util.TableReport import TableReport
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.utils.helper import make_sig
import numpy as np

java_imports = {'String':'java/lang/String',
                'TaxaList':'net/maizegenetics/taxa/TaxaList',
                'TaxaListMatrix':'net/maizegenetics/taxa/distance/TaxaListMatrix'}

class TaxaListMatrix(TableReport):
    _java_name = java_imports['TaxaListMatrix']
    @javaConstructorOverload(java_imports['TaxaListMatrix'])
    def __init__(self, *args, **kwargs):
        pass
    def __getitem__(self, inds):
        if len(inds) != 2:
            raise ValueError("Must supply row and column indices")
        return self.getDistance(*inds)
    ## Return TaxaList of this matrix
    # @return TaxaList of this matrix
    @javaOverload("getTaxaList",
                  (make_sig([],java_imports['TaxaList']),(),
                   lambda x: TaxaList(obj=x)))
    def getTaxaList(self, *args):
        """
        Return TaxaList of this matrix

        Signatures:

        TaxaList getTaxaList()

        Returns:

        TaxaList of this matrix
        """
        pass
    ## Get string representation of alignment as a string
    # @return Representation of alignment as a string
    @javaOverload("toString",
                  (make_sig([],java_imports['String']),(),None))
    def toString(self, *args):
        """
        Get string representation of alignment as a string

        Signatures:

        String toString()

        Returns:

        Representation of alignment as a string
        """
        pass
    ## Returns the number of rows and columns that the distance matrix has
    # @return Number of rows and columns in the distance matrix
    @javaOverload("getSize",
                  (make_sig([],'int'),(),None))
    def getSize(self, *args):
        """
        Returns the number of rows and columns that the distance matrix has

        Signatures:

        int getSize()

        Returns:

        Number of rows and columns in the distance matrix
        """
        pass
    ## Returns the distances as a 2-dimensional array of doubles.
    # Matrix is cloned first so it can be altered freely
    # @return matrix as 2-d array of doubles
    @javaOverload("getClonedDistances",
            (make_sig([],"double[][]"),(),
            lambda x: javaPrimativeArray.get_array_type('double').wrap_existing_array(x)))
    def getClonedDistances(self, *args):
        """
        Returns the distances as a 2-dimensional array of doubles.
        Matrix is cloned first so it can be altered freely

        Signatures:

        double[][] getClonedDistances()

        Returns:

        matrix as 2-d array of doubles
        """
        pass
    ## Returns the distance calculated for two taxa with the indices row
    # and col
    # @param row row
    # @param col col
    # @return The distance for the taxa at the specified row and col
    @javaOverload("getDistance",
                  (make_sig(['int','int'],'double'),(metaInteger,metaInteger),
                   np.float64))
    def getDistance(self, *args):
        """
        Returns the distance calculated for two taxa with the indices
        row and col

        Signatures:

        double getDistance(int row, int col)

        Arguments:

        row -- row
        col -- col

        Returns:

        Distance for the two taxa at the specified indices
        """
        pass
    ## Returns the mean pairwise distance of this matrix
    # @return Mean pairwise distance of this matrix
    @javaOverload("meanDistance",
                  (make_sig([],'double'),(),np.float64))
    def meanDistance(self, *args):
        """
        Returns the mean pairwise distnace of this matrix

        Signatures:

        double meanDistance()

        Returns:

        Mean pairwise distance of this matrix
        """
        pass
    ## Test whether this matrix is a symmetric distance matrix
    # @return Whether this matrix is a symmetric distance matrix
    @javaOverload("isSymmetric",
                  (make_sig([],'boolean'),(),None))
    def isSymmetric(self, *args):
        """
        Test whether this matrix is a symmetrix distance matrix

        Signatures:

        boolean isSymmetric()

        Returns:

        Whether this matrix is a symmetric distance matrix
        """
        pass
