from TASSELpy.java.util.FilterList import FilterList
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.javaObj import javaObj
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.java.lang.Object import Object
from TASSELpy.utils.primativeArray import javaPrimativeArray

java_imports = {'String': 'java/lang/String',
                'Tags': 'net/maizegenetics/dna/tag/Tags',
                'Boolean': 'java/lang/Boolean'}


class Tags(Object):
    _java_name = java_imports['Tags']

    @javaConstructorOverload(java_imports['Tags'])
    def __init__(self, *args, **kwargs):
        super(Tags, self).__init__(*args, **kwargs)

    ## Returns TaxaSize

    #Returns the number of longs use to represent the sequence
    #@return
    @javaOverload("getTagSizeInLong",
                  (make_sig([], 'int'), (), None))
    def getTagSizeInLong(self, *args):
        """
        Returns a polyA string of length 32*getTagSizeInLong()

        Signatures:

        int getTagSizeInLong()

        Returns:

        the number of longs use to represent the sequence
        """
        pass

    #Returns a polyA string of length 32*getTagSizeInLong()
    #@return
    @javaOverload("getNullTag",
                  (make_sig([], java_imports['String']), (), None))
    def getNullTag(self, *args):
        """
        Returns a polyA string of length 32*getTagSizeInLong()

        Signature:

        String getNullTag()

        Return:

        a polyA string of length 32*getTagSizeInLong()
        """
        pass

    #Returns the length in bp of a particular tag
    #@param index
    #@return length
    @javaOverload("getTagLength",
                  (make_sig(['int'], java_imports['int']), (int,), None))
    def getTagLength(self, *args):
        """
        Returns the length in bp of a particular tag

        Signature:

        int getTagLength(int index)

        Argument:

        index -- index

        Return:

        int length
        """
        pass

    #Get the compressed read sequence in a long array for a given index
    #@param index
    #@return compressed read sequence in long array
    @javaOverload("getTag",
                  (make_sig(['int'], 'long[]'), (metaInteger,), lambda x: javaPrimativeArray.make_array_from_obj(x)))
    def getTag(self, *args):
        """
        Get the compressed read sequence in a long array for a given index

        Signature:

        long[] getTag(int index)

        Argument:

        index -- index

        Return:

        long array: compressed read sequence
        """
        pass

    #Gets the first index of a read (the only one if a unique list).
    #If the read is not found then it return
    #a negative value indicating its insertion point.
    #@param read as a compressed long array
    #@return index of the read in the array
    @javaOverload("getTagIndex",
                  (make_sig(['long[]'], 'int'), (metaInteger,), None))
    def getTagIndex(self, *args):
        """
        Gets the first index of a read (the only one if a unique list).
        If the read is not found then it return
        a negative value indicating its insertion point.

        Signature:

        int getTagIndex(long[] read)

        Argument:

        read -- param read as a compressed long array

        Return

        int index of the read in the array

        """
        pass

    #Gets the set indices of matching reads (the only one if a unique list).
    #If the read is not found then it returns a null array
    #indicating its insertion point.
    #@param read as a compressed long array
    #@return set of indices of the read in the array (or null)
    @javaOverload("getTagIndexSet",
                  (make_sig(['long[]'], 'int[]'), (metaInteger,), lambda x: javaPrimativeArray.make_array_from_obj(x)))
    def getTagIndexSet(self, *args):
        """
        Gets the set indices of matching reads (the only one if a unique list).
        If the read is not found then it returns a null array
        indicating its insertion point.

        Argument:

        long[] -- index read as a compressed long array

        Return:

        int[] -- set of indices of the read in the array (or null)"""
        pass

    #Reports whether this list of reads includes duplicates
    #True is there are no read duplicates, false otherwise.
    #Collapses read files are likely to be unique
    #While a virtual digest of a genome with contain some duplicates
    #@return whether tags are unique
    @javaOverload("areTagsUnique",
                  (make_sig([], java_imports['Boolean']), (), None))
    def areTagsUnique(self, *args):
        """
        Reports whether this list of reads includes duplicates
        True is there are no read duplicates, false otherwise.
        Collapses read files are likely to be unique

        Signature:

        boolean areTagsUnique()

        Return:

        boolean
            True -- no duplicate
            False -- otherwise

        """
        pass

    #This is the number of different tags in the list (NOT THE SUM OF THE COUNTS)
    #The index will vary from 0 to (ReadTotal-1)
    #This is the number of distinct tags if readUnique is true
    #@return total number of tags
    @javaOverload("getTagCount", (make_sig([], 'int'), (), None))
    def getTagCount(self, *args):
        """
        This is the number of different tags in the list (NOT THE SUM OF THE COUNTS)
        The index will vary from 0 to (ReadTotal-1)
        This is the number of distinct tags if readUnique is true

        Signature:

        public int getTagCount();

        Return:

        int -- tagCount

        """
        pass




