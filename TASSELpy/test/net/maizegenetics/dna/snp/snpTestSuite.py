import unittest
from TASSELpy.test.net.maizegenetics.dna.snp.GenotypeTableTest import GenotypeTableTest
from TASSELpy.TASSELbridge import TASSELbridge

class snpTestSuite(unittest.TestSuite):
    def __init__(self):
        super(snpTestSuite, self).__init__()
        self.addTest(unittest.makeSuite(GenotypeTableTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(snpTestSuite())
    TASSELbridge.stop()
