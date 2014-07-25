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
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.net.maizegenetics.taxa.TaxaListBuilder import TaxaListBuilder
from TASSELpy.net.maizegenetics.taxa.distance.DistanceMatrix import DistanceMatrix
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.javaObj import javaArray

class DistanceMatrixTest(unittest.TestCase):
    def test_constructor1(self):
        print "Testing first DistanceMatrix constructor"
        mat = DistanceMatrix()
        self.assertIsInstance(mat, DistanceMatrix)
        self.assertIsInstance(mat.o, javabridge.JB_Object)
    def test_constructor2(self):
        print "Testing second DistanceMatrix constructor"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat = DistanceMatrix(primative_mat, taxa_list)
        self.assertIsInstance(mat, DistanceMatrix)
        self.assertIsInstance(mat.o, javabridge.JB_Object)
    def test_constructor3(self):
        print "Testing third DistanceMatrix constructor"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat1 = DistanceMatrix(primative_mat, taxa_list)
        mat2 = DistanceMatrix(mat1)
        self.assertIsInstance(mat2, DistanceMatrix)
        self.assertNotEqual(mat1.o, mat2.o)
    def test_constructor4(self):
        print "Testing fourth DistanceMatrix constructor"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat1 = DistanceMatrix(primative_mat, taxa_list)
        mat2 = DistanceMatrix(mat1, taxa_list)
        self.assertIsInstance(mat2, DistanceMatrix)
        self.assertNotEqual(mat1.o, mat2.o)
    def test_squaredDistance(self):
        print "Testing squaredDistance"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat1 = DistanceMatrix(primative_mat, taxa_list)
        mat2 = DistanceMatrix(mat1)
        dist = mat1.squaredDistance(mat2, False)
        self.assertIsInstance(dist, metaDouble)
        self.assertEquals(dist, 0.)
    def test_absoluteDistance(self):
        print "Testing absoluteDistance"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat1 = DistanceMatrix(primative_mat, taxa_list)
        mat2 = DistanceMatrix(mat1)
        dist = mat1.absoluteDistance(mat2)
        self.assertIsInstance(dist, metaDouble)
        self.assertEquals(dist, 0.)
    def test_getDistances(self):
        print "Testing getDistances"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat = DistanceMatrix(primative_mat, taxa_list)
        dists = mat.getDistances()
        self.assertIsInstance(dists, javaArray.get_array_type(javaPrimativeArray.get_array_type('double')))
        self.assertEqual(dists[0][1],primative_mat[0][1])
    def test_getTaxon(self):
        print "Testing getTaxon"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat = DistanceMatrix(primative_mat, taxa_list)
        tax = mat.getTaxon(1)
        self.assertIsInstance(tax, Taxon)
        self.assertEqual(tax.toString(), "second")
    def test_numberOfTaxa(self):
        print "Testing numberOfTaxa"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat = DistanceMatrix(primative_mat, taxa_list)
        self.assertEquals(mat.numberOfTaxa(),2)
    def test_whichIdNumber(self):
        print "Testing whichIdNumber"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat = DistanceMatrix(primative_mat, taxa_list)
        self.assertEquals(mat.whichIdNumber('first'),0)
        self.assertEquals(mat.whichIdNumber(Taxon('first')),0)
    def test_getClosestIndex(self):
        print "Testing getClosestIndex"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat = DistanceMatrix(primative_mat, taxa_list)
        self.assertEqual(mat.getClosestIndex(0,None),1)
    def test_getColumnName(self):
        print "Testing getColumnName"
        primative_mat = javaPrimativeArray.make_dbl_array('double',2,2)
        primative_mat[0][0] = np.float64(0.)
        primative_mat[0][1] = np.float64(0.25)
        primative_mat[1][0] = np.float64(0.25)
        primative_mat[1][1] = np.float64(0.)
        list_builder = TaxaListBuilder()
        list_builder.add(Taxon('first'))
        list_builder.add(Taxon('second'))
        taxa_list = list_builder.build()
        mat = DistanceMatrix(primative_mat, taxa_list)
        self.assertEquals(mat.getColumnName(1),'first')
        self.assertEquals(mat.getColumnName(2),'second')
if __name__ == "__main__":
    unittest.main(exit=False)
    TASSELbridge.stop()
