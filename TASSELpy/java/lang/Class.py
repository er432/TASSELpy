from TASSELpy.java.lang.Object import Object
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.utils.Overloading import javaGenericOverload
from TASSELpy.javaObj import genericJavaObj

java_imports = {'Class':'java/lang/Class',
                'Object':'java/lang/Object',
                'String':'java/lang/String'}

class Class(Object):
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
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Class, with specification of bracketed type
        """
        super(Class, self).__init__(*args, **kwargs)
    @javaGenericOverload("cast",
                         (make_sig([java_imports['Object']],java_imports['Object']),
                          (Object,)'/@1/'))
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
                  (make_sig([],None),(),None))
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
