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
from TASSELpy.java.lang.Byte import Byte, metaByte
import numpy as np

class ByteTest(unittest.TestCase):
    """ Tests for Byte.py """
    def test_Byte(self):
        print "Testing Byte constructor"
        val1 = Byte(np.int8(10))
        val2 = Byte('10')
        self.assertIsInstance(val1,Byte)
        self.assertEqual(val1,val2)
    def test_metaByte(self):
        print "Testing metaByte class"
        self.assertIsInstance(Byte(np.int8(10)), metaByte)
        self.assertIsInstance(np.int8(10), metaByte)
        self.assertIsInstance(np.uint8(10), metaByte)
        self.assertNotIsInstance(10, metaByte)
    def test_compareTo(self):
        print "Testing compareTo"
        val1 = Byte(np.int8(10))
        val2 = Byte('10')
        self.assertEquals(val1.compareTo(val2),0)
    def test_addition(self):
        print "Testing addition"
        self.assertEquals(Byte(np.int8(10))+Byte(np.int8(5)), Byte(np.int8(15)))
        self.assertEquals(Byte(np.int8(10))+np.int8(5), Byte(np.int8(15)))
        self.assertEquals(Byte(np.int8(10))+Byte(np.int8(5)), np.int8(15))
if __name__ == "__main__":
    unittest.main(exit=False)
    TASSELbridge.stop()
