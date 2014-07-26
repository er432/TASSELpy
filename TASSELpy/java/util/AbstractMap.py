from TASSELpy.java.lang.Object import Object
from TASSELpy.java.util.Map import Map
from TASSELpy.utils.Overloading import javaConstructorOverload
from TASSELpy.utils.helper import make_sig

java_imports = {'AbstractMap':'java/util/AbstractMap'}

class AbstractMap(Map, Object):
    """
    public abstract class AbstractMap<K,V>
    extends Object
    implements Map<K,V>
    This class provides a skeletal implementation of the Map interface, to minimize the effort required to implement this interface.
    To implement an unmodifiable map, the programmer needs only to extend this class and provide an implementation for the entrySet method, which returns a set-view of the map's mappings. Typically, the returned set will, in turn, be implemented atop AbstractSet. This set should not support the add or remove methods, and its iterator should not support the remove method.

    To implement a modifiable map, the programmer must additionally override this class's put method (which otherwise throws an UnsupportedOperationException), and the iterator returned by entrySet().iterator() must additionally implement its remove method.

    The programmer should generally provide a void (no argument) and map constructor, as per the recommendation in the Map interface specification.

    The documentation for each non-abstract method in this class describes its implementation in detail. Each of these methods may be overridden if the map being implemented admits a more efficient implementation.

    This class is a member of the Java Collections Framework.
    """
    _java_name = java_imports['AbstractMap']
    @javaConstructorOverload(java_imports['AbstractMap'])
    def __init__(self, *args, **kwargs):
        """
        Sole constructor
        """
        super(AbstractMap,self).__init__(*args, **kwargs)
