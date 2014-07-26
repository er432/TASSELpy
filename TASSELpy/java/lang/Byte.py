from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.java.lang.Number import Number, metaNumber
from TASSELpy.java.lang.Integer import Integer, metaInteger
from TASSELpy.java.lang.String import metaString
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import javaObj
from TASSELpy.utils.DocInherit import DocInherit
from abc import ABCMeta
import numpy as np

java_imports = {'Byte':'java/lang/Byte',
                'String':'java/lang/String'}

class metaByte:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if C == np.int8:
            return True
        elif C == np.uint8:
            return True
        elif issubclass(C, Byte):
            return True
        else:
            return False
## Class for wrapping java type Byte
class Byte(Comparable, Number):
    """
    public final class Byte
    extends Number
    implements Comparable<Byte>

    The Byte class wraps a value of primitive type byte in an object.
    An object of type Byte contains a single field whose type is byte.

    In addition, this class provides several methods for converting a
    byte to a String and a String to a byte, as well as other constants and
    methods useful when dealing with a byte.
    """
    _java_name = java_imports['Byte']
    @javaConstructorOverload(java_imports['Byte'],
                             (make_sig(['byte'],'void'),(metaByte,)),
                             (make_sig([java_imports['String']],'void'),(metaString,)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Byte object

        Signatures:

        Byte(byte value)
        Byte(String s)

        Arguments:

        Byte(byte value)
           value -- a byte value
        Byte(String s)
           s -- the string to be converted to a Byte
        """
        super(Byte, self).__init__(*args, generic=(Byte,), **kwargs)
    @DocInherit
    @javaOverload("compareTo",
                  (make_sig([java_imports['Byte']],'int'),(metaByte,),None))
    def compareTo(self, *args):
        pass
    def __repr__(self):
        return "Byte(%d)" % self.byteValue()
    ###################################
    ## Numeric magic methods
    ###################################
    def __pos__(self):
        return Byte(+self.toPrimative())
    def __neg__(self):
        return Byte(-self.toPrimative())
    def __abs__(self):
        return Byte(abs(self.toPrimative()))
    def __invert__(self):
        return Byte(~self.toPrimative())
    def __floor__(self):
        return Byte(np.floor(self.toPrimative()))
    def __ceil__(self):
        return Byte(np.ceil(self.toPrimative()))
    ###################################
    ## Arithmetic magic methods
    ###################################
    def __add__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() + other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() + other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() + other.toPrimative())
            else:
                return Byte(self.toPrimative() + other)
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() - other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() - other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() - other.toPrimative())
            else:
                return Byte(self.toPrimative() - other)
    def __rsub__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative()-self.toPrimative()))
            else:
                return Integer(np.int32(other-self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(other.toPrimative()-self.toPrimative())
            else:
                return Byte(other-self.toPrimative())
    def __isub__(self, other):
        return self.__sub__(other)
    def __mul__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() * other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() * other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() * other.toPrimative())
            else:
                return Byte(self.toPrimative() * other)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        return self.__mul__(other)
    def __floordiv__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() // other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() // other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() // other.toPrimative())
            else:
                return Byte(self.toPrimative() // other)
    def __rfloordiv__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() // self.toPrimative()))
            else:
                return Integer(np.int32(other // self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(other.toPrimative() // self.toPrimative())
            else:
                return Byte(other // self.toPrimative())
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
    def __div__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() / other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() / other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() / other.toPrimative())
            else:
                return Byte(self.toPrimative() / other)
    def __rdiv__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() / self.toPrimative()))
            else:
                return Integer(np.int32(other / self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(other.toPrimative() / self.toPrimative())
            else:
                return Byte(other/self.toPrimative())
    def __idiv__(self, other):
        return self.__div__(other)
    def __mod__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() % other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() % other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() % other.toPrimative())
            else:
                return Byte(self.toPrimative() % other)
    def __rmod__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() % self.toPrimative()))
            else:
                return Integer(np.int32(other % self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(other.toPrimative() % self.toPrimative())
            else:
                return Byte(other % self.toPrimative())
    def __imod__(self, other):
        return self.__mod__(other)
    def __pow__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() ** other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() ** other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() ** other.toPrimative())
            else:
                return Byte(self.toPrimative() ** other)
    def __rpow__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() ** self.toPrimative()))
            else:
                return Integer(np.int32(other ** self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(other.toPrimative() ** self.toPrimative())
            else:
                return Byte(other ** self.toPrimative())
    def __ipow__(self, other):
        return self.__pow__(other)
    def __lshift__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() << other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() << other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() << other.toPrimative())
            else:
                return Byte(self.toPrimative() << other)
    def __rlshift__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() << self.toPrimative()))
            else:
                return Integer(np.int32(other << self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(other.toPrimative() << self.toPrimative())
            else:
                return Byte(other << self.toPrimative())
    def __ilshift__(self, other):
        return self.__lshift__(other)
    def __rshift__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() >> other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() >> other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() >> other.toPrimative())
            else:
                return Byte(self.toPrimative() >> other)
    def __rrlshift__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(other.toPrimative() >> self.toPrimative()))
            else:
                return Integer(np.int32(other >> self.toPrimative()))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(other.toPrimative() >> self.toPrimative())
            else:
                return Byte(other >> self.toPrimative())
    def __irshift__(self, other):
        return self.__rshift__(other)
    def __and__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() & other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() & other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() & other.toPrimative())
            else:
                return Byte(self.toPrimative() & other)
    def __rand__(self, other):
        return self.__and__(other)
    def __iand__(self, other):
        return self.__and__(other)
    def __or__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() | other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() | other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() | other.toPrimative())
            else:
                return Byte(self.toPrimative() | other)
    def __ror__(self, other):
        return self.__or__(other)
    def __ior__(self, other):
        return self.__or__(other)
    def __xor__(self, other):
        if isinstance(other, metaInteger):
            if isinstance(other, Number):
                return Integer(np.int32(self.toPrimative() ^ other.toPrimative()))
            else:
                return Integer(np.int32(self.toPrimative() ^ other))
        elif isinstance(other, metaNumber):
            if isinstance(other, Number):
                return Byte(self.toPrimative() ^ other.toPrimative())
            else:
                return Byte(self.toPrimative() ^ other)
    def __rxor__(self, other):
        return self.__xor__(other)
    def __ixor__(self, other):
        return self.__xor__(other)
    @DocInherit
    def toPrimative(self):
        return self.byteValue()
