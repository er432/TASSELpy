from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.net.maizegenetics.matrixalgebra.Matrix.DoubleMatrix import DoubleMatrix
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload,javaStaticOverload
from TASSELpy.java.lang.Enum import enum as java_enum
from TASSELpy.java.lang.Enum import Enum
from TASSELpy.utils.primativeArray import javaPrimativeArray, meta_double_array
from TASSELpy.javaObj import javaArray

java_imports = {'DoubleMatrix':'net/maizegenetics/matrixalgebra/Matrix/DoubleMatrix',
                'DoubleMatrixFactory':'net/maizegenetics/matrixalgebra/Matrix/DoubleMatrixFactory'}

## Builder for creating DoubleMatrix objects
class DoubleMatrixFactory(Object):
    """
    Builder for creating DoubleMatrix objects
    """
    _java_name = java_imports['DoubleMatrixFactory']
    ## FactoryType enum
    FactoryType = java_enum(java_imports['DoubleMatrixFactory']+'$FactoryType',
                            "ejml","jblas","colt","blas",subclass='FactoryType')
    ## Constructs a DoubleMatrixFactory
    # @param type One of the DoubleMatrixFactory.FactoryType types
    @javaConstructorOverload(java_imports['DoubleMatrixFactory'],
                             (make_sig([java_imports['DoubleMatrixFactory']+'$FactoryType'],
                                       'void'),
                                (FactoryType.subclass,)))
    def __init__(self, *args, **kwargs):
        """
        Constructor for DoubleMatrixFactory

        Signatures:

        DoubleMatrixFactory(FactoryType type)

        Arguments:

        type -- One of the DoubleMatrixFactory.FactoryType types (ejml,jblas,colt,blas)
        """
        pass
    ## Sets the default DoubleMatrix type
    # @param type One of the DoubleMatrixFactory.FactoryType types
    @javaStaticOverload(java_imports['DoubleMatrixFactory'],"setDefault",
                        (make_sig([java_imports['DoubleMatrixFactory']+'$FactoryType'],
                                  'void'),(FactoryType.subclass,),None))
    def setDefault(*args):
        """
        Sets the default DoubleMatrix type

        Signatures:

        static void setDefault(FactoryType type)

        Arguments:

        type -- One of the DoubleMatrixFactory.FactoryType types
        """
        pass
    ## Gets the FactoryType
    # @return The FactoryType
    @javaOverload("getType",
                  (make_sig([],java_imports['DoubleMatrixFactory']+'$FactoryType'),
                   (),lambda x: Enum(obj=x)))
    def getType(self, *args):
        """
        Gets the FactoryType

        Signatures:

        FactoryType getType()

        Returns:

        The FactoryType
        """
        pass
    ## Produces a DoubleMatrix (5 overloads)
    # @return A DoubleMatrix
    @javaOverload("make",
                  (make_sig(['int','int'],java_imports['DoubleMatrix']),
                   (metaInteger,metaInteger), lambda x: DoubleMatrix(obj=x)),
                  (make_sig(['int','int','double[]'],java_imports['DoubleMatrix']),
                   (metaInteger,metaInteger,meta_double_array),
                   lambda x: DoubleMatrix(obj=x)),
                  (make_sig(['int','int','double[]','boolean'],java_imports['DoubleMatrix']),
                   (metaInteger,metaInteger,meta_double_array,
                    metaBoolean),lambda x: DoubleMatrix(obj=x)),
                  (make_sig(['double[][]'],java_imports['DoubleMatrix']),
                   (javaArray.get_array_type(javaPrimativeArray.get_array_type('double')),),
                    lambda x: DoubleMatrix(obj=x)),
                  (make_sig(['int','int','double'],java_imports['DoubleMatrix']),
                   (metaInteger,metaInteger,metaDouble),lambda x: DoubleMatrix(obj=x)))
    def make(self, *args):
        """
        Produces a DoubleMatrix

        Signatures:

        DoubleMatrix make(int row, int col)
        DoubleMatrix make(int row, int col, double[] values)
        DoubleMatrix make(int row, int col, double[] values, boolean columnMajor)
        DoubleMatrix make(double[][] values)
        DoubleMatrix make(int row, int col, double val)

        Arguments:

        DoubleMatrix make(int row, int col)
            row -- The number of rows in this matrix
            col -- The number of columns in this matrix
        DoubleMatrix make(int row, int col, double[] values)
            row -- The number of rows in this matrix
            col -- The number of columns in this matrix
            values -- The values for the matrix, listed row-wise
        DoubleMatrix make(int row, int col, double[] values, boolean columnMajor)
            row -- The number of rows in this matrix
            col -- The number of columns in this matrix
            values -- The values for the matrix
            columnMajor -- Flag the values as listed column-wise
        DoubleMatrix make(double[][] values)
            values -- Values for matrix in 2D array
        DoubleMatrix make(int row, int col, double val)
            row -- The number of rows in this matrix
            col -- The number of columns in this matrix
            val -- A value to fill the matrix with

        Returns:

        A DoubleMatrix
        """
        pass
    ## Makes an identity matrix
    # @param n The size of the identity matrix
    # @return A DoubleMatrix representing an identity matrix
    @javaOverload("identity",
                  (make_sig(['int'],java_imports['DoubleMatrix']),
                   (metaInteger,),lambda x: DoubleMatrix(obj=x)))
    def identity(self, *args):
        """
        Makes an identity matrix

        Signatures:

        DoubleMatrix identity(int n)

        Arguments:

        n -- The size of the identity matrix

        Returns:

        A DoubleMatrix representing an identity matrix
        """
        pass
    ## Makes a diagonal matrix
    # @param diag Elements for the diagonal of the matrix
    # @return A DoubleMatrix with the specified elements along the diagonal
    @javaOverload("diagonal",
                  (make_sig(['double[]'],java_imports['DoubleMatrix']),
                   (meta_double_array,),
                    lambda x: DoubleMatrix(obj=x)))
    def diagonal(self, *args):
        """
        Makes a diagonal matrix

        Signatures:

        DoubleMatrix diagonal(double[] diag)

        Arguments:

        diag -- The elements for the diagonal of the matrix

        Returns:

        A DoubleMatrix with the specified elements along the diagonal
        """
        pass
    ## Puts together a DoubleMatrix out of multiple matrices
    # @param components 2D array of submatrices to form the matrix
    # @return A DoubleMatrix composed of the submatrices
    @javaOverload("compose",
                  (make_sig([java_imports['DoubleMatrix']+'[][]'],
                            java_imports['DoubleMatrix']),
                  (javaArray.get_array_type(javaArray.get_array_type(DoubleMatrix)),),
                  lambda x: DoubleMatrix(obj=x)))
    def compose(self, *args):
        """
        Puts together a DoubleMatrix out of multiple matrices

        Signatures:

        DoubleMatrix compose(DoubleMatrix[][] components)

        Arguments:

        components -- 2D array of submatrices to form the matrix

        Returns:

        A DoubleMatrix composed of the submatrices
        """
        pass
