from TASSELpy.java.lang.Object import Object
import TASSELpy.net.maizegenetics.matrixalgebra.decomposition.EigenvalueDecomposition
import TASSELpy.net.maizegenetics.matrixalgebra.decomposition.SingularValueDecomposition
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Number import metaNumber
from TASSELpy.utils.primativeArray import javaPrimativeArray, meta_int_array
from abc import ABCMeta
import numpy as np

java_imports = {'DoubleMatrix':'net/maizegenetics/matrixalgebra/Matrix/DoubleMatrix',
                'EigenvalueDecomposition':'net/maizegenetics/matrixalgebra/decomposition/EigenvalueDecomposition',
                'SingularValueDecomposition': 'net/maizegenetics/matrixalgebra/decomposition/SingularValueDecomposition'}

class metaDoubleMatrix:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C, DoubleMatrix):
            return True
        else:
            return False

class DoubleMatrix(Object):
    """
    Wrapper for the DoubleMatrix interface, which is implemented by several classes
    that call native methods
    """
    _java_name = java_imports['DoubleMatrix']
    @javaConstructorOverload(java_imports['DoubleMatrix'])
    def __init__(self, *args, **kwargs):
        pass
    ############
    # Python magic methods
    ############
    def __getitem__(self, key):
        if type(key) != tuple:
            raise KeyError("Must specify particular cell")
        return self.getChecked(*key)
    def __setitem__(self, key, value):
        if type(key) != tuple:
            raise KeyError("Must specify particular cell")
        self.setChecked(key[0],key[1],value)
    def __len__(self):
        return self.numberOfRows()
    def __repr__(self):
        return "%d x %d Matrix" % (self.numberOfRows(), self.numberOfColumns())
    def __add__(self, other):
        if isinstance(other, metaNumber):
            return self.scalarAdd(np.float64(other))
        elif isinstance(other, DoubleMatrix):
            return self.plus(other)
        else:
            raise TypeError("Unsupported operand type(s)")
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        if isinstance(other, metaNumber):
            return self.__add__(other)
        elif isinstance(other, DoubleMatrix):
            self.plusEquals(other)
            return self
        else:
            raise TypeError("Unsupported operand type(s)")
    def __sub__(self, other):
        if isinstance(other, metaNumber):
            return self.__add__(np.float64(-other))
        elif isinstance(other, DoubleMatrix):
            return self.minus(other)
        else:
            raise TypeError("Unsupported operand type(s)")
    def __rsub__(self, other):
        if isinstance(other, metaNumber):
            return self.__add__(self.__mul__(-1),other)
        elif isinstance(other, DoubleMatrix):
            return -self + other
        else:
            raise TypeError("Unsupported operand type(s)")
    def __isub__(self, other):
        if isinstance(other, metaNumber):
            return self.__sub__(other)
        elif isinstance(other, DoubleMatrix):
            self.minusEquals(other)
            return self
        else:
            raise TypeError("Unsupported operand type(s)")
    def __mul__(self, other):
        if isinstance(other, metaNumber):
            return self.scalarMult(np.float64(other))
        elif isinstance(other, DoubleMatrix):
            return self.mult(other)
        else:
            raise TypeError("Unsupported operand type(s)")
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        if isinstance(other, metaNumber):
            self.scalarMultEquals(np.float64(other))
            return self
        elif isinstance(other, DoubleMatrix):
            return self.__mul__(other)
        else:
            raise TypeError("Unsupported operand type(s)")
    ## Gets data and doesn't check to make sure they are in the matrix
    # @param row The zero-based row index
    # @param col The zero-based column index
    # @return The value at row, col
    @javaOverload("get",
                  (make_sig(['int','int'],'double'),(metaInteger,metaInteger),
                   np.float64))
    def get(self, *args):
        """
        Gets data and doesn't check to make sure they are in the matrix

        Signatures:

        double get(int row, int col)

        Arguments:

        row -- The zero-based row index
        col -- The zero-based column index

        Returns:

        The value at row, col
        """
        pass
    ## Gets data and checks to make sure they are in the matrix
    # @param row The zero-based row index
    # @param col The zero-based column index
    # @return The value at row, col
    @javaOverload("getChecked",
                  (make_sig(['int','int'],'double'),(metaInteger,metaInteger),
                   np.float64))
    def getChecked(self, *args):
        """
        Gets data and checks to make sure they are in the matrix

        Signatures:

        double getChecked(int row, int col)

        Arguments:

        row -- The zero-based row index
        col -- The zero-based column index

        Returns:

        The value at row, col
        """
        pass
    ## Sets the matrix value at row, col. The coordinates are not checked to make
    # sure they fall in the matrix
    # @param row The zero-based row index
    # @param col The zero-based column index
    # @param value The value to be set at row, col
    @javaOverload("set",
                  (make_sig(['int','int','double'],'void'),(metaInteger,metaInteger,metaDouble),
                   None))
    def set(self, *args):
        """
        Sets the matrix value at row, col. The coordinates are not checked to make
        sure they fall in the matrix

        Signatures:

        void set(int row, int col, double value)

        Arguments:

        row -- The zero-based row index
        col -- The zero-based column index
        value -- The value to be set at row, col
        """
        pass
    ## Sets the matrix value at row, col. The coordinates are checked to make
    # sure they fall in the matrix
    # @param row The zero-based row index
    # @param col The zero-based column index
    # @param value The value to be set at row, col
    @javaOverload("setChecked",
                  (make_sig(['int','int','double'],'void'),(metaInteger,metaInteger,metaDouble),
                   None))
    def setChecked(self, *args):
        """
        Sets the matrix value at row, col. The coordinates are checked to make
        sure they fall in the matrix

        Signatures:

        void setChecked(int row, int col, double value)

        Arguments:

        row -- The zero-based row index
        col -- The zero-based column index
        value -- The value to be set at row, col
        """
        pass
    ## Gets the tranpose of this matrix
    # @return The transpose of this matrix
    @javaOverload("transpose",
                  (make_sig([],java_imports['DoubleMatrix']),(),
                   lambda x: DoubleMatrix(obj=x)))
    def transpose(self, *args):
        """
        Gets the tranpose of this matrix

        Signatures:

        DoubleMatrix transpose()

        Returns:

        The transpose of this matrix
        """
        pass
    ## Multiply this matrix times another
    # @param dm A double matrix
    # @param transpose If true, this matrix will be transposed before multiplying
    # @param transposedm If ture, dm will be transposed before multiplying
    # @return The multiplied matrix
    @javaOverload("mult",
                  (make_sig([java_imports['DoubleMatrix'],'boolean','boolean'],
                            java_imports['DoubleMatrix']),(metaDoubleMatrix,metaBoolean,
                            metaBoolean),lambda x: DoubleMatrix(obj=x)),
                  (make_sig([java_imports['DoubleMatrix']],java_imports['DoubleMatrix']),
                   (metaDoubleMatrix,),lambda x: DoubleMatrix(obj=x)))
    def mult(self, *args):
        """
        Multiply this matrix times another

        Signatures:

        DoubleMatrix mult(DoubleMatrix dm, boolean transpose, boolean transposedm)
        DoubleMatrix mult(DoubleMatrix dm)

        Arguments:

        DoubleMatrix mult(DoubleMatrix dm, boolean transpose, boolean transposedm)
            dm -- A double matrix
            transpose -- If true, this matrix will be transposed before multiplying
            transposedm -- If true, dm will be transposed before multiplying
        DoubleMatrix mult(DoubleMatrix dm)
            dm -- A double matrix

        Returns:

        The multiplied matrix
        """
        pass
    ## Using this function for combining multiplication and addition allows the implementing
    # library to optimize the operations
    # @param A The matrix to be multiplied
    # @param B The matrix to be added, can be null
    # @param alpha -- scalar multiplier for A
    # @param beta scalar multiplier for B
    # @param transpose -- If true, X is transposed
    # @param transposeA - If true, A is transposed
    # @param transposeB -- If true, B is transposed
    # @return alpha*XA+beta*B where X is this matrix
    @javaOverload("multadd",
                  (make_sig([java_imports['DoubleMatrix'],java_imports['DoubleMatrix'],
                             'double','double','boolean','boolean'],
                             java_imports['DoubleMatrix']),
                  (metaDoubleMatrix,metaDoubleMatrix,metaDouble,metaDouble,
                   metaBoolean,metaBoolean),
                  lambda x: DoubleMatrix(obj=x)))
    def multadd(self, *args):
        """
        Using this function for combining multiplication and addition allows the
        implementing library to optimize the operations

        Signatures:

        DoubleMatrix multadd(DoubleMatrix A, DoubleMatrix B, double alpha, double beta,
                             boolean transpose, boolean transposeA)

        Arguments:

        A -- The matrix to be multiplied
        B -- The matrix to be added, can be null
        alpha -- scalar multiplier for A
        beta -- scalar multiplier for B
        transpose -- If true, X is transposed
        transposeA -- If true, A is transposed
        transposeB -- If true, B is transposed
        
        Returns:

        alpha*XA+beta*B where X is this matrix
        """
        pass
    ## Gets X'x or X'dm, where X is this matrix
    # @param dm The second matrix
    # @return The cross product
    @javaOverload("crossproduct",
                  (make_sig([],java_imports['DoubleMatrix']),(),
                   lambda x: DoubleMatrix(obj=x)),
                  (make_sig([java_imports['DoubleMatrix']],java_imports['DoubleMatrix']),
                   (metaDoubleMatrix,),lambda x: DoubleMatrix(obj=x)))
    def crossproduct(self, *args):
        """
        Get X'X or X'dm, where X is this matrix

        Signatures:

        DoubleMatrix crossproduct()
        DoubleMatrix crossproduct(DoubleMatrix dm)

        Arguments:

        DoubleMatrix crossproduct(DoubleMatrix dm)
            dm -- The second matrix

        Returns:

        The cross product
        """
        pass
    ## Gets XX' or Xdm', where X is this matrix
    # @param dm The second matrix
    # @return The tcrossproduct
    @javaOverload("tcrossproduct",
                  (make_sig([],java_imports['DoubleMatrix']),(),
                   lambda x: DoubleMatrix(obj=x)),
                  (make_sig([java_imports['DoubleMatrix']],java_imports['DoubleMatrix']),
                   (metaDoubleMatrix,),lambda x: DoubleMatrix(obj=x)))
    def tcrossproduct(self, *args):
        """
        Gets XX' or Xdm', where X is this matrix

        Signatures:

        DoubleMatrix tcrossproduct()
        DoubleMatrix tcrossproduct(DoubleMatrix dm)

        Arguments:

        DoubleMatrix tcrossproduct(DoubleMatrix dm)
            dm -- The second matrix

        Returns:

        The tcrossproduct
        """
        pass
    ## Puts two matrices together
    # @param dm A DoubleMatrix
    # @param rows true if rows are to be concatenated, false if columns are to be concatenated
    # @return X with dm appended, where X is this matrix
    @javaOverload("concatenate",
                  (make_sig([java_imports['DoubleMatrix'],'boolean'],
                            java_imports['DoubleMatrix']),
                            (metaDoubleMatrix,metaBoolean),
                            lambda x: DoubleMatrix(obj=x)))
    def concatenate(self, *args):
        """
        Puts two matrices together

        Signatures:

        DoubleMatrix concatenate(DoubleMatrix dm, boolean rows)

        Arguments:

        dm -- a DoubleMatrix
        rows -- true if rows are to be concatenated, false if columns are to be concatenated

        Returns:

        Returns X with dm appended, where X is this matrix
        """
        pass
    ## Returns the inverse of a square matrix, without modifying the original matrix
    # @return The inverse of a square matrix if it is non-singular, null otherwise
    @javaOverload("inverse",
                  (make_sig([],java_imports['DoubleMatrix']),(),
                   lambda x: DoubleMatrix(obj=x)))
    def inverse(self, *args):
        """
        Returns the inverse of a square matrix, without modifying the original matrix.

        Signatures:

        DoubleMatrix inverse()

        Returns:

        The inverse of a square matrix if it is non-singular, null otherwise
        """
        pass
    ## Inverts a square matrix, replacing the original with the inverse
    @javaOverload("invert",
                  (make_sig([],'void'),(),None))
    def invert(self, *args):
        """
        This inverts a square matrix, replacing the original with the inverse

        Signatures:

        void invert()
        """
        pass
    @javaOverload("generalizedInverse",
                  (make_sig([],java_imports['DoubleMatrix']),(),
                   lambda x: DoubleMatrix(obj=x)))
    def generalizedInverse(self, *args):
        """
        Gets the generalized inverse of a square matrix

        Signatures:

        DoubleMatrix generalizedInverse()

        Returns:

        The generalized inverse of a square matrix
        """
        pass
    ## Inverts the matrix and returns the rank as the first element in rank[]. The
    # original matrix is not modified
    # @param rank Array to hold element where rank will be stored
    # @return A generalized inverse of this matrix
    @javaOverload("generalizedInverseWithRank",
                  (make_sig(['int[]'],java_imports['DoubleMatrix']),
                   (meta_int_array,),
                  lambda x: DoubleMatrix(obj=x)))
    def generalizedInverseWithRank(self, *args):
        """
        Inverts the matrix and returns the rank as the first element in rank[]. The
        original matrix is not modified

        Signatures:

        DoubleMatrix generalizedInverseWithRank(int[] rank)

        Arguments:

        rank -- Array to hold element where rank will be stored

        Returns:

        A generalized inverse of this matrix
        """
        pass
    ## Solves the matrix
    # @param Y a DoubleMatrix
    # @return The least squares solutions for B, where XB=Y and X is this matrix
    @javaOverload("solve",
                  (make_sig([java_imports['DoubleMatrix']],java_imports['DoubleMatrix']),
                   (metaDoubleMatrix,),lambda x: DoubleMatrix(obj=x)))
    def solve(self, *args):
        """
        Solves the matrix

        Signatures:

        DoubleMatrix solve(DoubleMatrix Y)

        Arguments:

        Y -- a DoubleMatrix

        Returns:

        The least squares solutions for B, where XB = Y and X is this matrix
        """
        pass
    ## Gets the number of rows in this matrix
    # @return Number of rows in this matrix
    @javaOverload("numberOfRows",
                  (make_sig([],'int'),(),None))
    def numberOfRows(self, *args):
        """
        Gets the number of rows in this matrix

        Signatures:

        int numberOfRows()

        Returns:

        Number of rows in this matrix
        """
        pass
    ## Gets the number of columns in this matrix
    # @return Number of columns in this matrix
    @javaOverload("numberOfColumns",
                  (make_sig([],'int'),(),None))
    def numberOfColumns(self, *args):
        """
        Gets the number of columns in this matrix

        Signatures:

        int numberOfColumns()

        Returns:

        Number of columns in this matrix
        """
        pass
    ## Gets the row of the matrix as a column vector
    # @param i a row index
    # @return The ith row of this matrix as a column vector
    @javaOverload("row",
                  (make_sig(['int'],java_imports['DoubleMatrix']),(metaInteger,),
                   lambda x: DoubleMatrix(obj=x)))
    def row(self, *args):
        """
        Gets the row of the matrix as a row vector

        Signatures:

        DoubleMatrix row(int i)

        Arguments:

        i -- a row index

        Returns:

        The ith row of this matrix as a column vector
        """
        pass
    ## Gets the column of the matrix as a column vector
    # @param j A column index
    # @return The jth row of this matrix as a column vector
    @javaOverload("column",
                  (make_sig(['int'],java_imports['DoubleMatrix']),(metaInteger,),
                   lambda x: DoubleMatrix(obj=x)))
    def column(self, *args):
        """
        Gets the column of the matrix as a column vector

        Signatures:

        DoubleMatrix column(int j)

        Arguments:

        j -- A column index

        Returns:

        The jth row of this matrix as a column vector
        """
        pass
    ## Gets an array of three DoubleMatrices. Where X is this matrix, the first is
    # X'X, the second is the inverse of X'X, and the third is I-XGX'
    # @return Array of three DoubleMatrices. Where X is this matrix, the first is X'X,
    # the second is inverse of X'X, and the third is I-XGX'
    @javaOverload("getXtXGM",
                  (make_sig([],java_imports['DoubleMatrix']+'[]'),(),
                   lambda x: DoubleMatrix.wrap_existing_array(x)))
    def getXtXGM(self, *args):
        """
        Gets an array of three DoubleMatrices. Where X is this matrix, the first is
        X'X, the second is the inverse of X'X, and the third is I-XGX'

        Signatures:

        DoubleMatrix[] getXtXGM()

        Returns:

        An array of three DoubleMatrices. Where X is this matrix, the first is X'X,
        the second is the inverse of X'X, and the third is I-XGX'
        """
        pass
    ## Gets a copy of the matrix
    # @return A copy of the matrix
    @javaOverload("copy",
                  (make_sig([],java_imports['DoubleMatrix']),(),
                   lambda x: DoubleMatrix(obj=x)))
    def copy(self, *args):
        """
        Gets a copy of the matrix

        Signatures:

        DoubleMatrix copy()

        Returns:

        A copy of the matrix
        """
        pass
    ## Gets the eigenvalue decomposition of this matrix
    # @return An eigenvalue decomposition of this matrix
    @javaOverload("getEigenvalueDecomposition",
                  (make_sig([],java_imports['EigenvalueDecomposition']),
                   (),lambda x: TASSELpy.net.maizegenetics.matrixalgebra.\
                              decomposition.EigenvalueDecomposition.\
                              EigenvalueDecomposition(obj=x)))
    def getEigenvalueDecomposition(self, *args):
        """
        Gets the Eigenvalue decomposition of this matrix

        Signatures:

        EigenvalueDecomposition getEigenvalueDecomposition()

        Returns:

        An Eigenvalue Decomposition of this matrix
        """
        pass
    ## Gets the singular value decomposition of this matrix
    # @return An singular value decomposition of this matrix
    @javaOverload("getSingularValueDecomposition",
                  (make_sig([],java_imports['SingularValueDecomposition']),
                   (),lambda x: TASSELpy.net.maizegenetics.matrixalgebra.\
                              decomposition.SingularValueDecomposition.\
                              SingularValueDecomposition(obj=x)))
    def getSingularValueDecomposition(self, *args):
        """
        Gets the Singular Value decomposition of this matrix

        Signatures:

        SingularValueDecomposition getSingularValueDecomposition()

        Returns:

        An Singular Value Decomposition of this matrix
        """
        pass
    ## Subtracts a matrix from this matrix, X, without modifying X
    # @param dm A DoubleMatrix to subtract
    # @return A new DoubleMatrix created by subtracting dm from this matrix
    @javaOverload("minus",
                  (make_sig([java_imports['DoubleMatrix']],java_imports['DoubleMatrix']),
                   (metaDoubleMatrix,),lambda x: DoubleMatrix(obj=x)))
    def minus(self, *args):
        """
        Subtracts a matrix from this matrix, X, without modifying X

        Signatures:

        DoubleMatrix minus(DoubleMatrix dm)

        Arguments:

        dm -- A DoubleMatrix to subtract

        Returns:

        A new DoubleMatrix created by subtracting dm from this matrix
        """
        pass
    ## This function subtracts dm, modifying the original matrix
    # @param dm A DoubleMatrix to subtract
    @javaOverload("minusEquals",
                  (make_sig([java_imports['DoubleMatrix']],'void'),
                   (metaDoubleMatrix,),None))
    def minusEquals(self, *args):
        """
        This function subtracts dm, modifying the original matrix

        Signatures:

        void minusEquals(DoubleMatrix dm)

        Arguments:

        dm -- A DoubleMatrix to subtract
        """
        pass
    ## Adds a matrix from this matrix, X, without modifying X
    # @param dm A DoubleMatrix to add
    # @return A new DoubleMatrix created by adding dm from this matrix
    @javaOverload("plus",
                  (make_sig([java_imports['DoubleMatrix']],java_imports['DoubleMatrix']),
                   (metaDoubleMatrix,),lambda x: DoubleMatrix(obj=x)))
    def plus(self, *args):
        """
        Adds a matrix from this matrix, X, without modifying X

        Signatures:

        DoubleMatrix plus(DoubleMatrix dm)

        Arguments:

        dm -- A DoubleMatrix to add

        Returns:

        A new DoubleMatrix created by adding dm from this matrix
        """
        pass
    ## This function adds dm, modifying the original matrix
    # @param dm A DoubleMatrix to add
    @javaOverload("plusEquals",
                  (make_sig([java_imports['DoubleMatrix']],'void'),
                   (metaDoubleMatrix,),None))
    def plusEquals(self, *args):
        """
        This function adds dm, modifying the original matrix

        Signatures:

        void plusEquals(DoubleMatrix dm)

        Arguments:

        dm -- A DoubleMatrix to add
        """
        pass
    ## Adds a scalar to this matrix and returns a new matrix. The original is
    # not modified
    # @param s A scalar
    # @return The sum of this matrix and a scalar s
    @javaOverload("scalarAdd",
                  (make_sig(['double'],java_imports['DoubleMatrix']),
                   (metaDouble,),lambda x: DoubleMatrix(obj=x)))
    def scalarAdd(self, *args):
        """
        Adds a scalar to this matrix and returns a new matrix. The original is
        not modified

        Signatures:

        DoubleMatrix scalarAdd(double s)

        Arguments:

        s -- a scalar

        Returns:

        The sum of this matrix and a scalar s
        """
        pass
    ## Adds a scalar s to this matrix, replacing the original matrix with the result
    # @param s A scalar
    @javaOverload("scalarAddEquals",
                  (make_sig(['double'],'void'),(metaDouble,),None))
    def scalarAddEquals(self, *args):
        """
        Adds a scalar s to this matrix, replacing the original matrix with the result

        Signatures:

        void scalarAddEquals(double s)

        Arguments:

        s -- a scalar
        """
        pass
    ## Multiplies a scalar with this matrix and returns a new matrix. The original is
    # not modified
    # @param s A scalar
    # @return The sum of this matrix and a scalar s
    @javaOverload("scalarMult",
                  (make_sig(['double'],java_imports['DoubleMatrix']),
                   (metaDouble,),lambda x: DoubleMatrix(obj=x)))
    def scalarMult(self, *args):
        """
        Multiplies a scalar to this matrix and returns a new matrix. The original is
        not modified

        Signatures:

        DoubleMatrix scalarMult(double s)

        Arguments:

        s -- a scalar

        Returns:

        The sum of this matrix and a scalar s
        """
        pass
    ## Multiplies a scalar s with this matrix, replacing the original matrix with the result
    # @param s A scalar
    @javaOverload("scalarMultEquals",
                  (make_sig(['double'],'void'),(metaDouble,),None))
    def scalarMultEquals(self, *args):
        """
        Multiplies a scalar s to this matrix, replacing the original matrix with the result

        Signatures:

        void scalarMultEquals(double s)

        Arguments:

        s -- a scalar
        """
        pass
    ## Creates a new  matrix consisting of the rows and columns of this matrix in the
    # order specified. If rows or columns is null, then all rows or columns, respectively,
    # will be included
    # @param rows The rows to be included in the new matrix
    # @param columns The columns to be included in the new matrix
    # @return A new matrix consisting of the specified rows and columns
    @javaOverload("getSelection",
                  (make_sig(['int[]','int[]'],java_imports['DoubleMatrix']),
                   (meta_int_array, meta_int_array),
                  lambda x: DoubleMatrix(obj=x)))
    def getSelection(self, *args):
        """
        Creates a new matrix consisting of the rows and columns of this matrix in the
        order specified. If rows or columns is null, then all rows or columns, respectively,
        will be included

        Signatures:

        DoubleMatrix getSelection(int[] rows, int[] columns)

        Arguments:

        rows -- The rows to be included in the new matrix
        columns -- The columns to be included in the new matrix

        Returns:

        A new matrix consisting of the specified rows and columns
        """
        pass
    ## Sums a row
    # @param row The index of the row to sum
    # @return The sum of the elements in this row
    @javaOverload("rowSum",
                  (make_sig(['int'],'double'),(metaInteger,),np.float64))
    def rowSum(self, *args):
        """
        Sums a row

        Signatures:

        double rowSum(int row)

        Arguments:

        row -- The row index to sum

        Returns:

        The sum of the elements in this row
        """
        pass
    ## Sums a column
    # @param column The index of the column to sum
    # @return The sum of the elements in this column
    @javaOverload("columnSum",
                  (make_sig(['int'],'double'),(metaInteger,),np.float64))
    def columnSum(self, *args):
        """
        Sums a column

        Signatures:

        double columnSum(int column)

        Arguments:

        column -- The column index to sum

        Returns:

        The sum of the elements in this column
        """
        pass
    ## Gets the column rank of this matrix
    # @return The column rank of this matrix
    @javaOverload("columnRank",
                  (make_sig([],'int'),(),None))
    def columnRank(self, *args):
        """
        Gets the column rank of this matrix

        Signatures:

        int columnRank()

        Returns:

        The column rank of this matrix
        """
        pass
