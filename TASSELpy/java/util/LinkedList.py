from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaGenericOverload
from TASSELpy.java.util.List import List
from TASSELpy.java.util.Deque import Deque
from TASSELpy.java.util.Collection import Collection
from TASSELpy.java.lang.Integer import metaInteger

java_imports = {'Collection':'java/util/Collection',
                'LinkedList':'java/util/LinkedList'}

class LinkedList(List, Deque):
    """ From docs.oracle.com:

public class LinkedList<E>
extends AbstractSequentialList<E>
implements List<E>, Deque<E>, Cloneable, Serializable

    Doubly-linked list implementation of the List and Deque
    interfaces. Implements all optional list operations, and permits all
    elements (including null).

    All of the operations perform as could be expected for a doubly-linked
    list. Operations that index into the list will traverse the list from
    the beginning or the end, whichever is closer to the specified index.

    Note that this implementation is not synchronized. If multiple threads
    access a linked list concurrently, and at least one of the threads
    modifies the list structurally, it must be synchronized externally. (A
    structural modification is any operation that adds or deletes one or
    more elements; merely setting the value of an element is not a
    structural modification.) This is typically accomplished by
    synchronizing on some object that naturally encapsulates the list. If
    no such object exists, the list should be "wrapped" using the
    Collections.synchronizedList method. This is best done at creation
    time, to prevent accidental unsynchronized access to the list:

       List list = Collections.synchronizedList(new LinkedList(...));

    The iterators returned by this class's iterator and listIterator
    methods are fail-fast: if the list is structurally modified at any
    time after the iterator is created, in any way except through the
    Iterator's own remove or add methods, the iterator will throw a
    ConcurrentModificationException. Thus, in the face of concurrent
    modification, the iterator fails quickly and cleanly, rather than
    risking arbitrary, non-deterministic behavior at an undetermined time
    in the future.

    Note that the fail-fast behavior of an iterator cannot be guaranteed
    as it is, generally speaking, impossible to make any hard guarantees
    in the presence of unsynchronized concurrent modification. Fail-fast
    iterators throw ConcurrentModificationException on a best-effort
    basis. Therefore, it would be wrong to write a program that depended
    on this exception for its correctness: the fail-fast behavior of
    iterators should be used only to detect bugs.
    """
    _java_name = java_imports['LinkedList']
    @javaConstructorOverload(java_imports['LinkedList'],
                             (make_sig([],'void'),()),
                             (make_sig([java_imports['Collection']],'void'),(Collection,)))
    def __init__(self, *args, **kwargs):
        """ Constructs a new LinkedList

        Signatures:

        LinkedList()
        LinkedList(Collection<? extends E> c)

        Arguments:

        LinkedList(Collection<? extends E> c)
            c -- the collection whose elements are to be placed into this list
        """
        super(LinkedList, self).__init__(*args, **kwargs)
    @javaOverload("addAll",
                  (make_sig([java_imports['Collection']],'boolean'),(Collection,),None),
                  (make_sig(['int',java_imports['Collection']],'boolean'),
                   (metaInteger, Collection), None))
    def addAll(self, *args):
        """ Inserts all the lements in the specified collection into this list. Can start
        at some specified position

        Signatures:

        boolean addAll(Collection<? extends E> c)
        boolean addAll(int index, Collection<? extends E> c)

        Arguments:

        boolean addAll(Collection<? extends E> c)
            c -- collection containing elements to be added to this list
        boolean addAll(int index, Collection<? extends E> c)
            index -- index at which to insert the first element from the specified collection
            c -- collection containing elements to be added to this list

        Returns:

        true if this list changed as a result of the call
        """
        pass
