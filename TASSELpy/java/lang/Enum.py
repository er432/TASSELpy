from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.javaObj import javaObj
from TASSELpy.utils.helper import make_sig
from abc import ABCMeta
import javabridge

java_imports = {'Enum':'java/lang/Enum',
                'Object':'java/lang/Object',
                'String':'java/lang/String'}

## Base class only used to refer to enum type with Enum
class metaEnum:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C, Enum):
            return True
        else:
            return False

class Enum(Object):
    """
    This is the common base class of all Java language enumeration types.
    """
    _java_name = java_imports['Enum']
    def __repr__(self):
        return "Enum(%s: %d)" % (self.name(), self.ordinal())
    @javaConstructorOverload(java_imports['Enum'])
    def __init__(self, *args, **kwargs):
        """
        Instantiates the common base class of all Java language
        enumeration types.

        There is no explicit constructor. Only an object can be
        pass in
        """
        pass
    ## Compares this enum with the specified object for order
    @javaOverload("compareTo",
                  (make_sig([java_imports['Enum']],'int'),(metaEnum,),None))
    def compareTo(self, *args):
        """
        Compares this enum with the specified object for order
        
        Signatures:
        int compareTo(Enum o)

        Arguments:

        The object to compare to
        """
        pass
    ## Returns true if the specified object is equal to this enum constant
    # @param other The object you want to test for equality
    # @return Whether object is equal to enum constant
    @javaOverload("equals",
                  (make_sig([java_imports['Object']],'boolean'),(javaObj,),None))
    def equals(self, *args):
        """
        Returns true if the specified object is equal to this enum constant

        Signatures:

        boolean equals(Object other)

        Arguments:

        other -- the object you want to test for equality

        Returns:

        Whether object is equal to enum constant
        """
        pass
    ## Returns the name of this enum constant, exactly as declared in
    # its enum declaration
    # @return The name of the enum constant
    @javaOverload("name",
                  (make_sig([],java_imports['String']),(),None))
    def name(self, *args):
        """
        Returns the name of this enum constant, exactly as declared
        in its enum declaration

        Signatures:

        String name()

        Returns:

        The name of this enum constant
        """
        pass
    ## Returns the ordinal of this enumeration constant (its position in
    # its enum declaration, where the initial constant is assigned an
    # ordinal of zero
    # @return Oridinal of this enumeration constant
    @javaOverload("ordinal",
                  (make_sig([],'int'),(),None))
    def ordinal(self, *args):
        """
        Returns the ordinal of this enumeration constant (its position in
        its enum declaration, where the initial constant is assigned an
        ordinal of zero

        Signatures:

        int ordinal()

        Returns:

        Ordinal of this enumeration constant
        """
        pass
    ## Returns the name of this enum constant, as contained in the
    # declaration
    # @return The name of this enum constant
    @javaOverload("toString",
                  (make_sig([],java_imports['String']),(),None))
    def toString(self, *args):
        """
        Returns the name of this enum constant, as contained in the
        declaration

        Signatures:

        String toString()

        Returns:

        The name of this enum constant
        """
        pass

class enum(object):
    """
    Class used to declare wrapper enums like in Java

    Example:

    my_enum = enum("path/to/MY_ENUM","FIRST","SECOND","THIRD")
    """
    def __init__(self, enum_name, *args, **kwargs):
        """
        Instantiates an enum. Each constant becomes a class attribute
        that is an instance of the Enum class

        Arguments:

        enum_name -- The path to the enum in Java (e.g. "path/to/class$MY_ENUM")
        args -- The constant names
        subclass -- Optional name of subclass to given constant instances
        """
        self.subclass = Enum
        if 'subclass' in kwargs:
            self.subclass = type(kwargs['subclass'],(Enum,),{})
        for arg in args:
            if 'subclass' in kwargs:
                setattr(self,arg,
                        self.subclass(obj=javabridge.get_static_field(enum_name,
                                arg,"L%s;" % enum_name)))
            else:
                setattr(self,arg,
                        Enum(obj=javabridge.get_static_field(enum_name,
                        arg,
                        "L%s;" % enum_name)))
    def __repr__(self):
        tuples = [(k,v) for k,v in self.__dict__.iteritems() if isinstance(v,self.subclass)]
        tuples = sorted(tuples, key=lambda x: x[1].ordinal())
        return "<%s>" % ', '.join(["%s: %d" % (v.toString(), v.ordinal()) for k,v in \
                            tuples if isinstance(v,self.subclass)])
