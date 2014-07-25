from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Long import metaLong
from TASSELpy.utils.Overloading import javaOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray, meta_long_array
from TASSELpy.utils.helper import make_sig
import numpy as np
import javabridge

java_imports = {'BitSet':'net/maizegenetics/util/BitSet'}

## Class that is only used to subclass BitSet so that it can be referred
# to as a type within BitSet
class MetaBitSet(Object):
    pass

class BitSet(MetaBitSet):
    _java_name = java_imports['BitSet']
    ## Returns capacity
    # @return capacity
    @javaOverload("capacity",
                  (make_sig([],'long'),(),None))
    def capacity(self, *args):
        """
        Returns capacity

        Returns:

        Capacity
        """
        pass
    ## Returns the current capacity of this set. Included for
    # compatibility. This is not equal to cardinality
    @javaOverload("size",
                  (make_sig([],'long'),(),None))
    def size(self, *args):
        """
        Returns the current capacity of this set. Included for
        compatibility. This is not equal to cardinality
        """
        pass
    @javaOverload("isEmpty",
                  (make_sig([],'boolean'),(),None))
    ## Returns true if there are no set bits
    def isEmpty(self, *args):
        """
        Returns true if there are no set bits
        """
        pass
    ## Expert: returns the long[] storing the bits
    @javaOverload("getBits",
                  (make_sig([],"long[]"),(),
                   lambda x: javaPrimativeArray.make_array_from_obj('long',x)),
                  (make_sig(['int','int'],'long[]'),(metaInteger,metaInteger),
                   lambda x: javaPrimativeArray.make_array_from_obj('long',x)),
                  (make_sig(['int'],'long'),(metaInteger,),None))
    def getBits(self, *args):
        """
        Expert: returns the long[] storing the bits

        Signatures:

        getBits()
        getBits(int startWord, int endWord)
        getBits(int index)
        
        Arguments:
           Second method:
              startWord -- integer for first word
              endWord -- integer for last word
           Third method:
              index -- index
        """
        pass
    ## Expert: sets a new long[] to use as the bit storage
    # @param bits long[] to use as the bit storage
    @javaOverload("setBits",
                  (make_sig(["long[]"],"void"),(meta_long_array,),None))
    def setBits(self, *args):
        """
        Expert: sets a new long[] to use as the bit storage

        Arguments:

        bits -- long[] to use as the bit storage
        """
        pass
    ## Expert: sets specified word with given bits
    # @param wordNum word index
    # @param bits bits
    @javaOverload("setLong",
                  (make_sig(['int','long'],'void'),(metaInteger,metaLong),None))
    def setLong(self, *args):
        """
        Expert: sets the specified word with given bits

        Arguments:

        wordNum -- word index
        bits -- bits
        """
        pass
    ## Expert: gets the number of longs in the array that
    # are in use
    @javaOverload("getNumWords",
                  (make_sig([],'int'),(),None))
    def getNumWords(self, *args):
        """
        Expert: gets the number of longs in the array that
        are in use
        """
        pass
    @javaOverload("setNumWords",
                  (make_sig(['int'],'void'),(metaInteger,),None))
    ## Expert: sets the number of longs in the array that are in use
    # @param nWords The number of longs in the array that should be in use
    def setNumWords(self, *args):
        """
        Expert: sets the number of longs in the array that are in use

        Arguments:

        nWords -- The number of longs in the array that should be in use
        """
        pass
    ## Returns true or false for the specified bit index
    # @param index index
    @javaOverload("get",
              (make_sig(['long'],'boolean'),(metaLong,),None),
              (make_sig(['int'],'boolean'),(metaInteger,),None))
    def get(self, *args):
        """
        Returns true or false for the specified bit index

        Signatures:

        get(int index)
        get(long index)
        
        Arguments:

        index -- index (long or int)
        """
        pass
    ## Returns true or false for the specified bit index
    # @param The index should be less than the BitSet size
    @javaOverload("fastGet",
                  (make_sig(['long'],'boolean'),(metaLong,),None),
                  (make_sig(['int'],'boolean'),(metaInteger,),None))
    def fastGet(self, *args):
        """
        Returns true or false for the specified bit index

        Signatures:

        fastGet(int index)
        fastGet(long index)
        
        Arguments:

        index -- index (long or int), should be less than the BitSet size
        """
        pass
    ## Returns 1 if the bit is set, 0 if not
    # @param index, should be less than the BitSet size
    @javaOverload("getBit",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def getBit(self, *args):
        """
        Returns 1 if the bit is set, 0 if not

        Arguments:

        index -- index, should be less than the BitSet size
        """
        pass
    ## Sets a bit, expanding the set size if necessary
    # @param index index (long)
    @javaOverload("set",
                  (make_sig(['long'],'void'),(metaLong,),None),
                  (make_sig(['long','long'],'void'),(metaLong,metaLong),None))
    def set(self, *args):
        """
        Sets a bit, expanding the set size if necessary

        Signatures:

        set(long index)
        set(long startIndex, long endIndex)
        
        Arguments:

        index -- index (long)
        startIndex -- lower index (long)
        endIndex -- one-past the last bit to set (long)
        """
        pass
    ## Sets the bit at the specified index.
    # The index should be less than the bitset size
    # @param index index (long)
    @javaOverload("fastSet",
                  (make_sig(['int'],'void'),(metaInteger,),None),
                  (make_sig(['long'],'void'),(metaLong,),None))
    def fastSet(self, *args):
        """
        Sets the bit at the specified index. The
        index should be less than the BitSet size

        Signatures:

        fastSet(int index)
        fastSet(long index)
        
        Arguments:

        index -- index (long or int)
        """
        pass
    ## Clears a bit.
    # The index should be less than the BitSet size
    # @param index index
    @javaOverload("fastClear",
                  (make_sig(['int'],'void'),(metaInteger,),None),
                  (make_sig(['long'],'void'),(metaLong,),None))
    def fastClear(self, *args):
        """
        Clears a bit
        The index should be less than the BitSet size

        Signatures:

        fastClear(int index)
        fastClear(long index)
        
        Arguments:

        index -- index (long or int)
        """
        pass
    ## Clears a bit or range of bits, allowing access beyond the current set
    # size without changing the size
    # @param index index to clear
    # @param startIndex lower index
    # @param endIndex one-past the last bit to clear
    @javaOverload("clear",
                  (make_sig(['long'],'void'),(metaLong,),None),
                  (make_sig(['int','int'],'void'),(metaInteger,metaInteger),None),
                  (make_sig(['long','long'],'void'),(metaLong,metaLong),None))
    def clear(self,*args):
        """
        Clears a bit or range of bits, allowing access beyond the current set
        size without changing the size

        Signatures:

        clear(long index)
        clear(int startIndex, int endIndex)
        clear(long startIndex, long endIndex)

        Arguments:
           clear(long index)
              index -- The index to clear
           clear(int startIndex, int endIndex)
           clear(long startIndex, long endIndex)
              startIndex -- lower index
              endIndex -- one-past the last bit to clear
        """
        pass
    ## Sets a bit and returns the previous value.
    # The index should be less than the BitSet size
    # @param index The index to clear and view (long or int)
    # @return The previous value of the bit
    @javaOverload("getAndSet",
                  (make_sig(['int'],'boolean'),(metaInteger,),None),
                  (make_sig(['long'],'boolean'),(metaLong,),None))
    def getAndSet(self, *args):
        """
        Sets a bit and returns the previous value.
        The index should be less than the BitSet size

        Signatures:

        getAndSet(int index)
        getAndSet(long index)

        Arguments:

        index -- The index to clear and view (long or int)

        Returns:

        The previous value of the bit
        """
        pass
    ## Flips a bit.
    # The index should be less than the BitSet size
    # @param index The index of the bit to flip
    @javaOverload("fastFlip",
                  (make_sig(['int'],'void'),(metaInteger,),None),
                  (make_sig(['long'],'void'),(metaLong,),None))
    def fastFlip(self, *args):
        """
        Flips a bit.
        The index should be less than the BitSet size

        Signatures:

        fastFlip(int index)
        fastFlip(long index)

        Arguments:
        
        index -- The index of the bit to flip (long or int)
        """
        pass
    ## Flips a bit, expanding the set size if necessary
    # @param index The index to flip
    # @param startIndex lower index
    # @param endIndex one-past the last bit to flip
    @javaOverload("flip",
                  (make_sig(['long'],'void'),(metaLong,),None),
                  (make_sig(['long','long'],'void'),(metaLong,metaLong),None))
    def flip(self, *args):
        """
        Flips a bit, expanding the set size if necessary

        Signatures:

        flip(long index)
        flip(long startIndex, long endIndex)

        Arguments:
           flip(long index)
              index -- The index to flip
           flip(long startIndex, long endIndex)
              startIndex -- lower index
              endIndex -- one-past the last bit to flip
        """
        pass
    ## Flips a bit and returns the resulting bit value.
    # The index should be less than the BitSet size
    # @param index The index to flip and get
    # @return The bit in the state to which it was just flipped
    @javaOverload("flipAndGet",
                  (make_sig(['int'],'boolean'),(metaInteger,),None),
                  (make_sig(['long'],'boolean'),(metaLong,),None))
    def flipAndGet(self, *args):
        """
        Flips a bit and returns the resulting bit value.
        The index should be less than the BitSet size

        Signatures:

        flipAndGet(int index)
        flipAndGet(long index)

        Arguments:

        index -- The index to flip and get

        Returns:

        The bit in the state to which it was just flipped
        """
        pass
    ## Returns number of set bits (up to and including bit
    # at given index)
    # @param index index
    # @return The number of set bits
    @javaOverload("cardinality",
                  (make_sig([],'long'),(),None),
                  (make_sig(['int'],'long'),(metaInteger,),None))
    def cardinality(self, *args):
        """
        Returns number of set bits

        Signatures:

        long cardinality()
        long cardinality(int index)

        Arguments:
           long cardinality(int index):
              index -- index

        Returns:

        The number of set bits
        """
        pass
    ## Returns the index of the first set bit starting at the
    # index specified. -1 is returned if there are no more set
    # bits
    # @param index - index
    # @return The next set bit
    @javaOverload("nextSetBit",
                  (make_sig(['long'],'long'),(metaLong,),None),
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def nextSetBit(self, *args):
        """
        Returns the index of the first set bit starting at the
        index specified. -1 is returned if there are no more set
        bits

        Signatures:

        long nextSetBit(long index)
        int nextSetBit(int index)

        Arguments:

        index -- index (long or int)

        Returns:

        The next set bit
        """
        pass
    ## Returns the index of the previous set bit starting at
    # the index specified. If the bit at the index is set, index
    # is returned, otherwise the next lower numbered set bit
    # is returned. -1 is returned if there are no more set bits
    # @param index index
    # @return The previous set bit
    @javaOverload("previousSetBit",
                  (make_sig(['long'],'long'),(metaLong,),None),
                  (make_sig(['int'],'int'),(metaInteger,),None))
    def previousSetBit(self, *args):
        """
        Returns the index of the previous set bit starting at
        the index specified. If the bit at the index is set, index
        is returned, otherwise the next lower numbered set bit
        is retuned. -1 is returned if there are no more set bits

        Signatures:

        long previousSetBit(long index)
        int previousSetBit(int index)
        
        Arguments:

        index -- index

        Returns:

        The previous set bit
        """
        pass
    ## this = this AND other
    # @param other Another BitSet instance
    @javaOverload("intersect",
                  (make_sig([java_imports['BitSet']],'void'),(MetaBitSet,),None))
    def intersect(self, *args):
        """
        this = this AND other

        Signatures:

        void intersect(BitSet other)
        
        Arguments:

        other -- Another BitSet instance
        """
        pass
    ## this = this OR other
    # @param other Another BitSet instance
    @javaOverload("union",
                  (make_sig([java_imports['BitSet']],'void'),(MetaBitSet,),None))
    def union(self, *args):
        """
        this = this OR other

        Signatures:

        void union(BitSet other)
        
        Arguments:

        other -- Another BitSet instance
        """
        pass
    ## Remove all elements set in other. this = this AND_NOT other
    # @param other Another BitSet instance
    @javaOverload("remove",
                  (make_sig([java_imports['BitSet']],'void'),(MetaBitSet,),None))
    def remove(self, *args):
        """
        Remove all elements set in other. this = this AND_NOT other

        Signatures:

        void remove(BitSet other)

        Arguments:

        other -- Another BitSEt instance
        """
        pass
    ## this = this XOR other
    # @param other Another BitSet instance
    @javaOverload("xor",
                  (make_sig([java_imports['BitSet']],'void'),(MetaBitSet,),None))
    def xor(self, *args):
        """
        this = this XOR other

        Signatures:

        void xor(BitSet other)
        
        Arguments:

        other -- Another BitSet instance
        """
        pass
    ## this = this AND other
    # @param other Another BitSet instance
    @javaOverload("and",
                  (make_sig([java_imports['BitSet']],'void'),(MetaBitSet,),None))
    def _and(self, *args):
        """
        this = this AND other

        Signatures:

        void xor(BitSet other)
        
        Arguments:

        other -- Another BitSet instance
        """
        pass
    ## this = this OR other
    # @param other Another BitSet instance
    @javaOverload("or",
                  (make_sig([java_imports['BitSet']],'void'),(MetaBitSet,),None))
    def _or(self, *args):
        """
        this = this OR other

        Signatures:

        void or(BitSet other)
        
        Arguments:

        other -- Another BitSet instance
        """
        pass
    ## this = this ANDNOT other
    # @param other Another BitSet instance
    @javaOverload("andNot",
                  (make_sig([java_imports['BitSet']],'void'),(MetaBitSet,),None))
    def andNot(self, *args):
        """
        this = this ANDNOT other

        Signatures:

        void xor(BitSet other)
        
        Arguments:

        other -- Another BitSet instance
        """
        pass
    ## Returns true if the sets have any elements in common
    # @param other Another BitSet instance
    # @return Whether the sets have any elements in common
    @javaOverload("intersects",
                  (make_sig([java_imports['BitSet']],'boolean'),(MetaBitSet,),None))
    def intersects(self,*args):
        """
        Returns true if the sets have any elements in common

        Signatures:

        boolean intersects(BitSet other)

        Arguments:

        other -- Another BitSet instance
        """
        pass
    ## Expand the long[] with the size given as a number of words (64 bit longs).
    # getNumWords() is unchanged by this call
    # @param numWords The number of words to expand the long[] by
    @javaOverload("ensureCapacityWords",
                  (make_sig(['int'],'void'),(metaInteger,),None))
    def ensureCapacityWords(self, *args):
        """
        Expand the long[] with the size given as a number of words (64 bit longs).
        getNumWords() is unchanged by this call

        Signatures:

        void ensureCapacityWords(int numWords)

        Arguments:

        numWords -- The number of words to expand the long[] by
        """
        pass
    ## Ensure that the long[] is big enough to hold numBits, expanding it
    # if necessary. getNumWords() is unchanged by this call.
    # @param numBits The number of bits the BitSet should be able to hold
    @javaOverload("ensureCapacity",
                  (make_sig(['long'],'void'),(metaLong,),None))
    def ensureCapacity(self, *args):
        """
        Ensure that the long[] is big enough to hold numBits, expanding it
        if necessary. getNumWords() is unchanged by this call

        Signatures:

        void ensureCapacity(long numBits)

        Arguments:

        numBits -- The number of bits the BitSet should be able to hold
        """
        pass
    ## Lowers numWords, the number of words in use, by checking for trailing
    # zero words
    @javaOverload("trimTrailingZeros",
                  (make_sig([],'void'),(),None))
    def trimTrailingZeros(self, *args):
        """
        Lowers numWords, the number of words in use, by checking for trailing
        zero words

        Signatures:

        void trimTrailingZeros()
        """
        pass
    @javaOverload("indexOfNthSetBit",
                  (make_sig(['int'],'int'),(metaInteger,),None))
    ## Returns index of the nth set bit.
    # @param n nth set bit
    def indexOfNthSetBit(self, *args):
        """
        Returns index of the nth set bit

        Arguments:

        n -- nth set bit
        """
        pass
    ## Returns the indices of set bits
    # @return indices
    @javaOverload("getIndicesOfSetBits",
                  (make_sig([],'int[]'),(),
                   lambda x: javabridge.get_env().get_int_array_elements(x)))
    def getIndicesOfSetBits(self, *args):
        """
        Returns the indices of set bits
        """
        pass
