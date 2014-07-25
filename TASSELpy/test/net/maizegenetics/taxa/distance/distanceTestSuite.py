import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.net.maizegenetics.taxa.distance.DistanceMatrixTest import DistanceMatrixTest
from TASSELpy.test.net.maizegenetics.taxa.distance.TaxaListMatrixTest import TaxaListMatrixTest

class distanceTestSuite(unittest.TestSuite):
    def __init__(self):
        super(distanceTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(DistanceMatrixTest))
        self.addTest(unittest.makeSuite(TaxaListMatrixTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(distanceTestSuite())
    TASSELbridge.stop()
