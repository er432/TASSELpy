import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.net.maizegenetics.stats.statistics.FisherExactTest import FisherExactTest

class statisticsTestSuite(unittest.TestSuite):
    def __init__(self):
        super(statisticsTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(FisherExactTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(statisticsTestSuite())
    TASSELbridge.stop()
