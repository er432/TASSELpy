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
from TASSELpy.utils.primativeArray import meta_double_array

debug = False

class SingularValueDecompositionTest(unittest.TestCase):
    """ Tests for SingularValueDecomposition """
    def setUp(self):
        self.factory = DoubleMatrixFactory(DoubleMatrixFactory.FactoryType.ejml)
        self.mat = self.factory.diagonal(np.arange(1,7))
        self.svd = self.mat.getSingularValueDecomposition()
    def test_getU(self):
        if debug: print("Testing getU")
        U = self.svd.getU(False)
        self.assertIsInstance(U, DoubleMatrix)
        self.assertEquals(U[0,0],1.)
        self.assertEquals(U[1,1],1.)
        self.assertEquals(U[0,1],0.)
    def test_getV(self):
        if debug: print("Testing getV")
        V = self.svd.getV(False)
        self.assertIsInstance(V, DoubleMatrix)
        self.assertEquals(V[0,0],1.)
        self.assertEquals(V[1,1],1.)
        self.assertEquals(V[0,1],0.)
    def test_getS(self):
        if debug: print("Testing getS")
        S = self.svd.getS()
        self.assertIsInstance(S, DoubleMatrix)
        self.assertEquals(S[0,0],1.)
        self.assertEquals(S[1,1],2.)
    def test_getSingularValues(self):
        if debug: print("Testing getSingularValues")
        singular_vals = self.svd.getSingularValues()
        self.assertIsInstance(singular_vals, meta_double_array)
        self.assertEquals(singular_vals[0],1.)
        self.assertEquals(singular_vals[1],2.)
    def test_getRank(self):
        if debug: print("Testing getRank")
        self.assertEquals(self.svd.getRank(),6)
if __name__ == "__main__":
    debug = True
    unittest.main(exit = False)
    TASSELbridge.stop()
