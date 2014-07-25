import unittest
import javabridge
import numpy as np
from TASSELpy.TASSELbridge import TASSELbridge
try:
    try:
        javabridge.get_env()
    except AttributeError:
        TASSELbridge.start()
    except AssertionError:
        TASSELbridge.start()
except:
    raise RuntimeError("Could not start JVM")
from TASSELpy.net.maizegenetics.matrixalgebra.Matrix.DoubleMatrixFactory import DoubleMatrixFactory
from TASSELpy.net.maizegenetics.matrixalgebra.Matrix.DoubleMatrix import DoubleMatrix
from TASSELpy.utils.primativeArray import javaPrimativeArray

debug = False

class DoubleMatrixTest(unittest.TestCase):
    """ Tests for DoubleMatrix """
    def setUp(self):
        # Create a diagonal matrix
        self.factory = DoubleMatrixFactory(DoubleMatrixFactory.FactoryType.ejml)
        vals = javaPrimativeArray.make_array('double',6)
        for i in np.arange(1,7):
            vals[i-1] = np.float64(i)
        self.mat = self.factory.diagonal(vals)
    def test_get(self):
        if debug: print("Testing get")
        self.assertEquals(self.mat.get(0,0),1.)
        self.assertEquals(self.mat.get(0,1),0.)
        with self.assertRaises(javabridge.JavaException):
            self.mat.get(0,7)
    def test_getChecked(self):
        if debug: print("Testing getChecked")
        val1 = self.mat.getChecked(1,1)
        val2 = self.mat[1,1]
        self.assertEqual(val1,val2)
    def test_set(self):
        if debug: print("Testing set")
        self.mat[1,1] = np.float64(3.14)
        self.mat.set(2,2,np.float64(6.28))
        self.assertEquals(self.mat[1,1],3.14)
        self.assertEquals(self.mat[2,2],6.28)
    def test_transpose(self):
        if debug: print("Testing transpose")
        vals = javaPrimativeArray.make_array('double',6)
        for i in np.arange(6):
            vals[i] = np.float64(i)
        mat = self.factory.make(2,3,vals)
        mat_t = mat.transpose()
        self.assertEquals(mat_t.numberOfRows(),3)
        self.assertEquals(mat_t.numberOfColumns(),2)
        self.assertEquals(mat_t[0,1],3.)
    def test_mult(self):
        if debug: print("Testing mult")
        vals = javaPrimativeArray.make_array('double',6)
        for i in np.arange(1,7):
            vals[i-1] = np.float64(i)
        mat2 = self.factory.diagonal(vals)
        mult_mat1 = self.mat.mult(mat2)
        mult_mat2 = self.mat*mat2
        mult_mat3 = mat2*self.mat
        self.assertEquals(mult_mat1[1,1],4.)
        self.assertEquals(mult_mat1[3,3],16.)
        self.assertEquals(mult_mat2[1,1],4.)
        self.assertEquals(mult_mat2[3,3],16.)
        self.assertEquals(mult_mat3[1,1],4.)
        self.assertEquals(mult_mat3[3,3],16.)
    def test_multadd(self):
        if debug: print("Testing multadd")
        test_val = self.mat.multadd(self.factory.identity(6),self.factory.identity(6),
                                 np.float64(1.),np.float64(2.),False,False)
        self.assertEquals(self.mat[1,1]+2., test_val[1,1])
        self.assertEquals(self.mat[0,1], test_val[0,1])
    def test_crossproduct(self):
        if debug: print("Testing crossproduct")
        crossprod1 = self.mat.crossproduct()
        vals = javaPrimativeArray.make_array('double',6)
        for i in np.arange(1,7):
            vals[i-1] = np.float64(i)
        mat2 = self.factory.diagonal(vals)
        crossprod2 = self.mat.crossproduct(mat2)
        self.assertEquals(crossprod1[1,1],4.)
        self.assertEquals(crossprod2[1,1],4.)
    def test_tcrossproduct(self):
        if debug: print("Testing tcrossproduct")
        crossprod1 = self.mat.tcrossproduct()
        vals = javaPrimativeArray.make_array('double',6)
        for i in np.arange(1,7):
            vals[i-1] = np.float64(i)
        mat2 = self.factory.diagonal(vals)
        crossprod2 = self.mat.tcrossproduct(mat2)
        self.assertEquals(crossprod1[1,1],4.)
        self.assertEquals(crossprod2[1,1],4.)
    def test_concatenate(self):
        if debug: print("Testing concatenate")
        concat_mat = self.factory.identity(6)
        concatted1 = self.mat.concatenate(concat_mat,True)
        concatted2 = self.mat.concatenate(concat_mat,False)
        self.assertEquals(concatted1.numberOfRows(),12)
        self.assertEquals(concatted1.numberOfColumns(),6)
        self.assertEquals(concatted2.numberOfRows(),6)
        self.assertEquals(concatted2.numberOfColumns(),12)
    def test_inverse(self):
        if debug: print("Testing inverse")
        inverted = self.mat.inverse()
        self.assertEquals(inverted[1,1],0.5)
        self.assertEquals(inverted[3,3],0.25)
    def test_invert(self):
        if debug: print("Testing invert")
        self.mat.invert()
        self.assertEquals(self.mat[1,1],0.5)
        self.assertEquals(self.mat[3,3],0.25)
    def test_generalizedInverse(self):
        if debug: print("Testing generalizedInverse")
        inverted = self.mat.generalizedInverse()
        self.assertEquals(inverted[1,1],0.5)
        self.assertEquals(inverted[3,3],0.25)
    def test_generalizedInverseWithRank(self):
        if debug: print("Testing generalizedInverseWithRank")
        rank = javaPrimativeArray.make_array('int',2)
        inverted = self.mat.generalizedInverseWithRank(rank)
        self.assertEquals(inverted[1,1],0.5)
        self.assertEquals(inverted[3,3],0.25)
        self.assertEquals(rank[0],6)
    def test_solve(self):
        if debug: print("Testing solve")
        vals = javaPrimativeArray.make_array('double',6)
        for i in np.arange(1,7):
            vals[i-1] = np.float64(i)
        Y = self.factory.make(6,1,vals)
        B = self.mat.solve(Y)
        self.assertEquals(B[0,0],1.)
        self.assertEquals(B[5,0],1.)
    def test_numberOfRowsAndCols(self):
        if debug: print("Testing numberOfRows")
        self.assertEquals(self.mat.numberOfRows(),6)
        self.assertEquals(self.mat.numberOfColumns(),6)
    ###########
    # TODO: Test row method
    ###########
    def test_column(self):
        if debug: print("Testing column")
        col = self.mat.column(1)
        self.assertEquals(col.numberOfRows(),6)
        self.assertEquals(col.numberOfColumns(),1)
        self.assertEquals(col[1,0],2.)
    def test_getXtXGM(self):
        if debug: print("Testing getXtXGM")
        mats = self.mat.getXtXGM()
        self.assertEquals(len(mats),3)
        self.assertEquals(mats[0][1,1],4.)
        self.assertEquals(mats[1][1,1],0.25)
    def test_copy(self):
        if debug: print("Testing copy")
        mat_cp = self.mat.copy()
        self.assertEquals(self.mat[0,0],mat_cp[0,0])
        self.assertEquals(self.mat[3,3],mat_cp[3,3])
    def test_getEigenvalueDecomposition(self):
        if debug: print("Testing getEigenvalueDecomposition")
        eig = self.mat.getEigenvalueDecomposition()
        self.assertIsInstance(eig.o,javabridge.JB_Object)
    def test_getSingularValueDecomposition(self):
        if debug: print("Testing getSingularValueDecomposition")
        svd = self.mat.getSingularValueDecomposition()
        self.assertIsInstance(svd.o,javabridge.JB_Object)
    def test_minus(self):
        if debug: print("Testing minus")
        sub_mat = self.factory.identity(6)
        minus_mat1 = self.mat - sub_mat
        minus_mat2 = sub_mat - self.mat
        minus_mat3 = self.mat.minus(sub_mat)
        self.assertEquals(minus_mat1[2,2],2.)
        self.assertEquals(minus_mat1[2,2],minus_mat3[2,2])
        self.assertEquals(minus_mat2[2,2],-2.)
    def test_minusEquals(self):
        if debug: print("Testing minusEquals")
        sub_mat = self.factory.identity(6)
        self.mat -= sub_mat
        self.assertEquals(self.mat[2,2],2.)
        self.mat.minusEquals(sub_mat)
        self.assertEquals(self.mat[2,2],1.)
    def test_plus(self):
        if debug: print("Testing plus")
        plus_mat = self.factory.identity(6)
        plus_mat1 = self.mat + plus_mat
        plus_mat2 = plus_mat + self.mat
        plus_mat3 = self.mat.plus(plus_mat)
        self.assertEquals(plus_mat1[2,2],4.)
        self.assertEquals(plus_mat1[2,2],plus_mat2[2,2])
        self.assertEquals(plus_mat2[2,2],plus_mat3[2,2])
    def test_plusEquals(self):
        if debug: print("Testing plusEquals")
        plus_mat = self.factory.identity(6)
        self.mat += plus_mat
        self.assertEquals(self.mat[2,2],4.)
        self.mat.plusEquals(plus_mat)
        self.assertEquals(self.mat[2,2],5.)
    def test_scalarAdd(self):
        if debug: print("Testing scalarAdd")
        add_mat1 = self.mat + 1
        self.assertEquals(add_mat1[2,2],4.)
        add_mat2 = 1 + self.mat
        self.assertEquals(add_mat2[2,2],4.)
        add_mat3 = self.mat.scalarAdd(np.float64(1.))
        self.assertEquals(add_mat3[2,2],4.)
    def test_scalarMult(self):
        if debug: print("Testing scalarMult")
        mult_mat1 = self.mat * 2
        mult_mat2 = 2 * self.mat
        mult_mat3 = self.mat.scalarMult(np.float64(2.))
        self.assertEquals(mult_mat1[2,2],6.)
        self.assertEquals(mult_mat2[2,2],6.)
        self.assertEquals(mult_mat3[2,2],6.)
    def test_scalarMultEquals(self):
        if debug: print("Testing scalarMultEquals")
        self.mat *= 2
        self.assertEquals(self.mat[2,2],6.)
        self.mat.scalarMultEquals(np.float64(2.))
        self.assertEquals(self.mat[2,2],12.)
    def test_getSelection(self):
        if debug: print("Testing getSelection")
        rows = javaPrimativeArray.make_array('int',2)
        cols = javaPrimativeArray.make_array('int',2)
        rows[0] = 0
        rows[1] = 1
        cols[0] = 0
        cols[1] = 2
        submat = self.mat.getSelection(rows, cols)
        self.assertEquals(submat[0,0],1.)
        self.assertEquals(submat[1,1],0.)
    def test_rowSum(self):
        if debug: print("Testing rowSum")
        self.assertEquals(self.mat.rowSum(1),2.)
    def test_columnSum(self):
        if debug: print("Testing columnSum")
        self.assertEquals(self.mat.columnSum(1),2.)
    def test_columnRank(self):
        if debug: print("Testing columnRank")
        self.assertEquals(self.mat.columnRank(),6)
if __name__ == "__main__":
    debug = True
    unittest.main(exit = False)
    TASSELbridge.stop()
