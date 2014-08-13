import unittest
from TASSELpy.TASSELbridge import TASSELbridge
from TASSELpy.test.net.maizegenetics.trait.TraitTest import TraitTest
from TASSELpy.test.net.maizegenetics.trait.PhenotypeTest import PhenotypeTest
from TASSELpy.test.net.maizegenetics.trait.MarkerPhenotypeTest import MarkerPhenotypeTest

class traitTestSuite(unittest.TestSuite):
    def __init__(self):
        super(traitTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(TraitTest))
        self.addTest(unittest.makeSuite(PhenotypeTest))
        self.addTest(unittest.makeSuite(MarkerPhenotypeTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(traitTestSuite())
    TASSELbridge.stop()
