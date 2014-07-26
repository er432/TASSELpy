from TASSELpy.net.maizegenetics.dna.snp.genotypecall import GenotypeCallTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
import javabridge
import numpy as np




# Dictionary to hold java objects
java_imports = {'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
		'GenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/
		GeneotypeCallTable'
		'AbstractGenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/	
		AbstractGenotypeCallTable'
		'MaxNumAlleles':'net/maizegenetics/dna/snp/NucleotideAlignmentConstants/
		NUMBER_NUCLEOTIDE_ALLELES'}


class AbstractGenotypeCallTable(GenotypeCallTable):
	@javaConstructorOverload(java_imports['AbstractGenotypeCallTable'],
	(make_sig(['int', 'int', 'boolean', java_imports['String']+'[][],' 'int'], 'void'), (int, int, boolean, np.array, int)), 
	(make_sig(['int', 'int', 'boolean', java_imports['String']+'[][]'], 'void'), (int, int, boolean, np.array))
)
