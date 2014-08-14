from TASSELpy.javaObj import javaObj
from TASSELpy.utils.Overloading import javaGenericOverload
from TASSELpy.javaObj import genericJavaObj
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
import javabridge

java_imports = {'Class':'java/lang/Class',
                'Object':'java/lang/Object',
                'String':'java/lang/String'}
class Object(javaObj):
    """
    Acts like Java.lang.Object
    """
    _java_name = java_imports['Object']
    ## Instantiates a Java Object
    @javaConstructorOverload(java_imports['Object'],
                             (make_sig([],'void'),()))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Java object

        Signatures:

        Object()
        """
        pass
    def castTo(self, pyType):
        """ Casts this object to another java/python type

        Parameters
        ----------
        pyType : Python type inheriting from javaObj

        Returns
        -------
        The object as an instance of the new type (in both java and python)
        """
        if not hasattr(pyType, '_java_name'):
            raise TypeError("pyType has no attribute _java_name")
        # Get the cast-to class
        cast_to_class = javabridge.class_for_name(pyType._java_name.replace('/','.'))
        cast_to_class = Class(obj=cast_to_class, generic=(pyType,))
        return cast_to_class.cast(self)
    ## Creates and returns a copy of this object
    # @return A copy of this object
    @javaOverload("clone",
            (make_sig([],java_imports['Object']),(),lambda x: Object(obj=x)))
    def clone(self, *args):
        """
        Creates and returns a copy of this object

        Signatures:

        protected Object clone()

        Returns:

        A copy of this object
        """
        pass
    ## Returns a string representation of the object
    # @return The string representation of the object
    @javaOverload("toString",
                  (make_sig([],java_imports['String']),(),None))
    def toString(self, *args):
        """
        Returns a string representation of the object

        Signatures:

        String toString()

        Returns:

        The string representaiton of the object
        """
        pass
    ## Indicates whether some other object is "equal to" this one
    # @param obj The object you want to test for equality
    # @return true if equal
    @javaOverload("equals",
                  (make_sig([java_imports['Object']],'boolean'),(javaObj,),None))
    def equals(self, *args):
        """
        Indicates whether some other object is "equal to" this one

        Signatures:

        boolean equals(Object obj)

        Arguments:

        obj -- The object you want to test for equality

        Returns:

        true if equal
        """
        pass
    ## Returns a hash code value for this object
    # @return Hash code value for this object
    @javaOverload("hashCode",
            (make_sig([],'int'),(),None))
    def hashCode(self, *args):
        """
        Returns a hash code vlaue for the object

        Signatures:

        int hashCode()

        Returns:

        Hash code value for this object
        """
        pass
    @javaOverload("getClass",
                  (make_sig([],java_imports['Class']),
                   (), lambda x: Class(obj=x)))
    def getClass(self, *args):
        """ Returns the runtime class of this Object.

        Signatures:

        final Class<?> getClass()

        Returns:

        The Class object that represents the runtime class of this object
        """
        pass
    #################
    # Python magic methods
    #################
    def __eq__(self, other):
        if isinstance(other, javaObj):
            return self.equals(other)
        else:
            return False
    def __hash__(self):
        return self.hashCode()
    def __str__(self):
        return self.toString()

class Class(genericJavaObj, Object):
    """
    public final class Class<T>
    extends Object
    implements Serializable, GenericDeclaration, Type, AnnotatedElement

    Instances of the class Class represent classes and interfaces in a
    running Java application. An enum is a kind of class and an annotation
    is a kind of interface. Every array also belongs to a class that is
    reflected as a Class object that is shared by all arrays with the same
    element type and number of dimensions. The primitive Java types (boolean,
     byte, char, short, int, long, float, and double), and the keyword void
    are also represented as Class objects.

    Class has no public constructor. Instead Class objects are constructed
    automatically by the Java Virtual Machine as classes are loaded and
    by calls to the defineClass method in the class loader.
    """
    _java_name = java_imports['Class']
    @javaConstructorOverload(java_imports['Class'])
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Class, with specification of bracketed type
        """
        super(Class, self).__init__(*args, **kwargs)
    @javaGenericOverload("cast",
                         (make_sig([java_imports['Object']],java_imports['Object']),
                          (Object,),'/@1/'))
    def cast(self, *args):
        """ Casts an object to the class or interface represented by this Class
        object

        Signatures:

        T cast(Object obj)

        Arguments:

        obj -- the object to be cast

        Returns:

        The object after casting, or null if the object is null
        """
        pass
    @javaOverload("getName",
                  (make_sig([],java_imports['String']),(),None))
    def getName(self, *args):
        """
        Returns the name of the entity (class, interface, array class, primitive type,
        or void) represented by this Class object, as a String.

        If this class object represents a class of arrays, then the internal form
        of the name consists of the name of the element type preceded by one or more
        '[' characters representing the depth of the array nesting.

        Signatures:

        String getName()
        
        Returns:

        The name of the class or interface represented by this object
        """
        pass
    @javaOverload("isPrimitive",
                  (make_sig([],'boolean'),(),None))
    def isPrimitive(self, *args):
        """ Determines if the specified Class object represents a primitive type.

        Signatures:

        boolean isPrimitive()

        Returns:

        true if and only if this class represents a primitive type
        """
        pass
    @javaGenericOverload("newInstance",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def newInstance(self, *args):
        """ Creates a new instance of the class represented by this Class object.
        The class is instantiated as if by a new expression with an empty argument
        list. The class is initialized if it has not already been initialized.

        Signatures:

        T newInstance()

        Returns:

        A newly allocated instance of the class represented by this object
        """
        pass
