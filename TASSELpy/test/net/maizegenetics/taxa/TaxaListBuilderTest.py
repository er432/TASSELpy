__author__ = 'Administrator'

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

from TASSELpy.net.maizegenetics.taxa.TaxaListBuilder import *
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.data import data_constants
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.util.ArrayList import ArrayList

java_imports = {'String': 'java/lang/String',
                'Taxon': 'net/maizegenetics/taxa/Taxon'}


class TaxaListBuilderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load data
        try:
            cls.data = ImportUtils.readGuessFormat(data_constants.SHORT_HMP_FILE)
            cls.test = TaxaListBuilder()
            assert type(cls.test) is TaxaListBuilder, "TaxaListBuilder constructure error"
        except:
            raise ValueError("Could not load test data")

    def test_add(self):
        arr = self.test.add(Taxon("Test Bokan"))
        self.assertIsInstance(arr, TaxaListBuilder)

    def test_addAll(self):
        arr1 = self.test.addAll(self.data)
        self.assertIsInstance(arr1, TaxaListBuilder)
        string_arr = String.getArray(2)
        string_arr[0] = "aaa"
        string_arr[1] = "bbb"
        arr2 = self.test.addAll(string_arr)
        self.assertIsInstance(arr2, TaxaListBuilder)
        Taxon_arr = Object.getArray(2)
        Taxon_arr[0] = Taxon("BokanTest1")
        Taxon_arr[1] = Taxon("BokanTest2")
        arr3 = self.test.addAll(Taxon_arr)
        self.assertIsInstance(arr3, TaxaListBuilder)
        collection_arr = ArrayList(generic=(Taxon,))
        collection_arr.add(0, Taxon("BokanTest4"))
        collection_arr.add(0, Taxon("BokanTest3"))
        arr4 = self.test.addAll(collection_arr)
        self.assertIsInstance(arr4, TaxaListBuilder)

    def test_duild(self):
        arr1 = self.test.build()
        self.assertIsInstance(arr1, TaxaList)


if __name__ == '__main__':
    unittest.main(exit=False)
    TASSELbridge.stop()
