from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Byte import metaByte
from TASSELpy.utils.primativeArray import javaPrimativeArray
import numpy as np

java_imports = {'GenotypeMergeRule':'net/maizegenetics/dna/snp/genotypecall/GenotypeMergeRule'}

class GenotypeMergeRule(Object):
    """ Defines the methods for merging the calls from two taxa. The merge
    rules need to be defined at the level of genotypic calls and for read
    depth. In general, if depth is available, it will be used to merge
    """
    _java_name = java_imports['GenotypeMergeRule']
    @javaConstructorOverload(java_imports['GenotypeMergeRule'])
    def __init__(self, *args, **kwargs):
        pass
    def isMergePossible(self, *args):
        """ Whether merge is even possible

        Signatures:

        boolean isMergePossible()
        
        Returns:

        Whether merging is allowed
        """
        pass
    @javaOverload("mergeCalls",
                  (make_sig(['byte','byte'],'byte'),(metaByte, metaByte),
                   np.int8))
    def mergeCalls(self, *args):
        """ Merges diploid genotypic calls into one

        Signatures:

        byte mergeCalls(byte geno1, byte geno2)

        Arguments:

        geno1 -- genotype call of taxa 1
        geno2 -- genotype call of taxa 2

        Returns:

        Merged genotype call
        """
        pass
    @javaOverload("mergeWithDepth",
                  (make_sig(['byte[]','byte[]'],'byte[]'),
                   (javaPrimativeArray.get_array_type('byte'),
                    javaPrimativeArray.get_array_type('byte')),
                   lambda x: javaPrimativeArray.make_array_from_obj('byte',x)))
    def mergeWithDepth(self, *args):
        """ Merges sequencing depths of 2 taxa

        Signatures:

        byte[] mergeWithDepth(byte[] geno1depths, byte[] geno2depths)

        Arguments:

        geno1depths -- allele depths of taxa 1
        geno2depths -- allele depths of taxa 2

        Returns:

        merged depths
        """
        pass
    @javaOverload("callBasedOnDepth",
                  (make_sig(['byte[]'],'byte'), (javaPrimativeArray.get_array_type('byte'),),
                   np.int8))
    def callBasedOnDepth(self, *args):
        """ Makes a genotypic call based on allele depths

        Signatures:

        byte callBasedOnDepth(byte[] genoDepths)

        Arguments:

        genoDepths -- allele depth of taxa

        Returns:

        genotype call
        """
        pass
