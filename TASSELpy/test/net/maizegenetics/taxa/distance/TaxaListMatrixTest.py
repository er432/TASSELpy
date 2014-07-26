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
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.javaObj import javaArray
from TASSELpy.net.maizegenetics.taxa.TaxaListBuilder import TaxaListBuilder
from TASSELpy.net.maizegenetics.taxa.distance.DistanceMatrix import DistanceMatrix
from TASSELpy.net.maizegenetics.taxa.distance.TaxaListMatrix import TaxaListMatrix
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList

debug = False
class TaxaListMatrixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        cls.mat = DistanceMatrix(primative_mat, taxa_list)
    def test_getTaxaList(self):
        if debug: print "Testing getTaxaList with DistanceMatrix"
        taxa_list = self.mat.getTaxaList()
        self.assertIsInstance(taxa_list,TaxaList)
        self.assertIsInstance(taxa_list.o, javabridge.JB_Object)
        self.assertEquals(taxa_list[0],Taxon('first'))
    def test_toString(self):
        if debug: print "Testing toString with DistanceMatrix"
        self.assertTrue('first' in self.mat.toString())
    def test_getSize(self):
        if debug: print "Testing getSize with DistanceMatrix"
        self.assertEquals(self.mat.getSize(),2)
    def test_getClonedDistances(self):
        if debug: print "Testing getClonedDistances with DistanceMatrix"
        dist_mat = self.mat.getClonedDistances()
        self.assertIsInstance(dist_mat,
                              javaArray.get_array_type(javaPrimativeArray.get_array_type('double')))
        self.assertEquals(dist_mat[0][1],np.float64(0.25))
    def test_getDistance(self):
        if debug: print "Testing getDistance with DistanceMatrix"
        self.assertEquals(self.mat.getDistance(0,1),0.25)
    def test_meanDistance(self):
        if debug: print "Testing meanDistance with DistanceMatrix"
        self.assertEquals(self.mat.meanDistance(),0.25)
    def test_isSymmetric(self):
        if debug: print "Testing isSymmetric with DistanceMatrix"
        self.assertTrue(self.mat.isSymmetric())
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
