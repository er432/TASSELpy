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
from TASSELpy.net.maizegenetics.stats.statistics.FisherExact import FisherExact

debug = False
class FisherExactTest(unittest.TestCase):
    def setUp(self):
        self.test = FisherExact(100)
    def test_getP(self):
        if debug: print "Testing getP"
        p = self.test.getP(2,3,6,4)
        self.assertAlmostEqual(p,0.32634032634)
    def test_getCumulativeP(self):
        if debug: print "Testing getCumulativeP"
        p = self.test.getCumulativeP(2,3,6,4)
        self.assertAlmostEqual(p,0.426573426573)
    def test_getRightTailedP(self):
        if debug: print "Testing getRightTailedP"
        p = self.test.getRightTailedP(2,3,6,4)
        self.assertAlmostEqual(p,0.899766899767)
    def test_getRightTailedPQuick(self):
        if debug: print "Testing getRightTailedPQuick"
        p = self.test.getRightTailedPQuick(2,3,6,4,np.float64(0.9))
        self.assertAlmostEqual(p,0.899766899767)
    def test_getLeftTailedP(self):
        if debug: print "Testing getLeftTailedP"
        p = self.test.getLeftTailedP(2,3,6,4)
        self.assertAlmostEqual(p,0.426573426573)
    def test_getTwoTailedP(self):
        if debug: print "Testing getTwoTailedP"
        p = self.test.getTwoTailedP(2,3,6,4)
        self.assertAlmostEqual(p,0.608391608392)
if __name__ == "__main__":
    debug = True
    unittest.main(exit = False)
    TASSELbridge.stop()
