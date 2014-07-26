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
from TASSELpy.java.lang.Boolean import Boolean, metaBoolean
debug = False

class BooleanTest(unittest.TestCase):
    """ Tests for Boolean.py """
    def test_Boolean(self):
        if debug: print "Testing Boolean constructor"
        val1 = Boolean(True)
        val2 = Boolean('True')
        self.assertIsInstance(val1,Boolean)
        self.assertEqual(val1,val2)
    def test_metaBoolean(self):
        if debug: print "Testing metaBoolean class"
        self.assertIsInstance(Boolean(True), metaBoolean)
        self.assertIsInstance(True, metaBoolean)
    def test_compareTo(self):
        if debug: print "Testing compareTo"
        val1 = Boolean(True)
        val2 = Boolean('True')
        self.assertEquals(val1.compareTo(val2),0)

if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
