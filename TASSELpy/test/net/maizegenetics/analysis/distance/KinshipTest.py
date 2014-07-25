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
        TASSELbridge.start()
except:
    raise RuntimeError("Could not start JVM")
from TASSELpy.data import data_constants
from TASSELpy.net.maizegenetics.analysis.distance.Kinship import Kinship
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.net.maizegenetics.taxa.distance.DistanceMatrix import DistanceMatrix
debug = False

class KinshipTest(unittest.TestCase):
    def setUp(self):
        # Test constructor1
        genoTable = ImportUtils.readGuessFormat(data_constants.SHORT_HMP_FILE)
        self.kin_vals = Kinship(genoTable)
    def test_getDm(self):
        if debug: print "Testing getDm"
        dm = self.kin_vals.getDm()
        self.assertIsInstance(dm, DistanceMatrix)
        

if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
