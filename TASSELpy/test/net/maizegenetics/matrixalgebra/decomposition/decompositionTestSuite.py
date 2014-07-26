import unittest
from TASSELpy.test.net.maizegenetics.matrixalgebra.decomposition.SingularValueDecompositionTest import SingularValueDecompositionTest
from TASSELpy.test.net.maizegenetics.matrixalgebra.decomposition.EigenvalueDecompositionTest import EigenvalueDecompositionTest
from TASSELpy.TASSELbridge import TASSELbridge

class decompositionTestSuite(unittest.TestSuite):
    def __init__(self):
        super(decompositionTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(SingularValueDecompositionTest))
        self.addTest(unittest.makeSuite(EigenvalueDecompositionTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(decompositionTestSuite())
    TASSELbridge.stop()
