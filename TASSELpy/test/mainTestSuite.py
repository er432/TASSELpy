import unittest
from TASSELpy.test.net.maizegenetics.dna.snp.snpTestSuite import snpTestSuite
from TASSELpy.test.java.lang.langTestSuite import langTestSuite
from TASSELpy.test.utils.utilsTestSuite import utilsTestSuite
from TASSELpy.test.javaObjTest import javaObjTest, javaArrayTest, genericJavaObjTest
from TASSELpy.test.net.maizegenetics.taxa.distance.distanceTestSuite import distanceTestSuite
from TASSELpy.test.net.maizegenetics.taxa.taxaTestSuite import taxaTestSuite
from TASSELpy.test.net.maizegenetics.util.utilTestSuite import utilTestSuite
from TASSELpy.test.net.maizegenetics.analysis.analysisTestSuite import analysisTestSuite
from TASSELpy.test.net.maizegenetics.analysis.distance.distanceTestSuite import distanceTestSuite
from TASSELpy.test.java.util.utilTestSuite import utilTestSuite
from TASSELpy.test.net.maizegenetics.trait.traitTestSuite import traitTestSuite
from TASSELpy.test.net.maizegenetics.analysis.popgen.popgenTestSuite import popgenTestSuite
from TASSELpy.test.net.maizegenetics.stats.statistics.statisticsTestSuite import statisticsTestSuite
from TASSELpy.test.net.maizegenetics.matrixalgebra.Matrix.MatrixTestSuite import MatrixTestSuite
from TASSELpy.test.net.maizegenetics.matrixalgebra.decomposition.decompositionTestSuite import decompositionTestSuite
from TASSELpy.test.net.maizegenetics.analysis.association.associationTestSuite import associationTestSuite
from TASSELpy.TASSELbridge import TASSELbridge


class mainTestSuite(unittest.TestSuite):
    def __init__(self):
        super(mainTestSuite, self).__init__()
        self.addTest(snpTestSuite())
        self.addTest(langTestSuite())
        self.addTest(utilsTestSuite())
        self.addTest(distanceTestSuite())
        self.addTest(utilTestSuite())
        self.addTest(analysisTestSuite())
        self.addTest(distanceTestSuite())
        self.addTest(utilTestSuite())
        self.addTest(traitTestSuite())
        self.addTest(popgenTestSuite())
        self.addTest(statisticsTestSuite())
        self.addTest(MatrixTestSuite())
        self.addTest(decompositionTestSuite())
        self.addTest(unittest.makeSuite(javaObjTest))
        self.addTest(unittest.makeSuite(javaArrayTest))
        self.addTest(unittest.makeSuite(genericJavaObjTest))
        self.addTest(taxaTestSuite())
        self.addTest(associationTestSuite())

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(mainTestSuite())
    TASSELbridge.stop()
