import unittest
from TASSELpy.test.net.maizegenetics.taxa.TaxaListBuilderTest import TaxaListBuilderTest
from TASSELpy.test.net.maizegenetics.taxa.TaxonTest import TaxonTest
from TASSELpy.test.net.maizegenetics.taxa.TaxaListTest import TaxaListTest
from TASSELpy.TASSELbridge import TASSELbridge



class taxaTestSuite(unittest.TestSuite):
    def __init__(self):
        super(taxaTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(TaxaListTest))
        self.addTest(unittest.makeSuite(TaxonTest))
        self.addTest(unittest.makeSuite(TaxaListBuilderTest))


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(taxaTestSuite())
    TASSELbridge.stop()