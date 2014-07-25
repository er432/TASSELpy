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

class EigenvalueDecompositionTest(unittest.TestCase):
    """ Tests for EigenvalueDecomposition """
    def setUp(self):
        self.factory = DoubleMatrixFactory(DoubleMatrixFactory.FactoryType.ejml)
        self.mat = self.factory.diagonal(np.arange(1,7))
        self.eig = self.mat.getEigenvalueDecomposition()
    def test_getEigenvalues(self):
        if debug: print("Testing getEigenvalues")
        eigvals = self.eig.getEigenvalues()
        self.assertIsInstance(eigvals, meta_double_array)
        self.assertEquals(eigvals[0],1.)
        self.assertEquals(eigvals[1],2.)
    def test_getEigenvalue(self):
        if debug: print("Testing getEigenvalue")
        self.assertEquals(self.eig.getEigenvalue(0),1.)
        self.assertEquals(self.eig.getEigenvalue(1),2.)
    def test_getEigenvectors(self):
        if debug: print("Testing getEigenvectors")
        evecs = self.eig.getEigenvectors()
        self.assertIsInstance(evecs, DoubleMatrix)
        self.assertEquals(evecs[0,0],1.)
        self.assertEquals(evecs[0,1],0.)
        self.assertEquals(evecs[1,1],1.)
    def test_getEigenvalueMatrix(self):
        if debug: print("Testing getEigenvalueMatrix")
        evals = self.eig.getEigenvalueMatrix()
        self.assertIsInstance(evals, DoubleMatrix)
        self.assertEquals(evals[0,0],1.)
        self.assertEquals(evals[1,1],2.)
if __name__ == "__main__":
    debug = True
    unittest.main(exit = False)
    TASSELbridge.stop()
