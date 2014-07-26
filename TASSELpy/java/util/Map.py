from TASSELpy.java.util.Collection import Collection
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.util.Set import Set
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload,javaGenericOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import genericJavaObj
from abc import ABCMeta

java_imports = {'Collection':'java/util/Collection',
                'Map':'java/util/Map',
                'Object':'java/lang/Object',
                'Set':'java/util/Set'}

class metaMap:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C, Map):
            return True
        else:
            return False

class Map(genericJavaObj, Object):
    """
    An object that maps keys to values. A map cannot contain duplicate keys; each key can map to at most one value.
    This interface takes the place of the Dictionary class, which was a totally abstract class rather than an interface.

    The Map interface provides three collection views, which allow a map's contents to be viewed as a set of keys, collection of values, or set of key-value mappings. The order of a map is defined as the order in which the iterators on the map's collection views return their elements. Some map implementations, like the TreeMap class, make specific guarantees as to their order; others, like the HashMap class, do not.

    Note: great care must be exercised if mutable objects are used as map keys. The behavior of a map is not specified if the value of an object is changed in a manner that affects equals comparisons while the object is a key in the map. A special case of this prohibition is that it is not permissible for a map to contain itself as a key. While it is permissible for a map to contain itself as a value, extreme caution is advised: the equals and hashCode methods are no longer well defined on such a map.

    All general-purpose map implementation classes should provide two "standard" constructors: a void (no arguments) constructor which creates an empty map, and a constructor with a single argument of type Map, which creates a new map with the same key-value mappings as its argument. In effect, the latter constructor allows the user to copy any map, producing an equivalent map of the desired class. There is no way to enforce this recommendation (as interfaces cannot contain constructors) but all of the general-purpose map implementations in the JDK comply.

    The "destructive" methods contained in this interface, that is, the methods that modify the map on which they operate, are specified to throw UnsupportedOperationException if this map does not support the operation. If this is the case, these methods may, but are not required to, throw an UnsupportedOperationException if the invocation would have no effect on the map. For example, invoking the putAll(Map) method on an unmodifiable map may, but is not required to, throw the exception if the map whose mappings are to be "superimposed" is empty.

    Some map implementations have restrictions on the keys and values they may contain. For example, some implementations prohibit null keys and values, and some have restrictions on the types of their keys. Attempting to insert an ineligible key or value throws an unchecked exception, typically NullPointerException or ClassCastException. Attempting to query the presence of an ineligible key or value may throw an exception, or it may simply return false; some implementations will exhibit the former behavior and some will exhibit the latter. More generally, attempting an operation on an ineligible key or value whose completion would not result in the insertion of an ineligible element into the map may throw an exception or it may succeed, at the option of the implementation. Such exceptions are marked as "optional" in the specification for this interface.

    This interface is a member of the Java Collections Framework.

    Many methods in Collections Framework interfaces are defined in terms of the equals method. For example, the specification for the containsKey(Object key) method says: "returns true if and only if this map contains a mapping for a key k such that (key==null ? k==null : key.equals(k))." This specification should not be construed to imply that invoking Map.containsKey with a non-null argument key will cause key.equals(k) to be invoked for any key k. Implementations are free to implement optimizations whereby the equals invocation is avoided, for example, by first comparing the hash codes of the two keys. (The Object.hashCode() specification guarantees that two objects with unequal hash codes cannot be equal.) More generally, implementations of the various Collections Framework interfaces are free to take advantage of the specified behavior of underlying Object methods wherever the implementor deems it appropriate.
    """
    _java_name = java_imports['Map']
    @javaConstructorOverload(java_imports['Map'])
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, val):
        return self.put(key, val)
    def __delitem__(self, key):
        return self.remove(key)
    def __len__(self):
        return self.size()
    def __repr__(self):
        if len(self) <= 6:
            return "{%s}" % ", ".join(map(lambda x: "%s => %s" % (x.getKey().toString(),
                                x.getValue().toString()), self.entrySet()))
        else:
            return "{%s ... %s}" % (", ".join(map(lambda x: "%s => %s" % (x.getKey().toString(),
                                x.getValue().toString()), [x for x in self.entrySet()][:3])),
                                ", ".join(map(lambda x: "%s => %s" % (x.getKey().toString(),
                                x.getValue().toString()), [x for x in self.entrySet()][-3:])))
    ## Removes all of the mappings from this map
    @javaOverload("clear",
                  (make_sig([],'void'),(),None))
    def clear(self, *args):
        """
        Removes all of the mappings from this map

        Signatures:

        void clear()
        """
        pass
    ## Returns true if this map contains a mapping for the specified key
    # @param key Key whose presence in map is to be tested
    # @return True if this map contains a mapping for the specified key
    @javaOverload("containsKey",
                  (make_sig([java_imports["Object"]],'boolean'),(Object,),None))
    def containsKey(self, *args):
        """
        Returns true if this map contains a mapping for the specified key

        Signatures:

        boolean containsKey(Object key)

        Arguments:

        key -- key whose presence in map is to be tested

        Returns:

        True if this map contains a mapping for the specified key
        """
        pass
    ## Returns true if this map contains a mapping for the specified value
    # @param value Value whose presence in map is to be tested
    # @return True if this map contains a mapping for the specified value
    @javaOverload("containsValue",
                  (make_sig([java_imports["Object"]],'boolean'),(Object,),None))
    def containsValue(self, *args):
        """
        Returns true if this map contains a mapping for the specified value

        Signatures:

        boolean containsValue(Object value)

        Arguments:

        value -- value whose presence in map is to be tested

        Returns:

        True if this map contains a mapping for the specified value
        """
        pass
    @javaGenericOverload("entrySet",
            (make_sig([],java_imports['Set']),(),
            lambda x: Set(obj=x, generic=(Map.Entry,))))
    def _entrySet(self, *args):
        pass
    ## Returns a Set view of the mapping contained in this map
    # @return Set view of the mappings contained in this map
    def entrySet(self, *args):
        """
        Returns a Set view of the mappings contained in this map

        Signatures:

        Set<Map.Entry<K,V>> entrySet()

        Returns:

        Set view of the mappings contained in this map
        """
        entryset = self._entrySet(*args)
        entryset.generic_dict['/@1/'].generic_dict = dict(self.generic_dict)
        return entryset
    ## Associates the specified value with the specified key in this map
    # @param key key with which the specified value is to be associated
    # @param value value to be associated with the specified key
    # @return Previous value associated with key, or null if there was no mapping for key
    @javaGenericOverload("put",
            (make_sig([java_imports['Object'],java_imports['Object']],java_imports['Object']),
             ('/@1/','/@2/'),'/@2/'))
    def put(self, *args):
        """
        Associates the specified value with the specified key in this map

        Signatures:

        V put(K key, V value)

        Arguments:

        key -- key with which the specified value is to be associated
        value -- value to be associated with the specified key

        Returns:

        Previous value associated with key, or null if there was no mapping for key
        """
        pass
    ## Gets the value to which the specified key is mapped, or null if this map contains no mapping
    # for this key
    # @param key The key whose associated value is to be returned
    # @return The value to which the specified key is mapped, or null if this map contains no mapping
    # for this key
    @javaGenericOverload("get",
                (make_sig([java_imports['Object']],java_imports['Object']),(Object,),
                 '/@2/'))
    def get(self, *args):
        """
        Gets the vlaue to which the specified key is mapped, or null if this map contains no
        mapping for the key

        Signatures:

        V get(Object key)

        Arguments:

        key -- the key whose associated value is to be returned

        Returns:

        The value to which the specified key is mapped, or null if htis map contains no mapping
        for the key
        """
        pass
    ## Returns true if this map contains no key-value mappings
    # @return Whether this map contains any key-value mappings
    @javaOverload("isEmpty",
                  (make_sig([],'boolean'),(),None))
    def isEmpty(self, *args):
        """
        Returns true if this map contains no key-value mappings

        Signatures:

        boolean isEmpty()

        Returns:

        Whether this map contains any key-value mappings
        """
        pass
    ## Returns a set view of the keys contained in this map
    # @return Set of the keys in the map
    @javaGenericOverload("keySet",
                  (make_sig([],java_imports['Set']),(),
                   dict(type=Set,generic=("/@1/",))))
    def keySet(self, *args):
        """
        Returns a Set view of the keys contained in this map

        Signatures:

        Set<K> keySet()

        Returns:

        Set of the keys in the map
        """
        pass
    ## Copies all of the mappings from the specified map to this map
    # @param m Mappings to be stored in this map
    @javaOverload("putAll",
                  (make_sig([java_imports['Map']],'void'),(metaMap,),None))
    def putAll(self, *args):
        """
        Copies all of the mappings from the specified map to this map

        Signatures:

        void putAll(Map<? extends K, ? extends V> m)

        Arguments:

        m -- Mappings to be stored in this map
        """
        pass
    ## Removes the mapping for a key from this map if it is present
    # @param key Key for the key-value pair you want to remove
    # @return The previous value associated with key, or null if there was no mapping for key
    @javaGenericOverload("remove",
                         (make_sig([java_imports['Object']],java_imports['Object']),(Object,),
                          '/@2/'))
    def remove(self, *args):
        """
        Removes the mapping for a key from this map if it is present

        Signatures:

        V remove(Object key)

        Arguments:

        key -- Key for the key-value pair you want to remove

        Returns:

        The previous value associated with key, or null if there was no mapping for key
        """
        pass
    ## Returns the number of key-value mappings in this map
    # @return The number of key-value mappings in this map
    @javaOverload("size",
                  (make_sig([],'int'),(),None))
    def size(self, *args):
        """
        Returns the number of key-value mappings in this map

        Signatures:

        int size()

        Returns:

        The number of key-value mappings in this map
        """
        pass
    ## Returns a Collection view of the values contained in this map
    # @return The Collection view of the values contained in this map
    @javaGenericOverload("values",
            (make_sig([],java_imports['Collection']),(),
             dict(type=Collection,generic=("/@2/",))))
    def values(self, *args):
        """
        Returns a Collection view of the values contained in this map

        Signatures:

        Collection<V> values()

        Returns:

        The Collection view of the values contained in this map
        """
        pass
    class Entry(genericJavaObj, Object):
        """
        A map entry (key-value pair). The Map.entrySet method returns a collection-view of the map,
        whose elements are of this class. The only way to obtain a reference to a map entry is from
        the iterator of this collection-view. These Map.Entry objects are valid only for the duration
        of the iteration; more formally, the behavior of a map entry is undefined if the backing map
        has been modified after the entry was returned by the iterator, except through the setValue
        operation on the map entry.
        """
        _java_name = java_imports['Map']+'$Entry'
        @javaConstructorOverload(java_imports['Map']+'$Entry')
        def __init__(self, *args, **kwargs):
            super(Map.Entry, self).__init__(*args, **kwargs)
        ## Returns the key corresponding to this entry
        # @return Key corresponding to this entry
        @javaGenericOverload("getKey",
                    (make_sig([],java_imports['Object']),(),"/@1/"))
        def getKey(self, *args):
            """
            Returns the key corresponding to this entry

            Signatures:

            K getKey()

            Returns:

            Key corresponding to this entry
            """
            pass
        ## Returns the value corresponding to this entry
        # @return Value corresponding to this entry
        @javaGenericOverload("getValue",
                    (make_sig([],java_imports['Object']),(),"/@2/"))
        def getValue(self, *args):
            """
            Returns the value corresponding to this entry

            Signatures:

            K getValue()

            Returns:

            Value corresponding to this entry            
            """
            pass
        ## Replaces the value corresponding to this entry with the specified value
        # @param value ne vlaue to be stored in this entry
        # @return Old value corresponding to the entry
        @javaGenericOverload("setValue",
                    (make_sig([java_imports['Object']],java_imports['Object']),('/@2/',),'/@2/'))
        def setValue(self, *args):
            """
            Replaces the value corresponding to this entry with the specified value

            Signatures:

            V setValue(V value)

            Arguments:

            value -- new value to be stored in this entry

            Returns:

            Old value corresponding to the entry
            """
            pass
        
