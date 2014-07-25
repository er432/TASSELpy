import unittest
import javabridge
from TASSELpy.TASSELbridge import TASSELbridge

try:
    try:
        javabridge.get_env()
    except AttributeError:
        print("AttributeError: start bridge")
        TASSELbridge.start()
    except AssertionError:
        print("AssertionError: start bridge")
        TASSELbridge.start()
except:
    raise RuntimeError("Could not start JVM")

from TASSELpy.java.lang.String import metaString
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon

java_imports = {'String': 'java/lang/String',
                'Taxon': 'net/maizegenetics/taxa/Taxon'}


class TaxonTest(unittest.TestCase):
    """ Tests for GenotypeTable.py """
    _java_name = java_imports['Taxon']

    @classmethod
    def setUpClass(cls):
        # Load data
        name = "Test1"
        cls.obj = Taxon(name)

    def test__init__(self):
        self.assertIsInstance(self.obj, Taxon), "__init__ is error"

    def test_toStringWithVCFAnnotation(self):
        print "Testing toStringWithVCFAnnotation"
        arr = self.obj.toStringWithVCFAnnotation()
        self.assertIsInstance(arr, metaString)

    def test_getName(self):
        print "Testing getName"
        arr = self.obj.getName()
        self.assertIsInstance(arr, metaString)

if __name__ == "__main__":
    unittest.main(exit=False)
    TASSELbridge.stop()
