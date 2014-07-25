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
from TASSELpy.net.maizegenetics.taxa.TaxaList import *
from TASSELpy.net.maizegenetics.taxa.TaxaListBuilder import TaxaListBuilder
from TASSELpy.java.lang.String import metaString


class TaxaListTest(unittest.TestCase):

    list_builder = TaxaListBuilder()
    list_builder.add(Taxon('first'))
    list_builder.add(Taxon('second'))
    taxa_list = list_builder.build()

    def test___init__(self):
        # Load data
        assert type(self.taxa_list) is TaxaList, "TaxaListBuilder constructure error"
        self.assertIsInstance(self.taxa_list, TaxaList), "__init__ is error"

    def test_numberOfTaxa(self):
        arr = self.taxa_list.numberOfTaxa()
        self.assertIsInstance(arr, metaInteger)
        self.assertEqual(arr, 2)

    def test_taxaName(self):
        arr1 = self.taxa_list.taxaName(0)
        arr2 = self.taxa_list.taxaName(1)
        self.assertIsInstance(arr1, metaString)


if __name__ == '__main__':
    unittest.main(exit=False)
    TASSELbridge.stop()
