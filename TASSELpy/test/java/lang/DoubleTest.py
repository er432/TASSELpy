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
from TASSELpy.java.lang.Double import Double, metaDouble
import numpy as np

class DoubleTest(unittest.TestCase):
    """ Tests for Double.py """
    def test_Double(self):
        print "Testing Double constructor"
        val1 = Double(np.float64(10.0))
        val2 = Double('10.0')
        self.assertIsInstance(val1,Double)
        self.assertEqual(val1,val2)
    def test_metaDouble(self):
        print "Testing metaDouble class"
        self.assertIsInstance(Double(np.float64(10.0)), metaDouble)
        self.assertIsInstance(np.float64(10.0), metaDouble)
        self.assertIsInstance(np.longdouble(10.0), metaDouble)
        self.assertNotIsInstance(np.float32(10.0), metaDouble)
    def test_compareTo(self):
        print "Testing compareTo"
        val1 = Double(np.float64(10.0))
        val2 = Double('10.0')
        self.assertEquals(val1.compareTo(val2),0)
    def test_addition(self):
        print "Testing addition"
        self.assertEquals(Double(np.float64(10.0))+Double(np.float64(5.0)), Double(np.float64(15.0)))
        self.assertEquals(Double(np.float64(10.0))+5.0, Double(np.float64(15.0)))
        self.assertEquals(Double(np.float64(10.0))+Double(np.float64(5.0)), np.float64(15.0))
if __name__ == "__main__":
    unittest.main(exit=False)
    TASSELbridge.stop()
