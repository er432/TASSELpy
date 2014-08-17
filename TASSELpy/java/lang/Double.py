from TASSELpy.java.lang.Number import Number, metaNumber
from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.java.lang.String import metaString
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import javaObj
from TASSELpy.utils.DocInherit import DocInherit
from abc import ABCMeta
import numpy as np

java_imports = {'Double':'java/lang/Double',
                'String':'java/lang/String'}

class metaDouble:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if C == np.float64:
            return True
        elif C == np.longdouble:
            return True
        elif issubclass(C,Double):
            return True
        else:
            return False

class Double(Comparable, Number):
    """
    public final class Double
    extends Number
    implements Comparable<Double>

    The Double class wraps a value of primitive type double in an object.
    An object of type Double contains a single field whose type is double.

    In addition, this class provides several methods for converting a double to
    a String and a String to a double, as well as other constants and methods useful
    when dealing with a double.
    """
    _java_name = java_imports['Double']
    @javaConstructorOverload(java_imports['Double'],
                (make_sig(['double'],'void'),(metaDouble,)),
                (make_sig([java_imports['String']],'void'),(metaString,)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Double object

        Signatures:

        Double(double value)
        Double(String s)

        Arguments:

        Double(double value)
            value -- A double value
        Double(String s)
            s -- The string to be converted to a Double
        """
        super(Double, self).__init__(*args, generic=(Double,), **kwargs)
    @javaOverload("compareTo",
                  (make_sig([java_imports['Double']],'int'),(metaDouble,),None))
    def compareTo(self, *args):
        pass        
    @DocInherit
    def toPrimative(self):
        return self.doubleValue()        
    ###################################
    ## Numeric magic methods
    ###################################
    def __pos__(self):
        return Double(+self.toPrimative())
    def __neg__(self):
        return Double(-self.toPrimative())
    def __abs__(self):
        return Double(abs(self.toPrimative()))
    def __invert__(self):
        return Double(~self.toPrimative())
    def __floor__(self):
        return Double(np.floor(self.toPrimative()))
    def __ceil__(self):
        return Double(np.ceil(self.toPrimative()))
    ###################################
    ## Arithmetic magic methods
    ###################################
    def __add__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() + other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() + other))
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() - other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() - other))
    def __rsub__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(other.toPrimative() - self.toPrimative()))
        else:
            return Double(np.float64(other-self.toPrimative()))
    def __isub__(self, other):
        return self.__sub__(other)
    def __mul__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() * other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() * other))
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        return self.__mul__(other)
    def __floordiv__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() // other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() // other))
    def __rfloordiv__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(other.toPrimative() // self.toPrimative()))
        else:
            return Double(np.float64(other // self.toPrimative()))
    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
    def __div__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() / other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() / other))
    def __rdiv__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(other.toPrimative() / self.toPrimative()))
        else:
            return Double(np.float64(other / self.toPrimative()))
    def __idiv__(self, other):
        return self.__div__(other)
    def __mod__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() % other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() % other))
    def __rmod__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(other.toPrimative() % self.toPrimative()))
        else:
            return Double(np.float64(other % self.toPrimative()))
    def __imod__(self, other):
        return self.__mod__(other)
    def __pow__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() ** other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() ** other))
    def __rpow__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(other.toPrimative() ** self.toPrimative()))
        else:
            return Double(np.float64(other ** self.toPrimative()))
    def __ipow__(self, other):
        return self.__pow__(other)
    def __lshift__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() << other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() << other))
    def __rlshift__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(other.toPrimative() << self.toPrimative()))
        else:
            return Long(other << np.float64(self.toPrimative()))
    def __ilshift__(self, other):
        return self.__lshift__(other)
    def __rshift__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() >> other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() >> other))
    def __rrlshift__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(other.toPrimative() >> self.toPrimative()))
        else:
            return Long(other >> np.float64(self.toPrimative()))
    def __irshift__(self, other):
        return self.__rshift__(other)
    def __and__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() & other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() & other))
    def __rand__(self, other):
        return self.__and__(other)
    def __iand__(self, other):
        return self.__and__(other)
    def __or__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() | other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() | other))
    def __ror__(self, other):
        return self.__or__(other)
    def __ior__(self, other):
        return self.__or__(other)
    def __xor__(self, other):
        if isinstance(other, Number):
            return Double(np.float64(self.toPrimative() ^ other.toPrimative()))
        else:
            return Double(np.float64(self.toPrimative() ^ other))
    def __rxor__(self, other):
        return self.__xor__(other)
    def __ixor__(self, other):
        return self.__xor__(other)
    def __repr__(self):
        return "Double(%0.5g)" % self.doubleValue()
