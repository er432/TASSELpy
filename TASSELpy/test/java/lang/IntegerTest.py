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
from TASSELpy.java.lang.Integer import Integer, metaInteger
import numpy as np

class IntegerTest(unittest.TestCase):
    """ Tests for Integer.py """
    def test_Integer(self):
        print "Testing Integer constructor"
        val1 = Integer(10)
        val2 = Integer('10')
        self.assertIsInstance(val1,Integer)
        self.assertEqual(val1,val2)
    def test_metaInteger(self):
        print "Testing metaInteger class"
        self.assertIsInstance(Integer(10), metaInteger)
        self.assertIsInstance(10, metaInteger)
        self.assertIsInstance(np.int32(10), metaInteger)
        self.assertNotIsInstance(np.int8(10), metaInteger)
    def test_compareTo(self):
        print "Testing compareTo"
        val1 = Integer(10)
        val2 = Integer('10')
        self.assertEquals(val1.compareTo(val2),0)
    def test_addition(self):
        print "Testing addition"
        self.assertEquals(Integer(10)+Integer(5), Integer(15))
        self.assertEquals(Integer(10)+5, Integer(15))
        self.assertEquals(Integer(10)+Integer(5), 15)
if __name__ == "__main__":
    unittest.main(exit=False)
    TASSELbridge.stop()
