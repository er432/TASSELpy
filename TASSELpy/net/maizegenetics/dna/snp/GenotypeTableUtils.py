from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import String
from TASSELpy.net.maizegenetics.util.BitSet import BitSet
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaStaticOverload, javaConstructorOverload
from TASSELpy.utils.primativeArray import meta_byte_array
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.javaObj import javaArray
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.java.lang.Byte import metaByte

java_imports = {'BitSet':'net/maizegenetics/util/BitSet',
                'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'GenotypeTableUtils':'net/maizegenetics/dna/snp/GenotypeTableUtils',
                'Object':'java/lang/Object',
                'String':'java/lang/String'}

class GenotypeTableUtils(Object):
    """ Utility methods for comparing, sorting, and counting genotypes
    """
    @javaConstructorOverload(java_imports['GenotypeTableUtils'])
    def __init__(self, *args, **kwargs):
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getAllelesSortedByFrequency',
                        (make_sig(['byte[]'], 'int[][]'),(meta_byte_array,),
                         lambda x: javaPrimativeArray.get_array_type('int').wrap_existing_array(x)),
                         (make_sig(['byte[][]','int'],'int[][]'),(meta_byte_array, metaInteger),
                          lambda x: javaPrimativeArray.get_array_type('int').wrap_existing_array(x)),
                         (make_sig([java_imports['String']+'[][]','int'],java_imports['Object']+'[][]'),
                          (javaArray.get_array_type(javaArray.get_array_type(String)), metaInteger),
                           lambda x: javaArray.to_wrapped_array(x, pyType = javaArray.get_array_type(Object))),
                          (make_sig([java_imports['GenotypeTable'],'int'],'int[][]'),
                           (GenotypeTable, metaInteger),
                           lambda x: javaPrimativeArray.get_array_type('int').wrap_existing_array(x)))
    def getAllelesSortedByFrequency(*args):
        """ This sorts alleles by frequency.

        Each cell in the given array contains a diploid value which is separated
        and counted individually. Resulting double dimension array holds alleles (bytes)
        in result[0]. And the counts are in result[1]. Counts haploid values twice and
        diploid vlaues once. Higher ploidies are not supported

        Signatures:

        static int[][] getAllelesSortedByFrequency(byte[] data)
        static int[][] getAllelesSortedByFrequency(byte[][] data, int site)
        static Object[][] getAllelesSortedByFrequency(String[][] data, int site)
        static int[][] getAllelesSortedByFrequency(GenotypeTable alignment, int site)

        Arguments:

        static int[][] getAllelesSortedByFrequency(byte[] data)
            data -- data
        static int[][] getAllelesSortedByFrequency(byte[][] data, int site)
            data -- data
            site -- site
        static Object[][] getAllelesSortedByFrequency(String[][] data, int site)
            data -- data
            site -- site
        static int[][] getAllelesSortedByFrequency(GenotypeTable alignment, int site)
            alignment -- an alignment
            site -- site

        Returns:

        alleles and counts
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getAlleles',
                        (make_sig(['byte[][]','int'],'byte[]'),
                         (javaArray.get_array_type(javaPrimativeArray.get_array_type('byte')),
                        metaInteger), None))
    def getAlleles(*args):
        """ Gets the alleles at a site

        Signatures:

        static byte[] getAlleles(byte[][] data, int site)

        Arguments:

        data -- data
        site -- site

        Returns:

        Alleles at site
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getDiploidsSortedByFrequency',
                        (make_sig([java_imports['GenotypeTable'],'int'],
                                  java_imports['Object']+'[][]'),
                        (GenotypeTable, metaInteger),
                        lambda x: javaArray.to_wrapped_array(x, pyType = javaArray.get_array_type(Object))))
    def getDiploidsSortedByFrequency(*args):
        """ Gets the diploids sorted by frequency

        Signatures:

        static Object[][] getDiploidsSortedByFrequency(GenotypeTable alignment,
                                                       int site)


        Arguments:

        alignment -- alignment
        site -- site

        Returns:

        Diploids, sorted by frequency
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getAlleleStates',
                        (make_sig([java_imports['String']+'[][]','int'],
                                  java_imports['String']+'[][]'),
                        (javaArray.get_array_type(javaArray.get_array_type(String)),
                         metaInteger),
                        lambda x: javaArray.to_wrapped_array(x, pyType = javaArray.get_array_type(String))))
    def getAlleleStates(*args):
        """ Gets the String states of alleles

        Signatures:

        static String[][] getAlleleStates(String[][] data, int maxNumAlleles)

        Arguments:

        data -- data
        maxNumAlleles -- maximum number of alleles

        Returns:

        The allele states at all loci
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'], 'getDataBytes',
                        (make_sig([java_imports['String']+'[]'],'byte[][]'),
                         (javaArray.get_array_type(String),),
                        lambda x: javaArray.to_wrapped_array(x, pyType = javaPrimativeArray.get_array_type('byte'))),
                        (make_sig([java_imports['String']+'[][]', java_imports['String']+'[][]','int'],
                                  'byte[][]'), (javaArray.get_array_type(javaArray.get_array_type(String)),
                                                javaArray.get_array_type(javaArray.get_array_type(String)),
                                                metaInteger),
                        lambda x: javaArray.to_wrapped_array(x, pyType = javaPrimativeArray.get_array_type('byte'))))
    def getDataBytes(*args):
        """ Gets the data as bytes

        Signatures:

        static byte[][] getDataBytes(String[] data)
        static byte[][] getDataBytes(String[][] data, String[][] alleleStates,
                                     int maxNumAlleles)

        Arguments:

        static byte[][] getDataBytes(String[] data)
            data -- data
        static byte[][] getDataBytes(String[][] data, String[][] alleleStates,
                                     int maxNumAlleles)
            data -- data
            alleleStates -- allele states
            maxNumAlleles -- maximum number of alleles

        Returns:

        data as bytes
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],"removeSitesBasedOnFreqIgnoreMissing",
                        (make_sig([java_imports['GenotypeTable'], 'double',
                                   'double','int'], java_imports['GenotypeTable']),
                        (GenotypeTable, metaDouble, metaDouble, metaInteger),
                        lambda x: GenotypeTable(obj=x)))
    def removeSitesBasedOnFreqIgnoreMissing(*args):
        """ Remove sites based on minimum frequency (the count of good bases,
        INCLUDING GAPS) and based on the proportion of good alleles (including
        gaps) different from consensus

        Signatures:

        static GenotypeTable removeSitesBasedOnFreqIgnoreMissing(GenotypeTable aa,
                             double minimumProportion, double maximumProportion,
                             int minimumCount)

        Arguments:

        aa -- the AnnotatedAlignment to filter
        minimumProportion -- minimum proportion of sites different from the
                             consensus
        maxmimumProportion -- maximum proportion of sites different from the
                              consensus
        minimumCount -- minimum number of sequences with good bases (not N or ?),
                        where GAP IS CONSIDERED A GOOD BASE

        Returns:

        filtered GenotypeTable
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],"getIncludedSitesBasedOnFreqIgnoreMissing",
                        (make_sig([java_imports['GenotypeTable'], 'double',
                                   'double','int'], 'int[]'),
                        (GenotypeTable, metaDouble, metaDouble, metaInteger),
                        lambda x: javaPrimativeArray.make_array_from_obj('int', x)))
    def getIncludedSitesBasedOnFreqIgnoreMissing(*args):
        """ Get sites to be included based on minimum frequency (the count
        of good bases, INCLUDING GAPS) and based on the proportion of good
        sites (INCLUDING GAPS) different from consensus

        Signatures:

        static int[] getIncludedSitesBasedOnFreqIgnoreMissing(GenotypeTable aa,
                             double minimumProportion, double maximumProportion,
                             int minimumCount)

        Arguments:

        aa -- the AnnotatedAlignment to filter
        minimumProportion -- minimum proportion of sites different from the
                             consensus
        maximumProportion -- maximum proportion of sites different from the
                             consensus
        minimumCount -- minimum number of sequences with a good base or a
                        gap (but not N or ?)

        Returns:

        The sites to be included
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],"removeSitesOutsideRange",
                        (make_sig([java_imports['GenotypeTable'], 'int', 'int'],
                                  java_imports['GenotypeTable']), (GenotypeTable,
                                  metaInteger, metaInteger),
                        lambda x: GenotypeTable(obj=x)))
    def removeSitesOutsideRange(*args):
        """ Remove sites based on site position (excluded sites are <firstSite and
        > lastSite) This does not affect any prior exclusions

        Signatures:

        static GenotypeTable removeSitesOutsideRange(GenotypeTable aa,
                              int firstSite, int lastSite)

        Arguments:

        aa -- the AnnotatedAlignment to filter
        firstSite -- first site to keep in the range
        lastSite -- last site to keep in the range

        Returns:

        Filtered GenotypeTable
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'isHeterozygous',
                        (make_sig(['byte'],'boolean'),(metaByte,),None))
    def isHeterozygous(*args):
        """ Returns whether diploid allele values are heterozygous. First 4
        bits in byte is one allele value. Second 4 bits is other allele value

        Signatures:

        static boolean isHeterozygous(byte diploidAllele)

        Arguments:

        diploidAllele -- alleles

        Returns:

        true if allele values different; false if values the same
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'isEqual',
                        (make_sig(['byte[]','byte[]'],'boolean'),
                         (meta_byte_array, meta_byte_array), None),
                         (make_sig(['byte','byte'],'boolean'),
                          (metaByte, metaByte), None))
    def isEqual(*args):
        """ Returns whether two diploid allele values are equal, ignoring order

        Signatures:

        static boolean isEqual(byte[] alleles1, byte[] alleles2)
        static boolean isEqual(byte diploidAllele1, byte diploidAllele2)

        Arguments:

        static boolean isEqual(byte[] alleles1, byte[] alleles2)
            alleles1 -- diploid alleles 1
            alleles2 -- diploid alleles 2
        static boolean isEqual(byte diploidAllele1, byte diploidAllele2)
            diploidAllele1 -- diploid alleles 1
            diploidAllele2 -- diploid alleles 2

        Returns:

        true if equal
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'isEqualOrUnknown',
                        (make_sig(['byte[]','byte[]'],'boolean'),
                         (meta_byte_array, meta_byte_array), None),
                         (make_sig(['byte','byte'],'boolean'),
                          (metaByte, metaByte), None))
    def isEqualOrUnknown(*args):
        """ Returns whether two diploid allele values are equal, ignoring order,
        where unknown values equal anything

        Signatures:

        static boolean isEqualOrUnknown(byte[] alleles1, byte[] alleles2)
        static boolean isEqualOrUnknown(byte diploidAllele1, byte diploidAllele2)

        Arguments:

        static boolean isEqualOrUnknown(byte[] alleles1, byte[] alleles2)
            alleles1 -- diploid alleles 1
            alleles2 -- diploid alleles 2
        static boolean isEqualOrUnknown(byte diploidAllele1, byte diploidAllele2)
            diploidAllele1 -- diploid alleles 1
            diploidAllele2 -- diploid alleles 2

        Returns:

        true if equal
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'isPartiallyEqual',
                        (make_sig(['byte','byte'],'boolean'),
                         (metaByte, metaByte), None))
    def isPartiallyEqual(*args):
        """ Returns true if at least one allele agrees

        Signatures:

        static boolean isPartiallyEqual(byte genotype1, byte genotype2)

        Arguments:

        genotype1 -- genotype 1
        genotype2 -- genotype 2

        Returns:

        true if at least 1 allele is equal
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getDiploidValuePhased',
                        (make_sig(['byte','byte'],'byte'),(metaByte,metaByte),
                         None))
    def getDiploidValuePhased(*args):
        """ Combines 2 allele values into one diploid value. Assumed phased

        Signatures:

        static byte getDiploidValuePhased(byte a, byte b)

        Arguments:

        a -- allele 1
        b -- allele 2

        Returns:

        diploid value
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getDiploidValue',
                        (make_sig(['byte','byte'],'byte'),(metaByte,metaByte),
                         None))    
    def getDiploidValue(*args):
        """ Combines 2 allele values into 1 diploid value. Assumed phased

        Signatures:

        static byte getDiploidValue(byte a, byte b)

        Arguments:

        a -- allele 1
        b -- allele 2

        Returns:

        diploid value        
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getUnphasedDiploidValue',
                        (make_sig(['byte','byte'],'byte'),(metaByte,metaByte),
                         None))        
    def getUnphasedDiploidValue(*args):
        """ Combines 2 allele values into 1 diploid value. In alphabetical order.

        Signatures:

        static byte getUnphasedDiploidValue(byte a, byte b)

        Arguments:

        a -- allele 1
        b -- allele 2

        Returns:

        diploid value sorted by order A < C < G < T
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getUnphasedDiploidValueNoHets',
                        (make_sig(['byte','byte'],'byte'),(metaByte,metaByte),
                         None))            
    def getUnphasedDiploidValueNoHets(*args):
        """ Combines 2 genotype values into 1 diploid value. Returns unknown
        if either parent is heterozygous or unknown, or alleles are swapped.

        Signatures:

        static byte getUnphasedDiploidValueNoHets(byte g1, byte g2)

        Arguments:

        g1 -- genotype 1
        g2 -- genotype 2

        Returns:

        diploid value
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'getDiploidValues',
                        (make_sig(['byte'],'byte[]'),(metaByte,),
                         lambda x: javaPrimativeArray.wrap_existing_array('byte',x)))
    def getDiploidValues(*args):
        """ Separates diploid allele value into its two values.

        Signatures:

        static byte[] getDiploidValues(byte genotype)

        Arguments:

        genotype -- diploid value

        Returns:

        separated allele values
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableUtils'],'calcBitPresenceFromGenotype',
                        (make_sig(['byte[]','byte[]','byte[]'],java_imports['BitSet']+'[]'),
                         (meta_byte_array, meta_byte_array, meta_byte_array),
                        lambda x: javaArray.to_wrapped_array(x, pyType=BitSet)),
                        (make_sig(['byte[]','byte[]'],java_imports['BitSet']),
                         (meta_byte_array, meta_byte_array),
                        lambda x: BitSet(obj=x)),
                        (make_sig(['byte[]','byte','byte'],java_imports['BitSet']+'[]'),
                         (meta_byte_array, metaByte, metaByte),
                        lambda x: javaArray.to_wrapped_array(x, pyType=BitSet)),
                        (make_sig(['byte[]','byte'],java_imports['BitSet']),
                         (meta_byte_array, metaByte),
                        lambda x: BitSet(obj=x)))
    def calcBitPresenceFromGenotype(*args):
        """ Method for getting TBits rapidly from major and minor allele arrays

        Signatures:

        static BitSet[] calcBitPresenceFromGenotype(byte[] genotype,
                        byte[] mjA, byte[] mnA)
        static BitSet calcBitPresenceFromGenotype(byte[] genotype,
                        byte[] referenceValues)
        static BitSet[] calcBitPresenceFromGenotype(byte[] genotype,
                        byte mj, byte mn)
        static BitSet calcBitPresenceFromGenotype(byte[] genotype,
                        byte referenceValue)

        Arguments:

        static BitSet[] calcBitPresenceFromGenotype(byte[] genotype,
                        byte[] mjA, byte[] mnA)
            genotype -- genotype
            mjA -- major alleles
            mnA -- minor alleles
        static BitSet calcBitPresenceFromGenotype(byte[] genotype,
                        byte[] referenceValues)            
            genotype -- genotype
            referenceValues -- reference
        static BitSet[] calcBitPresenceFromGenotype(byte[] genotype,
                        byte mj, byte mn)
            genotype -- genotype
            mj -- major byte
            mn -- minor byte
        static BitSet calcBitPresenceFromGenotype(byte[] genotype,
                        byte referenceValue)
            genotype -- genotype
            referenceValue -- reference

        Returns:

        Tbits
        """
        pass
