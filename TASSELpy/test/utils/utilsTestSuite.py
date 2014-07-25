import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.utils.primativeArrayTest import primativeArrayTest

class utilsTestSuite(unittest.TestSuite):
    def __init__(self):
        super(utilsTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(primativeArrayTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(utilsTestSuite())
    TASSELbridge.stop()
