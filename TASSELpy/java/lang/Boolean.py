from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import metaString
from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.DocInherit import DocInherit
from abc import ABCMeta

java_imports = {'Boolean':'java/lang/Boolean',
                'String': 'java/lang/String'}

class metaBoolean:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C,bool):
            return True
        elif issubclass(C,Boolean):
            return True
        else:
            return False
## Class for wrapping java type Boolean
class Boolean(Comparable, Object):
    """
    public final class Boolean
    extends Object
    implements Serializable, Comparable<Boolean>
    The Boolean class wraps a value of the primitive type boolean in an object.
    An object of type Boolean contains a single field whose type is boolean.

    In addition, this class provides many methods for converting a boolean to a String
    and a String to a boolean, as well as other constants and methods useful when dealing
    with a boolean.
    """
    _java_name = java_imports['Boolean']
    ## Instantiates a Boolean object
    @javaConstructorOverload(java_imports['Boolean'],
            (make_sig(['boolean'],'void'),(metaBoolean,)),
            (make_sig([java_imports['String']],'void'),(metaString,)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Boolean object

        Signatures:

        Boolean(boolean value)
        Boolean(String s)

        Arguments:

        Boolean(boolean value)
            value -- a boolean value
        Boolean(String s)
            s -- the string to be converted to a Boolean
        """
        super(Boolean, self).__init__(*args, generic=(Boolean,), **kwargs)
    @DocInherit
    @javaOverload("compareTo",
                  (make_sig([java_imports['Boolean']],'int'),(metaBoolean,),None))
    def compareTo(self, *args):
        pass
