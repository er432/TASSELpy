from TASSELpy.java.lang.Object import Object
from TASSELpy.utils.helper import make_sig
from TASSELpy.java.lang.String import metaString
from TASSELpy.utils.Overloading import javaStaticOverload, javaConstructorOverload
from TASSELpy.net.maizegenetics.dna.snp.CoreGenotypeTable import CoreGenotypeTable
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.java.lang.Boolean import metaBoolean
import javabridge

## Dictionary to hold the imports required from Java
java_imports = {'ImportUtils':'net/maizegenetics/dna/snp/ImportUtils',
                    'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                    'ProgressListener':'net/maizegenetics/util/ProgressListener',
                    'String':'java/lang/String'}
class ImportUtils(Object):
    _java_name = java_imports['ImportUtils']
    @javaConstructorOverload(java_imports['ImportUtils'])
    def __init__(self, *args, **kwargs):
        pass
    @javaStaticOverload(java_imports['ImportUtils'],"readGuessFormat",
                        (make_sig([java_imports['String']],java_imports['GenotypeTable']),
                         (metaString,), lambda x: GenotypeTable(obj=x)))
    def readGuessFormat(*args):
        """ Reads in a file after guessing its format

        Signatures:

        static GenotypeTable readGuessFormat(String fileName)
        
        Arguments:

        fileName -- The name of the file

        Returns:

        A GenotypeTable
        """
        pass
    @javaStaticOverload(java_imports['ImportUtils'],"readFromVCF",
                        (make_sig([java_imports['String'],java_imports['ProgressListener']],
                                  java_imports['GenotypeTable']), (metaString, Object),
                         lambda x: GenotypeTable(obj=x)),
                         (make_sig([java_imports['String'],java_imports['ProgressListener'],
                                    'boolean'],
                                   java_imports['GenotypeTable']), (metaString, Object, metaBoolean),
                         lambda x: GenotypeTable(obj=x)))
    def readFromVCF(*args):
        """ Reads from a VCF file

        Signatures:

        static GenotypeTable readFromVCF(final String filename, ProgressListener listener)
        static GenotypeTable readFromVCF(final String filename, ProgressListener listener,
                                         boolean ignoreDepth)

        Arguments:

        static GenotypeTable readFromVCF(final String filename, ProgressListener listener)
            filename -- The name of the file
            listener -- A progresslistener (can be null)
        static GenotypeTable readFromVCF(final String filename, ProgressListener listener,
                                         boolean ignoreDepth)
            filename -- The name of the file
            listener -- A progresslistener (can be null)
            ignoreDepth -- Whether to ignore depth information

        Returns:

        A GenotypeTable
        """
        pass
    @javaStaticOverload(java_imports['ImportUtils'],"readFromHapmap",
                        (make_sig([java_imports['String']],
                                  java_imports['GenotypeTable']), (metaString,),
                         lambda x: GenotypeTable(obj=x)),
                         (make_sig([java_imports['String'],java_imports['ProgressListener']],
                                   java_imports['GenotypeTable']), (metaString, Object),
                         lambda x: GenotypeTable(obj=x)))
    def readFromHapmap(*args):
        """ Read GenotypeTable from HapMap file

        Signatures:
        
        static GenotypeTable readFromHapmap(final String filename)
        static GenotypeTable readFromHapmap(final String filename, ProgressListener listener)

        Arguments:

        static GenotypeTable readFromHapmap(final String filename)
            filename -- The name of the file
        static GenotypeTable readFromHapmap(final String filename, ProgressListener listener)
            filename -- The name of the file
            listener -- A progresslistener (can be null)

        Returns:

        A GenotypeTable
        """
        pass
    @javaStaticOverload(java_imports['ImportUtils'],"readFromPLink",
                        (make_sig([java_imports['String'], java_imports['String'],
                                   java_imports['ProgressListener']],
                                   java_imports['GenotypeTable']),
                         (metaString, metaString, Object),
                         lambda x: GenotypeTable(obj=x)))
    def readFromPLink(*args):
        """ Read GenotypeTable from PLink files

        Signatures:

        static GenotypeTable readFromPLink(final String pedFilename,
                          final String mapFilename, ProgressListener listener)

        Arguments:

        static GenotypeTable readFromPLink(final String pedFilename,
                          final String mapFilename, ProgressListener listener)
            pedFilename -- The name of the ped file
            mapFilename -- The name of the map file
            listener -- A progresslistener (can be null)

        Returns:

        A GenotypeTable
        """
        pass
    @javaStaticOverload(java_imports['ImportUtils'], "readFasta",
                        (make_sig([java_imports['String']], java_imports['GenotypeTable']),
                         (metaString,), lambda x: GenotypeTable(obj=x)))
    def readFasta(*args):
        """ Read GenotypeTable from a fasta file

        Signatures:

        static GenotypeTable readFasta(String filename)

        Arguments:

        filename -- The name of the file

        Returns:

        A GenotypeTable
        """
        pass
