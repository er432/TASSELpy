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
from TASSELpy.net.maizegenetics.trait.SimplePhenotype import SimplePhenotype
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.net.maizegenetics.trait.Trait import Trait
from TASSELpy.net.maizegenetics.taxa.TaxaListBuilder import TaxaListBuilder
from TASSELpy.java.util.ArrayList import ArrayList
from TASSELpy.java.util.List import List
from TASSELpy.utils.primativeArray import javaPrimativeArray

debug = False

class PhenotypeTest(unittest.TestCase):
    """ Tests for Phenotype.py, SimplePhenotype.py """
    def setUp(self):
        tlb = TaxaListBuilder()
        tlb.add(Taxon("Taxon1"))
        tlb.add(Taxon("Taxon2"))
        taxa = tlb.build()
        traits = ArrayList(generic=(Trait,))
        traits.add(Trait("Trait1",True,"factor"))
        traits.add(Trait("Trait2",True,"factor"))
        # Test constructor 3
        pheno = SimplePhenotype(taxa, traits)
        # Test constructor 2
        data = javaPrimativeArray.make_dbl_array('double',2,2)
        data[0][0] = np.float64(1.)
        data[0][1] = np.float64(2.)
        data[1][0] = np.float64(3.)
        data[1][1] = np.float64(4.)
        self.pheno = SimplePhenotype(taxa, traits, data)
    def test_getData(self):
        if debug: print "Testing getData"
        dat1 = self.pheno.getData(0,0)
        dat2 = self.pheno.getData(Taxon("Taxon1"),
                                  Trait("Trait1",True,"factor"))
        self.assertEqual(dat1,dat2)
        self.assertEquals(dat1,1.)
    def test_setData(self):
        if debug: print "Testing setData"
        self.pheno.setData(0,0,np.float64(42.))
        self.assertEquals(self.pheno.getData(0,0),np.float64(42.))
    def test_whichTrait(self):
        if debug: print "Testing whichTrait"
        trait = Trait("Trait2",True,"factor")
        self.assertEqual(self.pheno.whichTrait(trait),1)
    def test_whichTaxon(self):
        if debug: print "Testing whichTaxon"
        taxon = Taxon("Taxon2")
        self.assertEqual(self.pheno.whichTaxon(taxon),1)
    def test_getTrait(self):
        if debug: print "Testing getTrait"
        trait = self.pheno.getTrait(0)
        self.assertEqual(trait,Trait("Trait1",True,"factor"))
    def test_getTaxon(self):
        if debug: print "Testing getTaxon"
        self.assertEqual(Taxon('Taxon1'), self.pheno.getTaxon(0))
    def test_getNumberOfTaxa(self):
        if debug: print "Testing getNumberOfTaxa"
        self.assertEqual(self.pheno.getNumberOfTaxa(),2)
    def test_getNumberOfTraits(self):
        if debug: print "Testing getNumberOfTraits"
        self.assertEqual(self.pheno.getNumberOfTraits(),2)
    def test_getTraits(self):
        if debug: print "Testing getTraits"
        traits = self.pheno.getTraits()
        self.assertIsInstance(traits, List)
        self.assertIsInstance(traits[0],Trait)
        self.assertEqual(traits[0],Trait("Trait1",True,"factor"))
    def test_getTaxa(self):
        if debug: print "Testing getTaxa"
        taxa = self.pheno.getTaxa()
        self.assertIsInstance(taxa,TaxaList)
        self.assertEqual(taxa[0],Taxon("Taxon1"))
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
