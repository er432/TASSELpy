import unittest
import javabridge
import numpy as np
from TASSELpy.TASSELbridge import TASSELbridge
try:
    try:
        javabridge.get_env()
    except AttributeError:
        TASSELbridge.start()
    except AssertionError:
        TASSELbridge.start()
except:
    raise RuntimeError("Could not start JVM")
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.net.maizegenetics.stats.statistics.FisherExact import FisherExact
from TASSELpy.net.maizegenetics.dna.WHICH_ALLELE import WHICH_ALLELE
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.data import data_constants
from TASSELpy.net.maizegenetics.analysis.popgen.LinkageDisequilibrium import LinkageDisequilibrium
from TASSELpy.net.maizegenetics.analysis.popgen.LDResult import LDResult

debug = False
class LinkageDisequilibriumTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load data
        try:
            cls.data = ImportUtils.readGuessFormat(data_constants.SHORT_HMP_FILE)
            cls.ld = LinkageDisequilibrium(cls.data, 1, LinkageDisequilibrium.testDesign.All,
                                           0, None, False, 0, None,
                                           LinkageDisequilibrium.HetTreatment.Homozygous)
            cls.ld.run()
        except:
            raise ValueError("Could not load test data")
    def test_constructor(self):
        if debug: print "Testing constructor"
        ld = LinkageDisequilibrium(self.data, 0, None, 0, None, False, 0, None, None)
        self.assertIsInstance(ld, LinkageDisequilibrium)
        self.assertIsInstance(ld.o,javabridge.JB_Object)
    def test_calculateBitLDForHaplotype(self):
        if debug: print "Testing calculateBitLDForHaplotype"
        result = LinkageDisequilibrium.calculateBitLDForHaplotype(True,2,self.data,0,1)
        self.assertIsInstance(result,LDResult)
        self.assertAlmostEqual(result.r2(),0.0280817858875)
    def test_calculateDPrime(self):
        if debug: print "Testing calculateDPrime"
        result = LinkageDisequilibrium.calculateDPrime(10,10,2,0,2)
        self.assertAlmostEquals(result,1.0)
    def test_calculateRSqr(self):
        if debug: print "Testing calculateRsqr"
        result = LinkageDisequilibrium.calculateRSqr(10,10,2,0,2)
        self.assertAlmostEqual(result,0.0833333333333)
    def test_getLDForSitePair(self):
        if debug: print "Testing getLDForSitePair"
        rMj = self.data.allelePresenceForAllTaxa(0,WHICH_ALLELE.Major)
        rMn = self.data.allelePresenceForAllTaxa(0,WHICH_ALLELE.Minor)
        cMj = self.data.allelePresenceForAllTaxa(1,WHICH_ALLELE.Major)
        cMn = self.data.allelePresenceForAllTaxa(1,WHICH_ALLELE.Minor)
        result = LinkageDisequilibrium.getLDForSitePair(rMj,rMn,cMj,cMn,1,1,0.001,
                                                        FisherExact(100),0,1)
        self.assertIsInstance(result, LDResult)
        self.assertAlmostEqual(result.r2(),0.0280817858875)
    def test_getPVal(self):
        if debug: print "Testing getPval"
        pval = self.ld.getPval(0,1)
        self.assertAlmostEqual(pval,0.003451925003901124)
    def test_getSampleSize(self):
        if debug: print "Testing getSampleSize"
        sampsize = self.ld.getSampleSize(0,1)
        self.assertEqual(sampsize,261)
    def test_getDPrime(self):
        if debug: print "Testing getDPrime"
        Dprime = self.ld.getDPrime(0,1)
        self.assertAlmostEqual(Dprime,0.330278605223)
    def test_getRSqr(self):
        if debug: print "Testing getRsqr"
        r2 = self.ld.getRSqr(0,1)
        self.assertAlmostEqual(r2,0.0347763262689)
    def test_getX(self):
        if debug: print "Testing getX"
        x = self.ld.getX(0)
        self.assertEqual(x,0)
    def test_getY(self):
        if debug: print "Testing getY"
        y = self.ld.getY(0)
        self.assertEqual(y,1)
    def test_getSiteCount(self):
        if debug: print "Testing getSiteCount"
        count = self.ld.getSiteCount()
        self.assertEqual(count,9)
    def test_getAlignment(self):
        if debug: print "Testing getAlignment"
        aln = self.ld.getAlignment()
        self.assertIsInstance(aln,GenotypeTable)
if __name__ == "__main__":
    debug = True
    unittest.main(exit = False)
    TASSELbridge.stop()
