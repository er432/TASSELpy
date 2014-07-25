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
from TASSELpy.java.lang.Object import Object
from TASSELpy.net.maizegenetics.trait.Trait import Trait
from TASSELpy.java.lang.String import String
from TASSELpy.java.util.Set import Set
from TASSELpy.java.util.ArrayList import ArrayList
debug = False

class TraitTest(unittest.TestCase):
    """ Tests for Trait.py """
    def setUp(self):
        try:
            self.trait = Trait("myTrait",True,"factor",None)
        except:
            self.fail("Constructor 1 fail on Trait")
        try:
            self.trait = Trait("myTrait",True,"factor")
        except:
            self.fail("Constructor 2 fail on Trait")
    def test_getInstance(self):
        if debug: print "Testing getInstance"
        copy = Trait.getInstance(self.trait)
        self.assertEqual(copy,self.trait)
    def test_isDiscrete(self):
        if debug: print "Testing isDiscrete"
        self.assertTrue(self.trait.isDiscrete())
    def test_setLevelLabels(self):
        if debug: print "Testing gen/setLevelLabels"
        arr = String.getArray(3)
        arr[0] = 'one'
        arr[1] = 'two'
        arr[2] = 'three'
        self.trait.setLevelLabels(arr)
        levels = self.trait.getLevelLabels()
        self.assertEqual(len(levels),3)
        self.assertEqual(levels[0],'one')
        self.assertEqual(levels[2],'three')
    def test_getLevelLabel(self):
        if debug: print "Testing getLevelLabel"
        arr = String.getArray(3)
        arr[0] = 'one'
        arr[1] = 'two'
        arr[2] = 'three'
        self.trait.setLevelLabels(arr)
        self.assertEqual(self.trait.getLevelLabel(1),'two')
    def test_getNumberOfLevels(self):
        if debug: print "Testing getNumberOfLevels"
        self.assertEqual(self.trait.getNumberOfLevels(),0)
        arr = String.getArray(3)
        arr[0] = 'one'
        arr[1] = 'two'
        arr[2] = 'three'
        self.trait.setLevelLabels(arr)
        self.assertEqual(self.trait.getNumberOfLevels(),3)
    def test_getNumberOfProperties(self):
        if debug: print "Testing getNumberOfProperties"
        self.assertEqual(self.trait.getNumberOfProperties(),0)
    def test_setProperty(self):
        if debug: print "Testing setProperty"
        self.trait.setProperty("foo",String("bar"))
        self.assertEqual(self.trait.getNumberOfProperties(),1)
    def test_getProperties(self):
        if debug: print "Testing getProperties"
        self.trait.setProperty("foo",String("bar"))
        prop_set = self.trait.getProperties()
        self.assertIsInstance(prop_set,Set)
        prop_set = [x for x in prop_set]
        self.assertEqual(prop_set[0].getKey(),"foo")
        self.assertIsInstance(prop_set[0].getValue(),Object)
        self.assertIsInstance(prop_set[0].o,javabridge.JB_Object)
        self.assertEqual(prop_set[0].getValue().toString(),"bar")
    def test_getProperty(self):
        if debug: print "Testing getProperty"
        self.trait.setProperty("foo",String("bar"))
        prop = self.trait.getProperty("foo")
        self.assertIsInstance(prop, Object)
        self.assertEqual(prop.toString(),"bar")
    def test_getPropertyNames(self):
        if debug: print "Testing getPropertyNames"
        self.trait.setProperty("foo",String("bar"))
        propnames = self.trait.getPropertyNames()
        self.assertIsInstance(propnames,Set)
        prop_names = [x for x in propnames]
        self.assertIsInstance(prop_names[0],String)
        self.assertEqual(prop_names[0],"foo")
    def test_addFactor(self):
        if debug: print "Testing addFactor"
        self.trait.addFactor("Foo","Bar")
        self.assertEqual(self.trait.getNumberOfFactors(),1)
    def test_getFactorNames(self):
        if debug: print "Testing getFactorNames"
        self.trait.addFactor("Foo","Bar")
        factor_names = self.trait.getFactorNames()
        self.assertIsInstance(factor_names,ArrayList)
        self.assertEqual(factor_names[0],"Foo")
    def test_getFactorValue(self):
        if debug: print "Testing getFactorValue"
        self.trait.addFactor("Foo","Bar")
        self.assertEqual(self.trait.getFactorValue("Foo"),"Bar")
    def test_getType(self):
        if debug: print "Testing getType"
        self.assertEqual(self.trait.getType(),"factor")
    def test_setType(self):
        if debug: print "Testing setType"
        self.trait.setType("covariate")
        self.assertEqual(self.trait.getType(),"covariate")
    def test_hasLevels(self):
        if debug: print "Testing hasLevels"
        self.assertFalse(self.trait.hasLevels())
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
