import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.java.lang.BooleanTest import BooleanTest
from TASSELpy.test.java.lang.ByteTest import ByteTest
from TASSELpy.test.java.lang.IntegerTest import IntegerTest
from TASSELpy.test.java.lang.LongTest import LongTest
from TASSELpy.test.java.lang.FloatTest import FloatTest
from TASSELpy.test.java.lang.DoubleTest import DoubleTest

class langTestSuite(unittest.TestSuite):
    def __init__(self):
        super(langTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(BooleanTest))
        self.addTest(unittest.makeSuite(ByteTest))
        self.addTest(unittest.makeSuite(IntegerTest))
        self.addTest(unittest.makeSuite(LongTest))
        self.addTest(unittest.makeSuite(FloatTest))
        self.addTest(unittest.makeSuite(DoubleTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(langTestSuite())
    TASSELbridge.stop()
