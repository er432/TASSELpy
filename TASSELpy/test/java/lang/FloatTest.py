import unittest
import javabridge
from TASSELpy.TASSELbridge import TASSELbridge
try:
    try:
        javabridge.get_env()
    except AttributeError:
        TASSELbridge.start()
    except AssertionError:
        print("AssertionError: start bridge")
        TASSELbridge.start()
except:
    raise RuntimeError("Could not start JVM")
from TASSELpy.java.lang.Float import Float, metaFloat
import numpy as np

class FloatTest(unittest.TestCase):
    """ Tests for Float.py """
    def test_Float(self):
        print "Testing Float constructor"
        val1 = Float(10.0)
        val2 = Float('10.0')
        self.assertIsInstance(val1,Float)
        self.assertEqual(val1,val2)
    def test_metaFloat(self):
        print "Testing metaFloat class"
        self.assertIsInstance(Float(10.0), metaFloat)
        self.assertIsInstance(10.0, metaFloat)
        self.assertIsInstance(np.float32(10), metaFloat)
    def test_compareTo(self):
        print "Testing compareTo"
        val1 = Float(10.0)
        val2 = Float('10.0')
        self.assertEquals(val1.compareTo(val2),0)
    def test_addition(self):
        print "Testing addition"
        self.assertEquals(Float(10.0)+Float(5.0), Float(15.0))
        self.assertEquals(Float(10.0)+5.0, Float(15.0))
        self.assertEquals(Float(10.0)+Float(5.0), 15.0)
if __name__ == "__main__":
    unittest.main(exit=False)
    TASSELbridge.stop()
