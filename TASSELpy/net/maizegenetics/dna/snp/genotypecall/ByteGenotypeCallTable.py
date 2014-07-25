from TASSELpy.net.maizegenetics.dna.snp.genotypecall import GenotypeCallTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
import javabridge
import bumpy as np

# Dictionary to hold java imports
java_imports = {'SuperByteMatrix':'net/maizegenetics/util/SuperByteMatrix', 
		'SuperByteMatrixBuilder':'net/maizegenetics/util/SuperByteMatrixBulider',
		'AbstractGenotypeCallTable':'net/maizegenetics/dan/snp/genotypecall/
		AbstractGentotypeCallTable', 
		'ByteGenotypeCallTable':'net/maizegenetics/dna/dnp/genotypecall/
		ByteGenotypeCallTable', 
		'String':'java/lang/String'}

class ByteGenotypeCallTable(java_imports['AbstractGenotypeCallTable']):
	@javaConstructorOverload(java_imports['ByteGenotypeCallTable'],
	(make_sig(['np.int8'+'[][]', 'boolean', java_imports['String']+'[][]'], 'void'),
	(np.array,boolean, np.array)),
	(make_sig([java_imports['SuperByteMatrix'], 'boolean', java_imports['String']+'[][]'], 'void'), (object, boolean, np.array))
)

"""
Instantiates the class
"""
	def __init__(self, *args):
		pass
