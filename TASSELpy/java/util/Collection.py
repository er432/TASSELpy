from TASSELpy.java.lang.Iterable import Iterable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaGenericOverload,javaConstructorOverload
from TASSELpy.javaObj import javaObj
import javabridge

java_imports = {'Collection':'java/util/Collection',
                'Object':'java/lang/Object'}

class metaCollection(Iterable):
    @javaConstructorOverload(java_imports['Collection'])
    def __init__(self, *args, **kwargs):
        super(metaCollection,self).__init__(*args, **kwargs)
    pass

## Wrapper for the root interface in the collection hierarchy
class Collection(metaCollection):
    """
    From docs.oracle.com:

    public interface Collection<E>
    extends Iterable<E>
    
    The root interface in the collection hierarchy. A collection represents a group of objects, known as its elements. Some collections allow duplicate elements and others do not. Some are ordered and others unordered. The JDK does not provide any direct implementations of this interface: it provides implementations of more specific subinterfaces like Set and List. This interface is typically used to pass collections around and manipulate them where maximum generality is desired.
    Bags or multisets (unordered collections that may contain duplicate elements) should implement this interface directly.

    All general-purpose Collection implementation classes (which typically implement Collection indirectly through one of its subinterfaces) should provide two "standard" constructors: a void (no arguments) constructor, which creates an empty collection, and a constructor with a single argument of type Collection, which creates a new collection with the same elements as its argument. In effect, the latter constructor allows the user to copy any collection, producing an equivalent collection of the desired implementation type. There is no way to enforce this convention (as interfaces cannot contain constructors) but all of the general-purpose Collection implementations in the Java platform libraries comply.

    The "destructive" methods contained in this interface, that is, the methods that modify the collection on which they operate, are specified to throw UnsupportedOperationException if this collection does not support the operation. If this is the case, these methods may, but are not required to, throw an UnsupportedOperationException if the invocation would have no effect on the collection. For example, invoking the addAll(Collection) method on an unmodifiable collection may, but is not required to, throw the exception if the collection to be added is empty.

    Some collection implementations have restrictions on the elements that they may contain. For example, some implementations prohibit null elements, and some have restrictions on the types of their elements. Attempting to add an ineligible element throws an unchecked exception, typically NullPointerException or ClassCastException. Attempting to query the presence of an ineligible element may throw an exception, or it may simply return false; some implementations will exhibit the former behavior and some will exhibit the latter. More generally, attempting an operation on an ineligible element whose completion would not result in the insertion of an ineligible element into the collection may throw an exception or it may succeed, at the option of the implementation. Such exceptions are marked as "optional" in the specification for this interface.

    It is up to each collection to determine its own synchronization policy. In the absence of a stronger guarantee by the implementation, undefined behavior may result from the invocation of any method on a collection that is being mutated by another thread; this includes direct invocations, passing the collection to a method that might perform invocations, and using an existing iterator to examine the collection.

    Many methods in Collections Framework interfaces are defined in terms of the equals method. For example, the specification for the contains(Object o) method says: "returns true if and only if this collection contains at least one element e such that (o==null ? e==null : o.equals(e))." This specification should not be construed to imply that invoking Collection.contains with a non-null argument o will cause o.equals(e) to be invoked for any element e. Implementations are free to implement optimizations whereby the equals invocation is avoided, for example, by first comparing the hash codes of the two elements. (The Object.hashCode() specification guarantees that two objects with unequal hash codes cannot be equal.) More generally, implementations of the various Collections Framework interfaces are free to take advantage of the specified behavior of underlying Object methods wherever the implementor deems it appropriate.

    This interface is a member of the Java Collections Framework.
    """
    _java_name = java_imports['Collection']
    @javaConstructorOverload(java_imports['Collection'])
    def __init__(self, *args, **kwargs):
        super(Collection, self).__init__(*args, **kwargs)
    def __contains__(self, item):
        return self.contains(item)
    ## Ensures that this collection contains the specified element.
    # @return true if this collection changed as a result of the call. False if this collection
    # does not permit duplicates and already contains the specified element.
    @javaGenericOverload("add",
                  (make_sig([java_imports['Object']],'boolean'),('/@1/',),None))
    def add(self, *args):
        """
        Ensures that this collection contains the specified element. Returns true if this collection
        changed as a result of the call. Returns false if this collection does not permit duplicates
        and already contains the specified element.

        Collections that support this operation may place limitations on what elements may be added to
        this collection. In particular, some collections will refuse to add null elements, and others
        will impose restrictions on the type of elements that may be added. Collection classes should
        clearly specify in their documentation any restrictions on what elements may be added.

        Signatures:

        boolean add(E e)

        Arguments:

        e -- element whose presence in this collection is to be ensured

        throws:

        UnsupportedOperationException -- if the add operation is not supported by this collection
        ClassCastException -- if the class of the specified element presents it from being added to this collection
        NullPointerException -- if the specified element is null and this collection does not permit null elements
        IllegalArgumentException -- if some property of the element prevents it from being added to this collection
        IllegalStateException -- if the element cannot be added at this time due to insertion restrictions
        """
        pass
    ## Adds all of the elements to the specified collection to this collection.
    # @param c The collection you want to add
    # @return true if collection changed as a result of the call
    @javaOverload("addAll",
                  (make_sig([java_imports['Collection']],'boolean'),(metaCollection,),None))
    def addAll(self,*args, **kwargs):
        """
        Adds all of the elements in the specified collection to this collection.

        Signatures:

        boolean addAll(Collection<? extends E> c

        Arguments:

        c -- The collection you want to add

        Returns:

        true if collection changed as a result of the call
        """
        pass
    ## Removes all of the elements from this collection. The collection will be empty after
    # this method Returns
    @javaOverload("clear",
                  (make_sig([],'void'),(),None))
    def clear(self, *args):
        """
        Removes all of the elements from this collection. The collection will be
        empty after this method returns

        Signatures:

        void clear()

        Throws:

        UnsupportedOperationException -- if clear operation not supported by this collection
        """
        pass
    ## Returns true if this collection contains the specified element. More formally, returns true
    # if and only if this collection contains at least one element e such that
    # (o == null ? e == null : o.equals(e))
    @javaOverload("contains",
                  (make_sig([java_imports['Object']],'boolean'),(javaObj,),None))
    def contains(self, *args):
        """
        Returns true if this collection contains the specified element. More formally, returns true
        if and only if this collection contains at least one element e such that
        (o == null ? e == null: o.equals(e))

        Signatures:

        boolean contains(Object o)

        Arguments:

        o -- element whose presence in this collection is to be tested

        Returns:

        true if this collection contains the specified element
        """
        pass
    @javaOverload("containsAll",
                  (make_sig([java_imports['Collection']],'boolean'),(metaCollection,),None))
    ## Returns true if this collection contains all of the elements in the specified collection
    # @param c collection to be checked for containment in this collection
    # @return true if this collection contains all of the elemnts in the specified collection
    def containsAll(self, *args):
        """
        Returns true if this collection contains all of the elements in the specified collection

        Signatures:

        boolean constainsAll(Collection<?> c)

        Arguments:

        c -- collection to be checked for containment in this collection

        Returns:

        true if this collection contains all of the elements in the specified collection

        Throws:

        ClassCastException -- if the types of one or more elements in the specified collection are
                              incompatible with this collection
        NullPointerException -- If the specified collection contains one or more null elements and
                                this colelction does not permit null elements
        """
        pass
    ## Returns true if this collection contains no elements
    # @return true if this collection contains no elements
    @javaOverload("isEmpty",
                  (make_sig([],'boolean'),(),None))
    def isEmpty(self, *args):
        """
        Returns true if this collection contains no elements

        Signatures:

        boolean isEmpty()

        Returns:

        true if this collection contains no elements
        """
    ## Removes a single instance of the specified element from this collection
    # @param o the element to be removed from this collection
    # @return true if an element was removed as a result of this call
    @javaOverload("remove",
                  (make_sig([java_imports['Object']],'boolean'),(javaObj,),None))
    def remove(self, *args):
        """
        Removes a single instance of the specified element from this collection, if it is present.
        More formally, removes an element e such that (o==null ? e==null : o.equals(e)), if this
        collection contains one or more such elements. Returns true if this collection contained the
        specified element (or equivalently, if this collection changed as a result of the call).

        Arguments:

        boolean remove(Object o)

        Arguments:

        o -- element to be removed from this collection

        Returns:

        true if an element was removed as a result of this call

        Throws:

        ClassCastException -- if the type of the specified element is incompatible with this collection
        NullPointerException -- if the specified element is nujll and this collection does not permit null elements
        UnsupportedOperationException -- if the remove operation is not supported by this collection
        """
        pass
    ## Removes all of this collection's elements that are also contained in the specified collection.
    # After this call returns, this collection will contain no elements in common with the specified
    # collection
    # @param c collection containing elements to be removed from this collection
    # @return true if this collection changed as a result of the call
    @javaOverload("removeAll",
                  (make_sig([java_imports['Collection']],'boolean'),(metaCollection,),None))
    def removeAll(self, *args):
        """
        Removes all of this collection's elements that are also contained in the specified
        collection. After this call returns, this collection will contain no elements in common
        with the specified collection

        Signatures:

        boolean removeAll(Collection<?> c)

        Arguments:

        c -- collection containing elements to be removed from this collection

        Returns:

        true if this collection changed as a result of the call

        Throws:

        UnsupportedOperationException -- if the removeAll method is not supported by this collection
        ClassCastException -- if the types of one or more elements in this collection are incompatible
                             with the specified collection
        NullPointerException -- if this collection contains one or more null elements and the specified
                               collection does not support null elements
        """
        pass
    ## Retains only the elements in this collection that are contained in the specified collection.
    # In other words, removes from thsi collection all of its elements that are not contained
    # in the specified collection
    # @param c collection containing elements to be retained in this collection
    # @return true if this collection changed as a result of the call
    @javaOverload("retainAll",
                  (make_sig([java_imports['Collection']],'boolean'),(metaCollection,),None))
    def retainAll(self, *args):
        """
        Retains only the elements in this collection that are contained in the specified collection.
        In other words, removes from this collection all of its elements that are not contained
        in the specified collection

        Signatures:

        boolean retainAll(Collection<?> c)

        Arguments:

        c -- collection containing elements to be retained in this collection

        Returns:

        true if this collection changed as a result of the call

        Throws:

        UnsupportedOperationException -- if the retainAll operation is not supported by this collection
        ClassCastException -- if the types of one or more of the elemtns in the collection are icompatible
                             with the specified collection
        NullPointerException -- if this collection contains one or more null elements and the specified
                                collection does not permit null elements, or if the specified collection
                                is null
        """
        pass
    ## Returns the number of elements in this collection. If the collection contains more than
    # Integer.MAX_VALUE elements, returns Integer.MAX_VALUE
    # @return the number of elements in this collection
    @javaOverload("size",
                  (make_sig([],'int'),(),None))
    def size(self, *args):
        """
        Returns the number of elements in this collection. If the collection contains more than
        Integer.MAX_VALUE elements, returns Integer.MAX_VALUE

        Signatures:

        int size()

        Returns:

        the number of elements in this collection
        """
        pass
    ## Returns an array containing all of the elements in this collection
    # @param a An optional array into which the elements of this collection are to be stored, if
    # it is big enough; otherwise, a new array of the same runtime type is allocated for this purpose
    # @return an array containing all of the elements in this collection
    @javaOverload("toArray",
                  (make_sig([],java_imports['Object']+'[]'),(),
                   lambda x: javabridge.get_env().get_object_array_elements(x)),
                  (make_sig([java_imports['Object']+'[]'],java_imports['Object']+'[]'),(javaObj,),
                   lambda x: javabridge.get_env().get_object_array_elements(x)))
    def toArray(self, *args):
        """
        Returns an array containing all of the elements in this collection. If this collection
        makes any guarantees as to what order its elements are returned by its iterator, this method
        must return the elements in the same order. The returned array will be "safe" in that no
        references to it are maintained in this collection. (In other words, this method must allocate
        a new array even if this collection is backed by an array). The caller is thus free to modify the
        returned array.

        Signatures:

        Object[] toArray()
        <T> T[] toArray(T[] a)

        Arguments:

        <T> T[] toArray(T[] a)
           a -- the array into which the elements of this collection are to be stored, if it
                is big enough; otherwise, a new array of the same runtime type is allocated for
                this purpose

        Returns:

        An array containing all of the elements in this collection

        Throws:

        ArrayStoreException -- if the runtime type of the specified array is not a supertype of the
                               runtime type of every element in this collection
        NullPointerException -- if the specified array is null
        """
        pass
