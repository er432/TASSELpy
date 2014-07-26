from TASSELpy.java.lang.Object import Object
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.utils.helper import make_sig
from abc import ABCMeta
import numpy as np

java_imports = {'Number':'java/lang/Number'}

class metaNumber:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C,np.number):
            return True
        elif any(map(lambda x: issubclass(C,x),(int, long, float))):
            return True
        elif issubclass(C, Number):
            return True
        else:
            return False
## Wrapper class for java Number abstract class
class Number(Object):
    """
    The abstact class Number is the superclass of classes BigDecimal,
    BigInteger, Byte, Double, Float, Integer, Long, and Short

    Subclasses of Number must provide methods to convert represented
    numeric value to byte, double float, int, long, and short
    """
    _java_name = java_imports['Number']
    @javaConstructorOverload(java_imports['Number'],
                             (make_sig([],'void'),()))
    def __init__(self, *args, **kwargs):
        pass
    ## Returns the value of the specified number as a byte
    # @return The numeric value represented by this object after conversion to type byte
    @javaOverload("byteValue",
                  (make_sig([],'byte'),(),np.int8))
    def byteValue(self, *args):
        """
        Returns the value of the specified number as a byte

        Signatures:

        byte byteValue()

        Returns:

        The numeric value represented by this object after conversion to type byte
        """
        pass
    ## Returns the value of the specified number as a double
    # @return The numeric value represented by this object after conversion to type double
    @javaOverload("doubleValue",
                  (make_sig([],'double'),(),np.float64))
    def doubleValue(self, *args):
        """
        Returns the value of the specified number as a double

        Signatures:

        double doubleValue()

        Returns:

        The numeric value represented by this object after conversion to type double
        """
        pass
    ## Returns the value of the specified number as a float
    # @return The numeric value represented by this object after conversion to type float
    @javaOverload("floatValue",
                  (make_sig([],'float'),(),np.float32))
    def floatValue(self, *args):
        """
        Returns the value of the specified number as a float

        Signatures:

        float floatValue()

        Returns:

        The numeric value represented by this object after conversion to type float
        """
        pass
    ## Returns the value of the specified number as a int
    # @return The numeric value represented by this object after conversion to type int
    @javaOverload("intValue",
                  (make_sig([],'int'),(),np.int32))
    def intValue(self, *args):
        """
        Returns the value of the specified number as a int

        Signatures:

        int intValue()

        Returns:

        The numeric value represented by this object after conversion to type int
        """
        pass
    ## Returns the value of the specified number as a long
    # @return The numeric value represented by this object after conversion to type long
    @javaOverload("longValue",
                  (make_sig([],'long'),(),np.int64))
    def longValue(self, *args):
        """
        Returns the value of the specified number as a long

        Signatures:

        long longValue()

        Returns:

        The numeric value represented by this object after conversion to type long
        """
        pass
    ## Returns the value of the specified number as a short
    # @return The numeric value represented by this object after conversion to type short
    @javaOverload("shortValue",
                  (make_sig([],'short'),(),np.int16))
    def shortValue(self, *args):
        """
        Returns the value of the specified number as a short

        Signatures:

        short shortValue()

        Returns:

        The numeric value represented by this object after conversion to type short
        """
        pass
    ## Returns the primative value (a numpy type) for this object
    # @return The numpy type for this object
    def toPrimative(self):
        """
        Returns the primative value (a numpy type) for this object

        Returns:

        The numpy type for this object
        """
        pass
    ###################################
    ## Comparison magic methods
    ###################################
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.toPrimative() == other.toPrimative()
        elif isinstance(other, metaNumber):
            return self.toPrimative() == other
        else:
            raise NotImplementedError
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if isinstance(other, Number):
            return self.toPrimative() < other.toPrimative()
        elif isinstance(other, metaNumber):
            return self.toPrimative() < other
        else:
            raise NotImplementedError
    def __gt__(self, other):
        if isinstance(other, Number):
            return self.toPrimative() > other.toPrimative()
        elif isinstance(other, metaNumber):
            return self.toPrimative() > other
        else:
            raise NotImplementedError
    def __le__(self, other):
        if isinstance(other, Number):
            return self.toPrimative() <= other.toPrimative()
        elif isinstance(other, metaNumber):
            return self.toPrimative() <= other
        else:
            raise NotImplementedError
    def __ge__(self, other):
        if isinstance(other, Number):
            return self.toPrimative() >= other.toPrimative()
        elif isinstance(other, metaNumber):
            return self.toPrimative() >= other
        else:
            raise NotImplementedError
    ###################################
    ## Type conversion magic methods
    ###################################
    def __int__(self):
        return int(self.toPrimative())
    def __long__(self):
        return long(self.toPrimative())
    def __float__(self):
        return float(self.toPrimative())
    def __complex__(self):
        return complex(self.toPrimative())
    def __oct__(self):
        return oct(self.toPrimative())
    def __hex__(self):
        return hex(self.toPrimative())
    def __str__(self):
        return str(self.toPrimative())
