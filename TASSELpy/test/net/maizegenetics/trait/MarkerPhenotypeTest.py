import unittest
import javabridge
import numpy as np
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
from TASSELpy.net.maizegenetics.trait.MarkerPhenotype import MarkerPhenotype
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.net.maizegenetics.trait.ReadPhenotypeUtils import ReadPhenotypeUtils
from TASSELpy.net.maizegenetics.trait.FilterPhenotype import FilterPhenotype
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.data.data_constants import *
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype

debug = False

class MarkerPhenotypeTest(unittest.TestCase):
    """ Tests for MarkerPhenotype.py """
    @classmethod
    def setUpClass(cls):
        cls.aln = ImportUtils.readFromHapmap(HAPMAP_FILE)
        phenos = ReadPhenotypeUtils.readGenericFile(TRAITS_FILE)
        useTraits = javaPrimativeArray.make_array('int',1)
        useTraits[0] = 2
        cls.trait = FilterPhenotype.getInstance(phenos, None, useTraits)
    def test_getInstance(self):
        if debug: print("Testing getInstance")
        combined1 = MarkerPhenotype.getInstance(self.aln, self.trait, False)
        self.assertIsInstance(combined1, MarkerPhenotype)
        self.assertEqual(combined1.getRowCount(),279)
        combined2 = MarkerPhenotype.getInstance(combined1, self.aln.taxa())
        self.assertIsInstance(combined2, MarkerPhenotype)
    def test_getAlignment(self):
        if debug: print("Testing getAlignment")
        combined = MarkerPhenotype.getInstance(self.aln, self.trait, False)
        self.assertIsInstance(combined.getAlignment(), GenotypeTable)
        self.assertEquals(combined.getAlignment().numberOfTaxa(), 279)
    def test_getPhenotype(self):
        if debug: print("Testing getPhenotype")
        combined = MarkerPhenotype.getInstance(self.aln, self.trait, False)
        self.assertIsInstance(combined.getPhenotype(), Phenotype)
        self.assertEqual(combined.getPhenotype().getRowCount(), 279)
                
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
