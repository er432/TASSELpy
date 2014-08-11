from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import String
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaStaticOverload, javaConstructorOverload
from TASSELpy.utils.primativeArray import meta_byte_array
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.javaObj import javaArray
from TASSELpy.java.lang.Integer import metaInteger

java_imports = {'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
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
                         (make_sig(['byte[]','int'],'int[][]'),(meta_byte_array, metaInteger),
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
    # TODO: finish class
