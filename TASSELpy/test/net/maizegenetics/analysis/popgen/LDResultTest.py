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
from TASSELpy.net.maizegenetics.analysis.popgen.LDResult import LDResult

debug = False

class LDResultTest(unittest.TestCase):
    def setUp(self):
        builder = LDResult.Builder(0,1).r2(0.1).dprime(0.2).p(0.05).n(100)
        self.result = builder.build()
    def test_r2(self):
        if debug: print "Testing r2"
        self.assertAlmostEqual(self.result.r2(),0.1)
    def test_dPrime(self):
        if debug: print "Testing dPrime"
        self.assertAlmostEqual(self.result.dPrime(),0.2)
    def test_p(self):
        if debug: print "Testing p"
        self.assertAlmostEqual(self.result.p(),0.05)
    def test_n(self):
        if debug: print "Testing n"
        self.assertEqual(self.result.n(),100)
    def test_site1(self):
        if debug: print "Testing site1"
        self.assertEqual(self.result.site1(),0)
    def test_site2(self):
        if debug: print "Testing site2"
        self.assertEqual(self.result.site2(),1)

if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
