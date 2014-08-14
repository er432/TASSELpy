from TASSELpy.java.util.Collection import Collection
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.util.ListIterator import ListIterator
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload,javaGenericOverload
from TASSELpy.java.lang.Object import Object

java_imports = {'List':'java/util/List',
                'ListIterator':'java/util/ListIterator',
                'Object':'java/lang/Object'}
class metaList(Collection):
    def __init__(self, *args, **kwargs):
        super(metaList, self).__init__(*args, **kwargs)

class List(metaList):
    """
    From docs.oracle.com:

    public interface List<E>
    extends Collection<E>

    An ordered collection (also known as a sequence). The user of this
    interface has precise control over where in the list each element
    is inserted. The user can access elements by their integer index
    (position in the list), and search for elements in the list.
    Unlike sets, lists typically allow duplicate elements. More
    formally, lists typically allow pairs of elements e1 and e2 such
    that e1.equals(e2), and they typically allow multiple null
    elements if they allow null elements at all. It is not
    inconceivable that someone might wish to implement a list that
    prohibits duplicates, by throwing runtime exceptions when the user
    attempts to insert them, but we expect this usage to be rare.

    The List interface places additional stipulations, beyond those
    specified in the Collection interface, on the contracts of the
    iterator, add, remove, equals, and hashCode methods. Declarations
    for other inherited methods are also included here for
    convenience.

    The List interface provides four methods for positional (indexed)
    access to list elements. Lists (like Java arrays) are zero
    based. Note that these operations may execute in time proportional
    to the index value for some implementations (the LinkedList class,
    for example). Thus, iterating over the elements in a list is
    typically preferable to indexing through it if the caller does not
    know the implementation.

    The List interface provides a special iterator, called a
    ListIterator, that allows element insertion and replacement, and
    bidirectional access in addition to the normal operations that the
    Iterator interface provides. A method is provided to obtain a list
    iterator that starts at a specified position in the list.

    The List interface provides two methods to search for a specified
    object. From a performance standpoint, these methods should be
    used with caution. In many implementations they will perform
    costly linear searches.

    The List interface provides two methods to efficiently insert and
    remove multiple elements at an arbitrary point in the list.

    Note: While it is permissible for lists to contain themselves as
    elements, extreme caution is advised: the equals and hashCode
    methods are no longer well defined on such a list.

    Some list implementations have restrictions on the elements that
    they may contain. For example, some implementations prohibit null
    elements, and some have restrictions on the types of their
    elements. Attempting to add an ineligible element throws an
    unchecked exception, typically NullPointerException or
    ClassCastException. Attempting to query the presence of an
    ineligible element may throw an exception, or it may simply return
    false; some implementations will exhibit the former behavior and
    some will exhibit the latter. More generally, attempting an
    operation on an ineligible element whose completion would not
    result in the insertion of an ineligible element into the list may
    throw an exception or it may succeed, at the option of the
    implementation. Such exceptions are marked as "optional" in the
    specification for this interface.

    This interface is a member of the Java Collections Framework.
    """
    _java_name = java_imports['List']
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, value):
        previous = self.set(key, value)
    @javaConstructorOverload(java_imports['List'])
    def __init__(self, *args, **kwargs):
        super(List, self).__init__(*args, **kwargs)
    ## Returns a list iterator over the elements in this list
    # @param index optional index of the first element to be returned from the list
    # iterator (by a call to next)
    # @return a list iterator over the elements in this list (in proper sequence),
    # starting at the specified position in the list
    @javaGenericOverload("listIterator",
            (make_sig([],java_imports['ListIterator']),(),
             dict(type=ListIterator, generic=('/@1/',))),
            (make_sig(['int'],java_imports['ListIterator']),(metaInteger,),
             dict(type=ListIterator, generic=('/@1/',))))
    def listIterator(self, *args):
        """
        Returns a list iterator over the elements in this list

        Signatures:

        ListIterator<E> listIterator()
        ListIterator<E> listIterator(int index)

        Arguments:

        ListIterator<E> listIterator(int index)
           index -- index of the first element to be returned from the list iterator
                    (by a call to next)

        Returns:

        a list iterator over the elements in this list (in proper sequence),
        starting at the specified position in the list
        """
        pass
    ## Returns the element at the specified position in this list
    # @param index the index of the item you want
    # @return The element at the specified position in the list
    @javaGenericOverload("get",
            (make_sig(['int'],java_imports['Object']), (metaInteger,), '/@1/'))
    def get(self, *args):
        """
        Returns the element at the specified position in this list

        Signatures:

        E get(int index)

        Arguments:

        index -- The index of the item you want

        Returns:

        The element at the specified position in the list
        """
        pass
    ## Replaces the element at the specified position in this list with the
    # specified element
    # @param index index of the element to replace
    # @param element element to be stored at the specified position
    # @return the element previously at the specified position
    @javaGenericOverload("set",
            (make_sig(['int',java_imports['Object']],java_imports['Object']),
             (metaInteger,'/@1/'),'/@1/'))
    def set(self, *args):
        """
        Replaces the element at the specified position in this list with
        the specified element

        Signatures:

        E set(int index, E element)

        Arguments:

        index -- index of the element to replace
        element -- element to be stored at the specified position

        Returns:

        the element previously at the specified position
        """
        pass
    @javaGenericOverload("subList",
            (make_sig(['int','int'],java_imports['List']),(metaInteger, metaInteger),
             dict(type=metaList, generic=('/@1/',))))
    def subList(self, *args):
        """
        REturns a view of the portion of this list between the specified fromIndex,
        inclusive, and toIndex, exclusive. If they are equal, the returned list is empty).
        The returned list is backed by this list, so non-structural changes in the returned list
        are reflected in this list, and vice-versa. The returned list supports all of the
        optional list operations supported by this list.

        This method eliminates the need for explicit range operations. Any operation that
        expects a list can be used as a range operations by passing a subList view instead
        of a whole list. For example, the following idiom removes a range of elements from a list:

        list.subList(from, to).clear();

        Similar idioms may be constructed for indexOf and lastIndexOf, and all of the algorithms
        in the Collections class can be applied to a subList.

        Signatures:

        List<E> subList(int fromIndex, int toIndex)

        Arguments:

        fromIndex -- low endpoint (inclusive) of the subList
        toIndex -- high endpoint (exclusive) of the subList

        Returns:

        a view of the specified range within this list
        """
        pass
    @javaOverload("indexOf",
                  (make_sig([java_imports['Object']],'int'),(Object,),None))
    def indexOf(self, *args):
        """ Returns the index of the first occurrence of the specified element in this
        list, or -1 if this list does not contain the element. More formally, returns the
        lowest index i such that (o==null ? get(i)==null : o.equals(get(i))), or -1 if there is no
        such index

        Signatures:

        int indexOf(Object o)

        Arguments:

        o -- element to search for

        Returns:

        the index of the first occurrence of the specified element in this list, or -1 if
        this list does not contain the element
        """
        pass
    @javaOverload("lastIndexOf",
                  (make_sig([java_imports['Object']],'int'),(Object,),None))
    def lastIndexOf(self, *args):
        """ Returns the index of the last occurrence of the specified element in this list,
        or -1 if this list does not contain the element. More formally, returns the highest index
        i such that (o==null ? get(i)==null : o.equals(get(i))), or -1 if there is no such index

        Signatures:

        int lastIndexOf(Object o)

        Arguments:

        o -- element to search for

        Returns:

        the index of the last occurrence of the specified element in this list, or -1
        if this list does not contain the element
        """
        pass
