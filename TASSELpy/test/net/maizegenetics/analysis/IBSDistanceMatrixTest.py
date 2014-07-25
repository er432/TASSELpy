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
from TASSELpy.net.maizegenetics.dna.WHICH_ALLELE import WHICH_ALLELE
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.java.lang.String import metaString
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.net.maizegenetics.analysis.distance.IBSDistanceMatrix import IBSDistanceMatrix
from TASSELpy.data import data_constants
from TASSELpy.utils.primativeArray import javaPrimativeArray
debug = False

class IBSDistanceMatrixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load data
        try:
            cls.data = ImportUtils.readGuessFormat(data_constants.SHORT_HMP_FILE)
        except:
            raise ValueError("Could not load test data")
    def test_constructor1(self):
        if debug: print "Testing constructor 1"
        dists = IBSDistanceMatrix(self.data)
        self.assertIsInstance(dists, IBSDistanceMatrix)
        self.assertIsInstance(dists.o,javabridge.JB_Object)
    def test_constructor2(self):
        if debug: print "Testing constructor 2"
        dists = IBSDistanceMatrix(self.data,None)
        self.assertIsInstance(dists, IBSDistanceMatrix)
        self.assertIsInstance(dists.o,javabridge.JB_Object)
    def test_constructor3(self):
        if debug: print "Testing constructor 3"
        dists = IBSDistanceMatrix(self.data,10,None)
        self.assertIsInstance(dists, IBSDistanceMatrix)
        self.assertIsInstance(dists.o,javabridge.JB_Object)
    def test_constructor4(self):
        if debug: print "Testing constructor 4"
        dists = IBSDistanceMatrix(self.data,10,False,None)
        self.assertIsInstance(dists, IBSDistanceMatrix)
        self.assertIsInstance(dists.o,javabridge.JB_Object)
    def test_computeHetBitDistances(self):
        if debug: print "Testing computeHetBitDistances"
        # First method
        dist = IBSDistanceMatrix.computeHetBitDistances(self.data,0,0)
        self.assertIsInstance(dist,javaPrimativeArray.get_array_type('double'))
        self.assertEquals(dist[0],0.)
        self.assertEquals(dist[1],9.)
        # Second method
        dist = IBSDistanceMatrix.computeHetBitDistances(self.data,0,0,2,False)
        self.assertIsInstance(dist,javaPrimativeArray.get_array_type('double'))
        self.assertEquals(dist[0],0.)
        self.assertEquals(dist[1],9.)
        # Third method
        dist = IBSDistanceMatrix.computeHetBitDistances(self.data,0,0,2,0,0,None)
        self.assertIsInstance(dist,javaPrimativeArray.get_array_type('double'))
        self.assertEquals(dist[0],0.)
        self.assertEquals(dist[1],9.)
        # Fourth method
        majorBits1 = self.data.allelePresenceForAllSites(0,WHICH_ALLELE.Major).getBits()
        minorBits1 = self.data.allelePresenceForAllSites(0,WHICH_ALLELE.Minor).getBits()
        dist = IBSDistanceMatrix.computeHetBitDistances(majorBits1,minorBits1,majorBits1,minorBits1,2)
        self.assertIsInstance(dist,javaPrimativeArray.get_array_type('double'))
        self.assertEquals(dist[0],0.)
        self.assertEquals(dist[1],9.)
        # Fifth method
        majorBits1 = self.data.allelePresenceForAllSites(0,WHICH_ALLELE.Major).getBits()
        minorBits1 = self.data.allelePresenceForAllSites(0,WHICH_ALLELE.Minor).getBits()
        dist = IBSDistanceMatrix.computeHetBitDistances(majorBits1,minorBits1,majorBits1,minorBits1,2,0,0)
        self.assertIsInstance(dist,javaPrimativeArray.get_array_type('double'))
        self.assertEquals(dist[0],0.)
        self.assertEquals(dist[1],9.)
    def test_getAverageTotalSits(self):
        if debug: print "Testing getAverageTotalSites"
        dists = IBSDistanceMatrix(self.data)
        avg = dists.getAverageTotalSites()
        self.assertIsInstance(avg, metaDouble)
        self.assertLessEqual(avg, 9.)
    def toString(self):
        if debug: print "Testing toString"
        dists = IBSDistanceMatrix(self.data)
        val1 = dists.toString()
        val2 = dists.toString(6)
        self.assertIsInstance(val1,metaString)
        self.assertEqual(val1,val2)
    def test_isTrueIBS(self):
        if debug: print "Testing isTrueIBS"
        dists = IBSDistanceMatrix(self.data)
        self.assertFalse(dists.isTrueIBS())
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
