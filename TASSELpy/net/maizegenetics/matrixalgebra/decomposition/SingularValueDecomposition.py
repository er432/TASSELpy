from TASSELpy.java.lang.Object import Object
import TASSELpy.net.maizegenetics.matrixalgebra.Matrix.DoubleMatrix
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.java.lang.Boolean import metaBoolean

java_imports = {'DoubleMatrix': 'net/maizegenetics/matrixalgebra/Matrix/DoubleMatrix',
                'SingularValueDecomposition':'net/maizegenetics/matrixalgebra/decomposition/SingularValueDecomposition'}

class SingularValueDecomposition(Object):
    _java_name = java_imports['SingularValueDecomposition']
    @javaConstructorOverload(java_imports['SingularValueDecomposition'])
    def __init__(self, *args, **kwargs):
        pass
    ## Gets U for the decomposition of A, where A = USV'
    # @param transpose Whether to transpose U
    # @return U (orthogonal)
    @javaOverload("getU",
                  (make_sig(['boolean'],java_imports['DoubleMatrix']),
                   (metaBoolean,),lambda x: TASSELpy.net.maizegenetics.matrixalgebra.\
                                            Matrix.DoubleMatrix.DoubleMatrix(obj=x)))
    def getU(self, *args):
        """
        Gets U for the decomopsition of A, where A = USV'

        Signatures:

        DoubleMatrix getU(boolean transpose)

        Arguments:

        transpose -- Whether to transpose U
        
        Returns:

        U (orthogonal)
        """
        pass
    ## Gets V for the decomposition of A, where A = USV'
    # @param transpose Whether to transpose V
    # @return V (orthogonal)
    @javaOverload("getV",
                  (make_sig(['boolean'],java_imports['DoubleMatrix']),
                   (metaBoolean,),lambda x: TASSELpy.net.maizegenetics.matrixalgebra.\
                                            Matrix.DoubleMatrix.DoubleMatrix(obj=x)))
    def getV(self, *args):
        """
        Gets V for the decomopsition of A, where A = VSV'

        Signatures:

        DoubleMatrix getV(boolean transpose)

        Arguments:

        transpose -- Whether to transpose V
        
        Returns:

        V (orthogonal)
        """
        pass
    ## Gets S for the decomposition of A, where A = USV'
    # @return S, the diagonal matrix of signular values
    @javaOverload("getS",
                  (make_sig([],java_imports['DoubleMatrix']),
                   (),lambda x: TASSELpy.net.maizegenetics.matrixalgebra.\
                                            Matrix.DoubleMatrix.DoubleMatrix(obj=x)))
    def getS(self, *args):
        """
        Gets S for the decomopsition of A, where A = VSV'

        Signatures:

        DoubleMatrix getV(boolean transpose)

        Returns:

        S, the diagonal matrix of singular values
        """
        pass
    ## Gets the singular values for the SVD of A, A = USV'
    # @return The singular values equal to the diagonal of S
    @javaOverload("getSingularValues",
                  (make_sig([],'double[]'),(),
                   lambda x: javaPrimativeArray.make_array_from_obj('double',x)))
    def getSingularValues(self, *args):
        """
        Gets the singular values for the SVD of A, A = USV'

        Signatures:

        double[] getSingularValues()

        Returns:

        The singular values equal to the diagonal of S
        """
        pass
    ## Gets the rank of the matrix that was decomposed
    # @return The rnak of the matrix that was decomposed
    @javaOverload("getRank",
                  (make_sig([],'int'),(),None))
    def getRank(self, *args):
        """
        Gets the rank of the matrix that was decomposed

        Signatures:

        int getRank()

        Returns:

        The rank of the matrix that was decomposed
        """
        pass
