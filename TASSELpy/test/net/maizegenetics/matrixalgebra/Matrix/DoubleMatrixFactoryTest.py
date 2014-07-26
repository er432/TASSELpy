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

class DoubleMatrixFactoryTest(unittest.TestCase):
    """ Tests for DoubleMatrixFactory """
    def setUp(self):
        # Test constructor
        self.factory = DoubleMatrixFactory(DoubleMatrixFactory.FactoryType.ejml)
    def test_getType(self):
        if debug: print("Testing getType")
        self.assertEqual(self.factory.getType(), DoubleMatrixFactory.FactoryType.ejml)
    def test_make(self):
        if debug: print("Testing make")
        # make 1
        mat = self.factory.make(5,4)
        self.assertIsInstance(mat,DoubleMatrix)
        self.assertEquals(mat.numberOfRows(), 5)
        self.assertEquals(mat.numberOfColumns(), 4)
        # make 2
        vals = javaPrimativeArray.make_array('double',6)
        for i in np.arange(6):
            vals[i] = np.float64(i)
        mat = self.factory.make(2,3,vals)
        self.assertIsInstance(mat,DoubleMatrix)
        self.assertEquals(mat.numberOfRows(),2)
        self.assertEquals(mat.numberOfColumns(),3)
        self.assertEqual(mat[0,1],1.)
        self.assertEqual(mat[1,0],3.)
        # make 3
        mat = self.factory.make(2,3,vals,True)
        self.assertIsInstance(mat,DoubleMatrix)
        self.assertEquals(mat.numberOfRows(),2)
        self.assertEquals(mat.numberOfColumns(),3)
        self.assertEqual(mat[0,1],2.)
        self.assertEqual(mat[1,0],1.)
        # make 4
        vals_2d = javaPrimativeArray.make_dbl_array('double',2,3)
        vals_2d[0][1] = np.float64(2.)
        vals_2d[1][0] = np.float64(4.)
        mat = self.factory.make(vals_2d)
        self.assertIsInstance(mat,DoubleMatrix)
        self.assertEquals(mat.numberOfRows(),2)
        self.assertEquals(mat.numberOfColumns(),3)
        self.assertEqual(mat[0,1],2.)
        self.assertEqual(mat[1,0],4.)
        # make 5
        mat = self.factory.make(2,3,np.float64(3.14))
        self.assertIsInstance(mat,DoubleMatrix)
        self.assertEquals(mat.numberOfRows(),2)
        self.assertEquals(mat.numberOfColumns(),3)
        self.assertEqual(mat[0,0],3.14)
        self.assertEqual(mat[0,1],3.14)
    def test_identity(self):
        if debug: print("Testing identity")
        mat = self.factory.identity(3)
        self.assertIsInstance(mat,DoubleMatrix)
        self.assertEquals(mat.numberOfRows(),3)
        self.assertEquals(mat.numberOfColumns(),3)
        self.assertEquals(mat[0,0],1.)
        self.assertEquals(mat[0,1],0.)
    def test_diagonal(self):
        if debug: print("Testing diagonal")
        vals = javaPrimativeArray.make_array('double',6)
        for i in np.arange(6):
            vals[i] = np.float64(i)
        mat = self.factory.diagonal(vals)
        self.assertEquals(mat.numberOfRows(),6)
        self.assertEquals(mat.numberOfColumns(),6)
        self.assertEquals(mat[0,0],0.)
        self.assertEquals(mat[2,2],2.)
        self.assertEquals(mat[2,3],0.)
    def test_compose(self):
        if debug: print("Testing compose")
        mat1 = self.factory.identity(2)
        mat2 = self.factory.identity(2)
        dblMatArr = DoubleMatrix.getDblArray(1,2)
        dblMatArr[0][0] = mat1
        dblMatArr[0][1] = mat2
        composed = self.factory.compose(dblMatArr)
        self.assertIsInstance(composed,DoubleMatrix)
        self.assertEquals(composed.numberOfRows(),2)
        self.assertEquals(composed.numberOfColumns(),4)
        self.assertEquals(composed[0,0],1.)
        self.assertEquals(composed[0,1],0.)
        self.assertEquals(composed[0,2],1.)
        
if __name__ == "__main__":
    debug = True
    unittest.main(exit = False)
    TASSELbridge.stop()
