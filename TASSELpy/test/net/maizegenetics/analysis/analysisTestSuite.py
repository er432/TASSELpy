import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.net.maizegenetics.analysis.IBSDistanceMatrixTest import IBSDistanceMatrixTest

class analysisTestSuite(unittest.TestSuite):
    def __init__(self):
        super(analysisTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(IBSDistanceMatrixTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(analysisTestSuite())
    TASSELbridge.stop()
