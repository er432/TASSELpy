import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.net.maizegenetics.analysis.association.FixedEffectLMPlugin import easy_GLMTest

class associationTestSuite(unittest.TestSuite):
    def __init__(self):
        super(associationTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(easy_GLMTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(associationTestSuite())
    TASSELbridge.stop()
