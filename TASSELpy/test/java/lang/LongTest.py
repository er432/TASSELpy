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
from TASSELpy.java.lang.Long import Long, metaLong
import numpy as np

class LongTest(unittest.TestCase):
    """ Tests for Long.py """
    def test_Long(self):
        print "Testing Long constructor"
        val1 = Long(long(10))
        val2 = Long('10')
        self.assertIsInstance(val1,Long)
        self.assertEqual(val1,val2)
    def test_metaLong(self):
        print "Testing metaLong class"
        self.assertIsInstance(Long(long(10)), metaLong)
        self.assertIsInstance(long(10), metaLong)
        self.assertIsInstance(np.int64(10), metaLong)
        self.assertNotIsInstance(np.int32(10), metaLong)
    def test_compareTo(self):
        print "Testing compareTo"
        val1 = Long(np.int64(10))
        val2 = Long('10')
        self.assertEquals(val1.compareTo(val2),0)
    def test_addition(self):
        print "Testing addition"
        self.assertEquals(Long(long(10))+Long(long(5)), Long(long(15)))
        self.assertEquals(Long(long(10))+long(5), Long(long(15)))
        self.assertEquals(Long(long(10))+Long(long(5)), long(15))
if __name__ == "__main__":
    unittest.main(exit=False)
    TASSELbridge.stop()
