import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.java.util.MapTest import MapTest

class utilTestSuite(unittest.TestSuite):
    def __init__(self):
        super(utilTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(MapTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(utilTestSuite())
    TASSELbridge.stop()
