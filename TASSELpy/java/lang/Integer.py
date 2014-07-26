from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.java.lang.String import metaString
from TASSELpy.java.lang.Number import Number, metaNumber
from TASSELpy.java.lang.Long import Long,metaLong
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.DocInherit import DocInherit
from abc import ABCMeta
import numpy as np

java_imports = {'Integer':'java/lang/Integer',
                'String':'java/lang/String'}

class metaInteger:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if C == np.int32:
            return True
        elif C == np.uint32:
            return True
        elif issubclass(C,Integer):
            return True
        elif issubclass(C, int):
            return True
        else:
            return False
## Class for wrapping java type Integer
class Integer(Comparable, Number):
    """
    public final class Integer
    extends Number
    implements Comparable<Integer>

    The Integer class wraps a value of primitive type int in an object.
    An object of type Integer contains a single field whose type is int.

    In addition, this class provides several methods for converting a
    int to a String and a String to a int, as well as other constants and
    methods useful when dealing with a int.
    """
    _java_name = java_imports['Integer']
    @javaConstructorOverload(java_imports['Integer'],
                             (make_sig(['int'],'void'),(metaInteger,)),
                             (make_sig([java_imports['String']],'void'),(metaString,)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Integer object

        Signatures:

        Integer(int value)
        Integer(String s)

        Arguments:

        Integer(int value)
           value -- a int value
        Integer(String s)
           s -- the string to be converted to a Integer
        """
        super(Integer, self).__init__(*args, generic=(Integer,), **kwargs)
    @DocInherit
    @javaOverload("compareTo",
                  (make_sig([java_imports['Integer']],'int'),(metaInteger,),None))
    def compareTo(self, *args):
        pass
    ###################################
    ## Numeric magic methods
    ###################################
    def __pos__(self):
        return Integer(+self.toPrimative())
    def __neg__(self):
        return Integer(-self.toPrimative())
    def __abs__(self):
        return Integer(abs(self.toPrimative()))
    def __invert__(self):
        return Integer(~self.toPrimative())
    def __floor__(self):
        return Integer(np.floor(self.toPrimative()))
    def __ceil__(self):
        return Integer(np.ceil(self.toPrimative()))
    ###################################
    ## Arithmetic magic methods
    ###################################
    def __add__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() + other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() + other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() + other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() + other))
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() - other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() - other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() - other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() - other))
    def __rsub__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(other.toPrimative() - self.toPrimative()))
            else:
                return Long(np.int64(other-self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative()-self.toPrimative()))
            else:
                return Integer(np.int32(other-self.toPrimative()))
    def __isub__(self, other):
        return self.__sub__(other)
    def __mul__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() * other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() * other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() * other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() * other))
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        return self.__mul__(other)
    def __floordiv__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() // other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() // other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() // other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() // other))
    def __rfloordiv__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(other.toPrimative() // self.toPrimative()))
            else:
                return Long(np.int64(other // self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() // self.toPrimative()))
            else:
                return Integer(np.int32(other // self.toPrimative()))
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
    def __div__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() / other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() / other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() / other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() / other))
    def __rdiv__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(other.toPrimative() / self.toPrimative()))
            else:
                return Long(np.int64(other / self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() / self.toPrimative()))
            else:
                return Integer(np.int32(other / self.toPrimative()))
    def __idiv__(self, other):
        return self.__div__(other)
    def __mod__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() % other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() % other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() % other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() % other))
    def __rmod__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(other.toPrimative() % self.toPrimative()))
            else:
                return Long(np.int64(other % self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() % self.toPrimative()))
            else:
                return Integer(np.int32(other % self.toPrimative()))
    def __imod__(self, other):
        return self.__mod__(other)
    def __pow__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() ** other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() ** other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() ** other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() ** other))
    def __rpow__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(other.toPrimative() ** self.toPrimative()))
            else:
                return Long(np.int64(other ** self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() ** self.toPrimative()))
            else:
                return Integer(np.int32(other ** self.toPrimative()))
    def __ipow__(self, other):
        return self.__pow__(other)
    def __lshift__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() << other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() << other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() << other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() << other))
    def __rlshift__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(other.toPrimative() << self.toPrimative()))
            else:
                return Long(other << np.int64(self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() << self.toPrimative()))
            else:
                return Integer(np.int32(other << self.toPrimative()))
    def __ilshift__(self, other):
        return self.__lshift__(other)
    def __rshift__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() >> other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() >> other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() >> other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() >> other))
    def __rrlshift__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(other.toPrimative() >> self.toPrimative()))
            else:
                return Long(other >> np.int64(self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() >> self.toPrimative()))
            else:
                return Integer(np.int32(other >> self.toPrimative()))
    def __irshift__(self, other):
        return self.__rshift__(other)
    def __and__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() & other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() & other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() & other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() & other))
    def __rand__(self, other):
        return self.__and__(other)
    def __iand__(self, other):
        return self.__and__(other)
    def __or__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() | other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() | other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() | other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() | other))
    def __ror__(self, other):
        return self.__or__(other)
    def __ior__(self, other):
        return self.__or__(other)
    def __xor__(self, other):
        if isinstance(other, metaLong):
            if isinstance(other, metaNumber):
                return Long(np.int64(self.toPrimative() ^ other.toPrimative()))
            else:
                return Long(np.int64(self.toPrimative() ^ other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() ^ other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() ^ other))
    def __rxor__(self, other):
        return self.__xor__(other)
    def __ixor__(self, other):
        return self.__xor__(other)
    def __repr__(self):
        return "Integer(%d)" % self.intValue()
    @DocInherit
    def toPrimative(self):
        return self.intValue()
