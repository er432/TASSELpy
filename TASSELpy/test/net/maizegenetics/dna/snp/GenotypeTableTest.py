import unittest
import javabridge
from javabridge import JavaException, is_instance_of
import numpy as np
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
from TASSELpy.net.maizegenetics.dna.WHICH_ALLELE import WHICH_ALLELE
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.net.maizegenetics.dna.map.PositionList import PositionList
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.util.BitSet import BitSet
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.utils.primativeArray import meta_byte_array, meta_long_array, meta_int_array, javaPrimativeArray
from TASSELpy.javaObj import javaArray
from TASSELpy.net.maizegenetics.dna.map.Chromosome import Chromosome
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Long import metaLong
from TASSELpy.java.lang.String import String,metaString
from TASSELpy.java.lang.Byte import metaByte
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.net.maizegenetics.dna.snp.depth.AlleleDepth import AlleleDepth
from TASSELpy.data import data_constants

debug = False

java_imports = {'IllegalStateException': 'java/lang/IllegalStateException',
                'NullPointerException': 'java/lang/NullPointerException',
                'UnsupportedOperationException': 'java/lang/UnsupportedOperationException'}

class GenotypeTableTest(unittest.TestCase):
    """ Tests for GenotypeTable.py """
    @classmethod
    def setUpClass(cls):
        # Load data
        try:
            cls.data = ImportUtils.readGuessFormat(data_constants.SHORT_HMP_FILE)
        except:
            raise ValueError("Could not load test data")
    def test_genotypeArray(self):
        if debug: print "Testing genotypeArray"
        arr = self.data.genotypeArray(0,0)
        self.assertIsInstance(arr,meta_byte_array)
    def test_genotype(self):
        if debug: print "Testing genotype"
        first_site_chrom = self.data.chromosome(0)
        first_site_pos = self.data.chromosomalPosition(0)
        geno1 = self.data.genotype(0,0)
        self.assertIsInstance(geno1, metaByte)
        self.assertEqual(geno1, self.data.genotype(0,first_site_chrom,first_site_pos))
    def test_genotypeRange(self):
        if debug: print "Testing genotypeRange"
        arr = self.data.genotypeRange(0,0,1)
        self.assertIsInstance(arr,meta_byte_array)
    def test_genotypeAllSites(self):
        if debug: print "Testing genotypeAllSites"
        arr = self.data.genotypeAllSites(0)
        self.assertIsInstance(arr,meta_byte_array)
    def test_genotypeAllTaxa(self):
        if debug: print "Testing genotypeAllTaxa"
        arr = self.data.genotypeAllTaxa(0)
        self.assertIsInstance(arr,meta_byte_array)
    def test_allelePresenceForAllSites(self):
        if debug: print "Testing allelePresenceForAllSites"
        bitset_major = self.data.allelePresenceForAllSites(0,WHICH_ALLELE.Major)
        self.assertIsInstance(bitset_major,BitSet)
    def test_allelePresenceForSitesBlock(self):
        if debug: print "Testing allelePresenceForSitesBlock"
        arr = self.data.allelePresenceForSitesBlock(0,WHICH_ALLELE.Major,0,1)
        self.assertIsInstance(arr,meta_long_array)
    def test_haplotypeAllelePresenceForAllSites(self):
        if debug: print "Testing haplotypeAllelePresenceForAllSites"
        try:
            bitset_major = self.data.haplotypeAllelePresenceForAllSites(0,True,WHICH_ALLELE.Major)
            self.assertIsInstance(bitset_major,BitSet)
        except JavaException as e:
            self.assertTrue(is_instance_of(e.throwable, java_imports['UnsupportedOperationException']))
    def test_haplotypeAllelePresenceForAllTaxa(self):
        if debug: print "Testing haplotypeAllelePresenceForAllTaxa"
        try:
            bitset_major = self.data.haplotypeAllelePresenceForAllTaxa(0,True,WHICH_ALLELE.Major)
            self.assertIsInstance(bitset_major,BitSet)
        except JavaException as e:
            self.assertTrue(is_instance_of(e.throwable, java_imports['UnsupportedOperationException']))
    def test_haplotypeAllelePresenceForSitesBlock(self):
        if debug: print "Testing haplotypeAllelePresenceForSitesBlock"
        try:
            arr = self.data.haplotypeAllelePresenceForSitesBlock(0,True,WHICH_ALLELE.Major,
                                                        0,1)
            self.assertIsInstance(arr,meta_long_array)
        except JavaException as e:
            self.assertTrue(is_instance_of(e.throwable, java_imports['UnsupportedOperationException']))
    def test_genotypeAsString(self):
        if debug: print "Testing genotypeAsString"
        geno1 = self.data.genotypeAsString(0,0)
        geno2 = self.data.genotypeAsString(0,np.int8(0))
        self.assertIsInstance(geno1,metaString)
        self.assertIsInstance(geno2,metaString)
    def test_genotypeAsStringRange(self):
        if debug: print "Testing genotypeAsStringRange"
        genos = self.data.genotypeAsStringRange(0,0,1)
        self.assertIsInstance(genos,metaString)
    def test_genotypeAsStringRow(self):
        if debug: print "Testing genotypeAsStringRow"
        genos = self.data.genotypeAsStringRow(0)
        self.assertIsInstance(genos,metaString)
    def test_genotypeAsStringArray(self):
        if debug: print "Testing genotypeAsStringArray"
        arr = self.data.genotypeAsStringArray(0,0)
        self.assertIsInstance(arr[0],String)
    def test_referenceAllele(self):
        if debug: print "Testing referenceAllele"
        ref = self.data.referenceAllele(0)
        self.assertIsInstance(ref,metaByte)
    def test_referenceAlleles(self):
        if debug: print "Testing referenceAlleles"
        arr = self.data.referenceAlleles(0,1)
        self.assertIsInstance(arr,meta_byte_array)
    def test_referenceAlleleForAllSites(self):
        if debug: print "Testing referenceAlleleForAllSites"
        arr = self.data.referenceAlleleForAllSites()
        self.assertIsInstance(arr,meta_byte_array)
    def test_hasReference(self):
        if debug: print "Testing hasReference"
        self.assertFalse(self.data.hasReference())
    def test_isHeterozygous(self):
        if debug: print "Testing isHeterozygous"
        self.assertIsInstance(self.data.isHeterozygous(0,0),metaBoolean)
    def test_heterozygousCount(self):
        if debug: print "Testing heterozygousCount"
        self.assertIsInstance(self.data.heterozygousCount(0),metaInteger)
    def test_siteName(self):
        if debug: print "Testing siteName"
        self.assertIsInstance(self.data.siteName(0),metaString)
    def test_chromosomeSiteCount(self):
        if debug: print "Testing chromosomeSitecount"
        first_site_chrom = self.data.chromosome(0)
        count = self.data.chromosomeSiteCount(first_site_chrom)
        self.assertIsInstance(count,metaInteger)
    def test_firstLastSiteOfChromosome(self):
        if debug: print "Testing firstLastSiteOfChromosome"
        first_site_chrom = self.data.chromosome(0)
        endpoints = self.data.firstLastSiteOfChromosome(first_site_chrom)
        self.assertIsInstance(endpoints, meta_int_array)
    def test_numberOfTaxa(self):
        if debug: print "Testing numberOfTaxa"
        self.assertIsInstance(self.data.numberOfTaxa(), metaInteger)
    def test_positions(self):
        if debug: print "Testing positions"
        poslist = self.data.positions()
        self.assertIsInstance(poslist, PositionList)
    def test_chromosomalPosition(self):
        if debug: print "Testing chromosomalPosition"
        self.assertIsInstance(self.data.chromosomalPosition(0),metaInteger)
    def test_siteOfPhysicalPosition(self):
        if debug: print "Testing siteOfPhysicalPosition"
        site1 = self.data.siteOfPhysicalPosition(data_constants.SHORT_HMP_FILE_FIRST_POS,
                                                 Chromosome(data_constants.SHORT_HMP_FILE_FIRST_CHROM))
        site2 = self.data.siteOfPhysicalPosition(data_constants.SHORT_HMP_FILE_FIRST_POS,
                                                 Chromosome(data_constants.SHORT_HMP_FILE_FIRST_CHROM),
                                                 data_constants.SHORT_HMP_FILE_FIRST_SITENAME)
        self.assertEquals(site1,0)
        self.assertEqual(site1,site2)
    def test_physicalPosition(self):
        if debug: print "Testing physicalPositions"
        positions = self.data.physicalPositions()
        self.assertIsInstance(positions, meta_int_array)
    def test_chromosomeName(self):
        if debug: print "Testing chromosomeName"
        self.assertEquals(self.data.chromosomeName(0), data_constants.SHORT_HMP_FILE_FIRST_CHROM)
    def test_chromosome(self):
        if debug: print "Testing chromosome"
        chrom1 = self.data.chromosome(0)
        chrom2 = self.data.chromosome(data_constants.SHORT_HMP_FILE_FIRST_CHROM)
        self.assertEquals(chrom1.getName(), data_constants.SHORT_HMP_FILE_FIRST_CHROM)
        self.assertEqual(chrom1,chrom2)
    def test_chromosomes(self):
        if debug: print "Testing chromosomes"
        chroms = self.data.chromosomes()
        self.assertIsInstance(chroms,javaArray)
        self.assertIsInstance(chroms[0], Chromosome)
    def test_numChromosomes(self):
        if debug: print "Testing numChromosomes"
        self.assertIsInstance(self.data.numChromosomes(),metaInteger)
    def test_chromosomesOffsets(self):
        if debug: print "Testing chromosomesOffsets"
        arr = self.data.chromosomesOffsets()
        self.assertIsInstance(arr,meta_int_array)
    def test_siteScore(self):
        if debug: print "Testing siteScore"
        try:
            score = self.data.siteScore(0,0)
            self.assertIsInstance(score,metaInteger)
        except JavaException as e:
            self.assertTrue(is_instance_of(e.throwable, java_imports['IllegalStateException']))
    def test_siteScores(self):
        if debug: print "Testing siteScores"
        try:
            score = self.data.siteScores()
            self.assertIsInstance(score,metaInteger)
        except JavaException as e:
            self.assertTrue(is_instance_of(e.throwable, java_imports['IllegalStateException']))
    def test_hasDepth(self):
        if debug: print "Testing hasDepth"
        self.assertIsInstance(self.data.hasDepth(),metaBoolean)
    def test_hasSiteScores(self):
        if debug: print "Testing hasSiteScores"
        self.assertIsInstance(self.data.hasSiteScores(),metaBoolean)
    def test_siteScoreType(self):
        if debug: print "Testing siteScoreType"
        try:
            scoretype = self.data.siteScoreType()
            self.assertTrue(any(map(lambda x: scoretype.equals(x),
                                    self.data.SITE_SCORE_TYPE.__dict__.values())))
        except JavaException as e:
            self.assertTrue(is_instance_of(e.throwable, java_imports['NullPointerException']))
    def test_indelSize(self):
        if debug: print "Testing indelSize"
        self.assertIsInstance(self.data.indelSize(0),metaInteger)
    def test_isIndel(self):
        if debug: print "Testing isIndel"
        self.assertIsInstance(self.data.isIndel(0),metaBoolean)
    def test_isAllPolymorphic(self):
        if debug: print "Testing isAllPolymorphic"
        self.assertIsInstance(self.data.isAllPolymorphic(),metaBoolean)
    def test_isPolymorphic(self):
        if debug: print "Testing isPolymorphic"
        self.assertIsInstance(self.data.isPolymorphic(0),metaBoolean)
    def test_majorAllele(self):
        if debug: print "Testing majorAllele"
        self.assertIsInstance(self.data.majorAllele(0),metaByte)
    def test_majorAlleleAsString(self):
        if debug: print "Testing majorAlleleAsString"
        self.assertIsInstance(self.data.majorAlleleAsString(0),metaString)
    def test_minorAllele(self):
        if debug: print "Testing minorAllele"
        self.assertIsInstance(self.data.minorAllele(0),metaByte)
    def test_minorAlleleAsString(self):
        if debug: print "Testing minorAlleleAsString"
        self.assertIsInstance(self.data.minorAlleleAsString(0),metaString)
    def test_minorAlleles(self):
        if debug: print "Testing minorAlleles"
        self.assertIsInstance(self.data.minorAlleles(0),meta_byte_array)
    def test_alleles(self):
        if debug: print "Testing alleles"
        self.assertIsInstance(self.data.alleles(0), meta_byte_array)
    def test_minorAlleleFrequency(self):
        if debug: print "Testing minorAlleleFrequency"
        self.assertIsInstance(self.data.minorAlleleFrequency(0),metaDouble)
    def test_majorAlleleFrequency(self):
        if debug: print "Testing majorAlleleFrequency"
        self.assertIsInstance(self.data.majorAlleleFrequency(0),metaDouble)
    def test_taxa(self):
        if debug: print "Testing taxa"
        taxa = self.data.taxa()
        self.assertIsInstance(taxa, TaxaList)
    def test_taxaName(self):
        if debug: print "Testing taxaName"
        self.assertIsInstance(self.data.taxaName(0), metaString)
    def test_genomeVersion(self):
        if debug: print "Testing genomeVersion"
        try:
            version = self.data.genomeVersion()
            if version is not None:
                self.assertIsInstance(version, metaString)
        except JavaException as e:
            self.assertTrue(is_instance_of(e.throwable, java_imports['UnsupportedOperationException']))
    def test_isPositiveStrand(self):
        if debug: print "Testing isPositiveStrand"
        self.assertIsInstance(self.data.isPositiveStrand(0),metaBoolean)
    def test_compositeAlignments(self):
        if debug: print "Testing compositeAlignments"
        alns = self.data.compositeAlignments()
        exp_arr_type = javaArray.get_array_type(GenotypeTable)
        self.assertIsInstance(alns, exp_arr_type)
    def test_allelesSortedByFrequency(self):
        if debug: print "Testing allelesSortedByFrequency"
        arr = self.data.allelesSortedByFrequency(0)
        exp_arr_type = javaArray.get_array_type(javaPrimativeArray.get_array_type('int'))
        self.assertIsInstance(arr,exp_arr_type)
    def test_genosSortedByFrequency(self):
        if debug: print "Testing genosSortedByFrequency"
        arr = self.data.genosSortedByFrequency(0)
        self.assertIsInstance(arr[0][0],metaString)
        self.assertIsInstance(arr[1][0],metaInteger)
    def test_isPhased(self):
        if debug: print "Testing isPhased"
        self.assertIsInstance(self.data.isPhased(),metaBoolean)
    def test_retainsRareAlleles(self):
        if debug: print "Testing retainsRareAlleles"
        self.assertIsInstance(self.data.retainsRareAlleles(),metaBoolean)
    def test_alleleDefinitions(self):
        if debug: print "Testing alleleDefinitions"
        arr1 = self.data.alleleDefinitions()
        arr2 = self.data.alleleDefinitions(0)
        self.assertIsInstance(arr1[0][0], metaString)
        self.assertEqual(arr1[0][0], arr2[0])
    def test_diploidAsString(self):
        if debug: print "Testing diploidAsString"
        val = self.data.diploidAsString(0,np.int8(0))
        self.assertIsInstance(val,metaString)
    def test_maxNumAlleles(self):
        if debug: print "Testing maxNumAlleles"
        self.assertIsInstance(self.data.maxNumAlleles(), metaInteger)
    def test_totalGametesNonMissingForSites(self):
        if debug: print "Testing totalGametesNonMissingForSite"
        self.assertIsInstance(self.data.totalGametesNonMissingForSite(0), metaInteger)
    def test_totalNonMissingForSite(self):
        if debug: print "Testing totalNonMissingForSite"
        self.assertIsInstance(self.data.totalNonMissingForSite(0), metaInteger)
    def test_minorAlleleCount(self):
        if debug: print "Testing minorAlleleCount"
        self.assertIsInstance(self.data.minorAlleleCount(0), metaInteger)
    def test_majorAlleleCount(self):
        if debug: print "Testing majorAlleleCount"
        self.assertIsInstance(self.data.majorAlleleCount(0), metaInteger)
    def test_genoCount(self):
        if debug: print "Testing genoCount"
        arr = self.data.genoCounts()
        self.assertIsInstance(arr[0][0], metaString)
        self.assertIsInstance(arr[1][0], metaLong)
    def test_majorMinorCounts(self):
        if debug: print "Testing majorMinorCounts"
        arr = self.data.majorMinorCounts()
        self.assertIsInstance(arr[0][0], metaString)
        self.assertIsInstance(arr[1][0], metaLong)
    def test_totalGametesNonMissingForTaxon(self):
        if debug: print "Testing totalGametesNonMissingForTaxon"
        val = self.data.totalGametesNonMissingForTaxon(0)
        self.assertIsInstance(val, metaInteger)
    def test_heterozygousCountForTaxon(self):
        if debug: print "Testing heterozygousCountForTaxon"
        val = self.data.heterozygousCountForTaxon(0)
        self.assertIsInstance(val, metaInteger)
    def test_totalNonMissingForTaxon(self):
        if debug: print "Testing totalNonMissingForTaxon"
        val = self.data.totalNonMissingForTaxon(0)
        self.assertIsInstance(val, metaInteger)
    def test_depth(self):
        if debug: print "Testing depth"
        depth = self.data.depth()
        self.assertTrue(depth is None or isinstance(depth, AlleleDepth))
    def test_depthForAlleles(self):
        if debug: print "Testing depthForAlleles"
        try:
            arr = self.data.depthForAlleles(0,0)
            self.assertIsInstance(arr[0],metaInteger)
        except JavaException as e:
            self.assertTrue(is_instance_of(e.throwable, java_imports['NullPointerException']))
    def test_allelesBySortType(self):
        if debug: print "Testing allelesBySortType"
        arr = self.data.allelesBySortType(self.data.ALLELE_SORT_TYPE.Reference,0)
        self.assertTrue(arr is None or isinstance(arr, meta_byte_array))
    def test_allelePresenceForAllTaxa(self):
        if debug: print "Testing allelePresenceForAllTaxa"
        bitset = self.data.allelePresenceForAllTaxa(0, WHICH_ALLELE.Major)
        self.assertIsInstance(bitset, BitSet)
        
if __name__ == "__main__":
    debug = True
    unittest.main()
    TASSELbridge.stop()
