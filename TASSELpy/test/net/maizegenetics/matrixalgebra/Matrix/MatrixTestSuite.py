import unittest
from TASSELpy.test.net.maizegenetics.matrixalgebra.Matrix.DoubleMatrixFactoryTest import DoubleMatrixFactoryTest
from TASSELpy.test.net.maizegenetics.matrixalgebra.Matrix.DoubleMatrixTest import DoubleMatrixTest
from TASSELpy.TASSELbridge import TASSELbridge

class MatrixTestSuite(unittest.TestSuite):
    def __init__(self):
        super(MatrixTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(DoubleMatrixFactoryTest))
        self.addTest(unittest.makeSuite(DoubleMatrixTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(MatrixTestSuite())
    TASSELbridge.stop()
