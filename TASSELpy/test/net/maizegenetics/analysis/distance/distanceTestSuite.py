import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.net.maizegenetics.analysis.distance.KinshipTest import KinshipTest

class distanceTestSuite(unittest.TestSuite):
    def __init__(self):
        super(distanceTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(KinshipTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(distanceTestSuite())
    TASSELbridge.stop()
