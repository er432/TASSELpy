from TASSELpy.java.lang.Object import Object
import TASSELpy.net.maizegenetics.matrixalgebra.Matrix.DoubleMatrix
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray
import numpy as np

java_imports = {'DoubleMatrix': 'net/maizegenetics/matrixalgebra/Matrix/DoubleMatrix',
                'EigenvalueDecomposition':'net/maizegenetics/matrixalgebra/decomposition/EigenvalueDecomposition'}

class EigenvalueDecomposition(Object):
    _java_name = java_imports['EigenvalueDecomposition']
    @javaConstructorOverload(java_imports['EigenvalueDecomposition'])
    def __init__(self, *args, **kwargs):
        pass
    ## Gets the eigenvalues for the decomposition
    # @return Array of eigenvalues
    @javaOverload("getEigenvalues",
                  (make_sig([],'double[]'),(),
                   lambda x: javaPrimativeArray.make_array_from_obj('double',x)))
    def getEigenvalues(self, *args):
        """
        Gets the eigenvalues for the decomposition

        Signatures:

        double[] getEigenvalues()

        Returns:

        Array of eigenvalues
        """
        pass
    ## Gets a single eigenvalue for the decomposition
    # @param i index of the eigenvalue you want
    # @return An eigenvalue
    @javaOverload("getEigenvalue",
                  (make_sig(['int'],'double'),(metaInteger,), np.float64))
    def getEigenvalue(self, *args):
        """
        Gets a single eigenvalue for the decomposition

        Signatures:

        double getEigenvalue(int i)

        Arguments:

        i -- index of the eigenvalue you want

        Returns:

        An eigenvalue
        """
        pass
    ## Gets the eigenvectors as a matrix
    # @return A DoubleMatrix containing the eigenvectors
    @javaOverload("getEigenvectors",
                  (make_sig([],java_imports['DoubleMatrix']),(),
                   lambda x: TASSELpy.net.maizegenetics.matrixalgebra.\
                             Matrix.DoubleMatrix.DoubleMatrix(obj=x)))
    def getEigenvectors(self, *args):
        """
        Gets the eigenvectors as a matrix

        Signatures:

        DoubleMatrix getEigenvectors()

        Returns:

        A DoubleMatrix containing the eigenvectors
        """
        pass
    ## Gets the eigenvalue matrix
    # @return The matrix containing the eigenvalues
    @javaOverload("getEigenvalueMatrix",
                  (make_sig([],java_imports['DoubleMatrix']),(),
                   lambda x: TASSELpy.net.maizegenetics.matrixalgebra.\
                             Matrix.DoubleMatrix.DoubleMatrix(obj=x)))
    def getEigenvalueMatrix(self, *args):
        """
        Gets the eigenvalue matrix

        Signatures:

        DoubleMatrix getEigenvalueMatrix()

        Returns:

        The matrix containing the eigenvalues
        """
        pass
