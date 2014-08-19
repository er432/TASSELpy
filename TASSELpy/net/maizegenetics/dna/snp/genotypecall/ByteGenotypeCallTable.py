from TASSELpy.net.maizegenetics.dna.snp.genotypecall.AbstractGenotypeCallTable import AbstractGenotypeCallTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
import javabridge
import bumpy as np

# Dictionary to hold java imports
java_imports = {'ByteGenotypeCallTable':'net/maizegenetics/dna/dnp/genotypecall/ByteGenotypeCallTable'}

class ByteGenotypeCallTable(AbstractGenotypeCallTable):
    """ In memory byte implementation of GenotypeCallTable backed by the high
    efficiency SuperByteMatrix class. Although the GenotypeCallTable is accessed as a 2D array,
    for efficiency it is usually backed single dimension arrays with either site or taxa
    as the inner loop
    """
    _java_name = java_imports['ByteGenotypeCallTable']

