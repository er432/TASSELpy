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
from TASSELpy.net.maizegenetics.taxa.TaxaListBuilder import TaxaListBuilder
from TASSELpy.net.maizegenetics.taxa.distance.DistanceMatrix import DistanceMatrix
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Double import Double
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.primativeArray import javaPrimativeArray
debug = False

class TableReportTest(unittest.TestCase):
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
    def test_toDict(self):
        if debug: print("Testing toDict")
        theDict = self.mat.toDict()
        self.assertEquals(len(theDict),3)
        self.assertEquals(theDict['Taxa'],[Taxon('first'),Taxon('second')])
        self.assertEquals(theDict['second'],[0.25,0.0])
        self.assertEquals(theDict['first'],[0.0,0.25])
    def test_getTableColumnNames(self):
        if debug: print "Testing getTableColumnNames with DistanceMatrix"
        names = self.mat.getTableColumnNames()
        self.assertIsInstance(names, javaArray.get_array_type(Object))
        self.assertEquals(names[0].toString(),'Taxa')
    def test_getTableTitle(self):
        if debug: print "Testing getTableTitle with DistanceMatrix"
        self.assertEquals(self.mat.getTableTitle(),"Alignment Distance Matrix")
    def test_getColumnCount(self):
        if debug: print "Testing getColumnCount with DistanceMatrix"
        self.assertEquals(self.mat.getColumnCount(),3)
    def test_getRowCount(self):
        if debug: print "Testing getRowCount with DistanceMatrix"
        self.assertEquals(self.mat.getRowCount(),2)
    def test_getElementCount(self):
        if debug: print "Testing getElementCount with DistanceMatrix"
        self.assertEqual(self.mat.getElementCount(),6)
    def test_getRow(self):
        if debug: print "Testing getRow with DistanceMatrix"
        row = self.mat.getRow(0)
        self.assertIsInstance(row, javaArray.get_array_type(Object))
        self.assertEquals(row[0].toString(),'first')
    def test_getValueAt(self):
        if debug: print "Testing getValueAt with DistanceMatrix"
        val = self.mat.getValueAt(1,1)
        self.assertIsInstance(val, Object)
        self.assertEqual(Double(obj=val.o),0.25)
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
