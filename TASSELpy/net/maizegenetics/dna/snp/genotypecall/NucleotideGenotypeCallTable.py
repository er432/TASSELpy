from TASSELpy.net.maizegenetics.dna.snp.genotypecall import GenotypeCallTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
import javabridge

# Dictionary to hold java objects
java_imports = {'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
		'SuperByteMatrix':'net/maizegenetics/util/SuperByteMatrix',
		'GenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/
		GeneotypeCallTable',
		'ByteGenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/	
		ByteGenotypeCallTable',
		'NucleotideGenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/	
		NucleotideGenotypeCallTable',
		'NucleotideAlignmentConstants':'net/maizegenetics/dna/snp/
		NucleotideAlignmentConstants/',
		'String':'java/lang/String'}


"""

"""
class NucleotideGenotypeCallTable(java_imports['ByteGenotypeCallTable']):
	@javaConstructorOverload(java_imports['NucleotideGenotypeCallTable'],
	(make_sig([java_imports['SuperByteMatrix'], 'boolean'], 'void'),
	(object, boolean)))
	
"""
Instantiates the class
"""
	def __init__(self, *args):
		pass