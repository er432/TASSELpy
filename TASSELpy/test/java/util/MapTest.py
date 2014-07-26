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
from TASSELpy.java.util.HashMap import HashMap
from TASSELpy.java.lang.Integer import Integer
from TASSELpy.java.lang.String import String

debug = False

class MapTest(unittest.TestCase):
    """ Tests for Map.py """
    def setUp(self):
        try:
            self.map = HashMap(generic=(String, Integer))
            self.map[String('one')] = Integer(1)
            self.map[String('two')] = Integer(2)
            self.map[String('three')] = Integer(3)
        except:
            self.fail("Map put fail")
    def test_clear(self):
        if debug: print "Testing clear using HashMap"
        self.map.clear()
        self.assertEquals(len(self.map),0)
    def test_containsKey(self):
        if debug: print "Testing containsKey using HashMap"
        self.assertTrue(self.map.containsKey(String('two')))
        self.assertFalse(self.map.containsKey(String('four')))
    def test_containsValue(self):
        if debug: print "Testing containsValue using HashMap"
        self.assertTrue(self.map.containsValue(Integer(2)))
        self.assertFalse(self.map.containsValue(Integer(4)))
    def test_entrySet(self):
        if debug: print "Testing entrySet using HashMap"
        entryset = [x for x in self.map.entrySet()]
        self.assertEquals(len(entryset),3)
        self.assertIsInstance(entryset[0].getKey(),String)
        self.assertIsInstance(entryset[0].getValue(),Integer)
    def test_get(self):
        if debug: print "Testing get using HashMap"
        self.assertEquals(self.map.get(String('one')),Integer(1))
        self.assertEquals(self.map[String('one')],Integer(1))
    def test_isEmpty(self):
        if debug: print "Testing isEmpty using HashMap"
        self.assertFalse(self.map.isEmpty())
        self.map.clear()
        self.assertTrue(self.map.isEmpty())
    def test_keySet(self):
        if debug: print "Testing keySet using HashMap"
        keys = self.map.keySet()
        self.assertTrue(String('two') in keys)
        self.assertFalse(String('four') in keys)
    def test_putAll(self):
        if debug: print "Testing putAll using HashMap"
        new_map = HashMap(generic=(String, Integer))
        new_map[String('four')] = Integer(4)
        new_map[String('five')] = Integer(5)
        self.map.putAll(new_map)
        self.assertTrue(self.map.containsKey(String('four')))
        self.assertEquals(len(self.map),5)
    def test_remove(self):
        if debug: print "Testing remove using HashMap"
        self.map.remove(String('three'))
        self.assertFalse(self.map.containsKey(String('three')))
        self.assertTrue(self.map.containsKey(String('two')))
        del self.map[String('two')]
        self.assertFalse(self.map.containsKey(String('two')))
    def test_size(self):
        if debug: print "Testing size using HashMap"
        self.assertEquals(len(self.map),3)
    def test_values(self):
        if debug: print "Testing values using HashMap"
        vals = self.map.values()
        self.assertTrue(Integer(1) in vals)
        self.assertTrue(Integer(3) in vals)
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
