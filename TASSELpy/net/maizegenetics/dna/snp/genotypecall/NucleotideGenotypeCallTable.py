from TASSELpy.net.maizegenetics.dna.snp.genotypecall.ByteGenotypeCallTable import ByteGenotypeCallTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
import javabridge

# Dictionary to hold java objects
java_imports = {
		'NucleotideGenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/NucleotideGenotypeCallTable',
		}

class NucleotideGenotypeCallTable(ByteGenotypeCallTable):
    """ In memory GenotypeCallTable for nucleotide data
    """
    _java_name = java_imports['NucleotideGenotypeCallTable']
