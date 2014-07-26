from TASSELpy.net.maizegenetics.util.BitSet import BitSet
from TASSELpy.utils.Overloading import javaConstructorOverload,javaOverload,javaStaticOverload
from TASSELpy.utils.helper import make_sig

java_imports = {'BitSet':'net/maizegenetics/util/BitSet',
                'UnmodifiableBitSet':'net/maizegenetics/util/UnmodifiableBitSet'}
class UnmodifiableBitSet(BitSet):
    _java_name = java_imports['UnmodifiableBitSet']
    ## Instantiates UnmodifiableBitSet
    # @param obj A Java instance implementing BitSet interface
    @javaConstructorOverload(java_imports['UnmodifiableBitSet'])
    def __init__(self, *args, **kwargs):
        """
        Instantiates UnmodifiableBitSet

        Arguments:

        obj -- A Java instance implementing BitSet interface
        """
        pass
    ## Get instance of UnmodifiableBitSet from a BitSet
    # @param bitSet An instance of a BitSet
    # @return An UnmodifiableBitSet
    @javaStaticOverload(java_imports['UnmodifiableBitSet'],"getInstance",
            (make_sig([java_imports['BitSet']],java_imports['UnmodifiableBitSet']),(BitSet,),
             lambda x: UnmodifiableBitSet(obj=x)))
    def getInstance(*args):
        """
        Get instance of UnmodifiableBitSet from a BitSet

        Arguments:

        bitSet -- An instance of a BitSet

        Returns:

        An UnmodifiableBitSet
        """
        pass
