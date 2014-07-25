from TASSELpy.utils.helper import make_sig
from TASSELpy.net.maizegenetics.dna.snp.CoreGenotypeTable import CoreGenotypeTable
import javabridge

## Dictionary to hold the imports required from Java
java_imports = {'ImportUtils':'net/maizegenetics/dna/snp/ImportUtils',
                    'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                    'String':'java/lang/String'}
class ImportUtils:
    ## Reads in a file after guessing its format
    # @param fileName The name of the file
    # @return A GenotypeTable
    @staticmethod
    def readGuessFormat(fileName):
        """
        Reads in a file after guessing its format

        Arguments:

        fileName -- The name of the file

        Returns:

        A GenotypeTable
        """
        ## Get the method signature
        method_args = [java_imports['String']]
        method_sig = make_sig(method_args,java_imports['GenotypeTable'])
        ## Get the java version of the object
        genoTable = javabridge.static_call("L%s;" % java_imports['ImportUtils'],
                                           "readGuessFormat",method_sig,
                                           fileName)
        # Convert to Python object and return
        return CoreGenotypeTable(obj=genoTable)
