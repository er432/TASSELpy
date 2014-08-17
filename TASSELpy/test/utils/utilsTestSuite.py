import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.utils.primativeArrayTest import primativeArrayTest
from TASSELpy.test.utils.cachingTest import doubleLinkedListTest

class utilsTestSuite(unittest.TestSuite):
    def __init__(self):
        super(utilsTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(primativeArrayTest))
        self.addTest(unittest.makeSuite(doubleLinkedListTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(utilsTestSuite())
    TASSELbridge.stop()
