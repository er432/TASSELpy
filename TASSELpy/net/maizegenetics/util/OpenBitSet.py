from TASSELpy.utils.Overloading import javaConstructorOverload
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.utils.helper import make_sig
from TASSELpy.net.maizegenetics.util.BitSet import BitSet
import numpy as np

## Dictionary to hold java imports
java_imports = {'BitSet':'net/maizegenetics/util/BitSet',
                'OpenBitSet':'net/maizegenetics/util/OpenBitSet'}

class OpenBitSet(BitSet):
    _java_name = java_imports['OpenBitSet']
    @javaConstructorOverload(java_imports['OpenBitSet'],
                (make_sig(['long'],'void'),(metaInteger,)),
                (make_sig([],'void'),()),
                (make_sig(['long[]','int'],'void'),(np.ndarray,metaInteger)),
                (make_sig(['long[]'],'void'),(np.ndarray,)),
                (make_sig([java_imports['BitSet']],'void'),(BitSet,)))
    def __init__(self, *args, **kwargs):
        """
        An "open" BitSet implementation that allows direct access to the array of words
        storing the bits

        Unlike java.util.bitset, the fact that bits are packed into an array of longs
        is part of the interface. This allows efficient implementation of other
        algorithms by someone other than the author. It also allows one to
        efficiently implement alternate serialization or interchange formats.

        OpenBitSet is faster than java.util.BitSet in most operations and *much* faster at
        calculating cardinality of sets and results of set operations. It can also handle
        sets of larger cardinality (up to 64*2**32-1

        The goals of OpenBitSet are the fastest implementation possible, and maximum code reuse.
        Extra safety and encapsulation may always be built on top, but if that's built in, the cost
        can never be removed (and hence people re-implement their own version in order to get better
        performance). If you want a "safe", totally encapsulated (and slower and limited) BitSet
        class (coward), use java.util.BitSet

        Signatures:

        OpenBitSet(BitSet cloneOBS)
        OpenBitSet(long[] bits)
        OpenBitSet(long[] bits, int numWords)
        OpenBitSet()
        OpenBitSet(long numBits)

        Arguments:

        numBits -- Specifies the OpenBitSet to be large enough to hold numBits
        bits -- The first 64 bits are in long[0], with bit index 0 at the least significant bit,
                and bit index 63 as the most significant. Given a bit index, the word containing it is
                long[index/64], and it is at bit number index index%64 within that word.
        numWords -- Should be less than bits.length, and any existing words in the array at postion
                    greater than numWords should be zero
        cloneOBS -- An instance of a class that implements the BitSet interface
        """
        pass
