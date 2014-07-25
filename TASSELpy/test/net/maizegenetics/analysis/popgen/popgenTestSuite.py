import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.net.maizegenetics.analysis.popgen.LDResultTest import LDResultTest
from TASSELpy.test.net.maizegenetics.analysis.popgen.LinkageDisequilibriumTest import LinkageDisequilibriumTest

class popgenTestSuite(unittest.TestSuite):
    def __init__(self):
        super(popgenTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(LDResultTest))
        self.addTest(unittest.makeSuite(LinkageDisequilibriumTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(popgenTestSuite())
    TASSELbridge.stop()
