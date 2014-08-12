from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaGenericOverload
from TASSELpy.java.util.Queue import Queue
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.util.Iterator import Iterator

java_imports = {'Deque':'java/lang/Deque',
                'Iterator':'java/util/Iterator',
                'Object':'java/lang/Object'}

class Deque(Queue):
    """
    From docs.oracle.com:

    public interface Deque<E>
    extends Queue<E>

    A linear collection that supports element insertion and removal at
    both ends. The name deque is short for "double ended queue" and is
    usually pronounced "deck". Most Deque implementations place no fixed
    limits on the number of elements they may contain, but this interface
    supports capacity-restricted deques as well as those with no fixed
    size limit.

    This interface defines methods to access the elements at both ends of
    the deque. Methods are provided to insert, remove, and examine the
    element. Each of these methods exists in two forms: one throws an
    exception if the operation fails, the other returns a special value
    (either null or false, depending on the operation). The latter form of
    the insert operation is designed specifically for use with
    capacity-restricted Deque implementations; in most implementations,
    insert operations cannot fail.
    """
    _java_name = java_imports['Deque']
    @javaConstructorOverload(java_imports['Deque'])
    def __init__(self, *args, **kwargs):
        super(Deque, self).__init__(*args, **kwargs)
    @javaGenericOverload("addFirst",
                         (make_sig([java_imports['Object']],'void'),('/@1/',),None))
    def addFirst(self, *args):
        """ Inserts the specified element at the front of this deque if it is
        possible to do so immediately without violating capacity restrictions. When using
        a capacity restricted deque, it is generally preferable to use method offerFirst(E).

        Signatures:

        void addFirst(E e)

        Arguments:

        e -- the element to add
        """
        pass
    @javaGenericOverload("addLast",
                         (make_sig([java_imports['Object']],'void'),('/@1/',),None))    
    def addLast(self, *args):
        """ Inserts the specified element at the end of this deque if it is possible to do
        so immediately without violating capacity restrictions. When using a capacity restricted
        deque, it is generally preferable to use method offerLast(E).

        This method is equivalent to add(E)

        Signatures:

        void addLast(E e)

        Arguments:

        e -- the element to add
        """
        pass
    @javaGenericOverload("descendingIterator",
                         (make_sig([],java_imports['Iterator']),(),
                          dict(type=Iterator, generic=('/@1/',))))
    def descendingIterator(self, *args):
        """ Returns an iterator over the elements in this deque in reverse sequential order.
        The elements will be returned in order from last (tail) to first (head)

        Signatures:

        Iterator<E> descendingIterator()

        Returns:

        An iterator over the elements in this deque in reverse sequence
        """
        pass
    @javaGenericOverload("getFirst",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def getFirst(self, *args):
        """ Retrieves, but does not remove, the first element of this deque. This method
        differs from peekFirst only in that it throws an exception if this deque is empty

        Signatures:

        E getFirst()

        Returns:

        the head of this deque
        """
        pass
    @javaGenericOverload("getLast",
                         (make_sig([],java_imports['Object']),(),'/@1/'))    
    def getLast(self, *args):
        """ Retrieves, but does not remove, the last element of this deque. This method
        differs from peekLast only in that it throws an exception of this deque is empty.

        Signatures:

        E getLast()

        Returns:

        The tail of this deque
        """
        pass
    @javaGenericOverload("offerFirst",
                         (make_sig([java_imports['Object']],'boolean'),('/@1/',),None))
    def offerFirst(self, *args):
        """ Inserts the specified element at the front of this deque unless it would
        violate capacity restrictions. When using a capacity restricted deque, this method
        is generally preferable to the addFirst(E) method, which can fail to insert an element
        only by throwing an exception.

        Signatures:

        boolean offerFirst(E e)

        Arguments:

        e -- the element to add

        Returns:

        true if the element was added to this deque, else false
        """
        pass
    @javaGenericOverload("offerLast",
                         (make_sig([java_imports['Object']],'boolean'),('/@1/',),None))    
    def offerLast(self, *args):
        """ Inserts the specified element at the end of this deque unless it would violate
        capacity restrictions.  When using a capacity-restricted deque, this method is generally
        preferable to the addLast(E) method, which can fail to insert an element only by
        throwing an exception.

        Signatures:

        boolean offerLast(E e)

        Arguments:

        e -- the element to add

        Returns:

        true if the element was added to this deque, else false
        """
        pass
    @javaGenericOverload("peekFirst",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def peekFirst(self, *args):
        """ Retrieves, but does not remove, the first element of this deque,
        or returns null if this deque is empty

        Signatures:

        E peekFirst()

        Returns:

        the head of this deque, or null if this deque is empty
        """
        pass
    @javaGenericOverload("peekLast",
                         (make_sig([],java_imports['Object']),(),'/@1/'))    
    def peekLast(self, *args):
        """ Retrieves, but does not remove, the last element of this deque,
        or returns null if this deque is empty

        Signatures:

        E peekLast()

        Returns:

        the tail of this deque, or null if this deque is empty
        """
        pass
    @javaGenericOverload("pollFirst",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def pollFirst(self, *args):
        """ Retrieves and removes the first element of this deque, or returns
        null if this deque is empty

        Signatures:

        E pollFirst()

        Returns:

        the head of this deque, or null if this deque is empty
        """
        pass
    @javaGenericOverload("pollLast",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def pollLast(self, *args):
        """ Retrieves and removes the last element of this deque, or returns
        null if this deque is empty

        Signatures:

        E pollLast()

        Returns:

        the tail of this deque, or null if this deque is empty
        """
        pass
    @javaGenericOverload("pop",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def pop(self, *args):
        """ Pops an element from the stack represented by this deque. In other
        words, removes and returns the first element of this deque.

        This method is equivalent to removeFirst()

        Signatures:

        E pop()

        Returns:

        the element at the front of this deque (which is the top of the stack represented
        by this deque)
        """
        pass
    @javaGenericOverload("push",
                         (make_sig([java_imports['Object']],'void'),('/@1/',),None))
    def push(self, *args):
        """ Pushes an element onto the stack represented by this deque (in other
        words, at the head of the deque) if it is possible to do so immediately without
        violating capacity restrictions, returning true upon success and throwing an
        IllegalStateException if no space is currently available

        This method is equivalent to addFirst(E)

        Signatures:

        void push(E e)

        Arguments:

        e -- the element to push
        """
        pass
    @javaGenericOverload("remove",
                         (make_sig([],java_imports['Object']),(),'/@1/'),
                         (make_sig([java_imports['Object']],'boolean'), (Object,),
                          None))
    def remove(self, *args):
        """ Retrieves and removes the head of the queue represented by this
        deque (in other words, the first element of this deque). This method differs
        from poll only in that it throws an exception if this deque is empty

        The second removes the first occurrence of the specified element from this deque.
        
        Signatures:

        E remove()
        boolean remove(Object o)

        Arguments:

        boolean remove(Object o)
            o -- element to be removed from this deque, if present
        
        Returns:

        the head of the queue represented by this deque
        """
        pass
    @javaGenericOverload("removeFirst",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def removeFirst(self, *args):
        """ Retrieves and removes the first element of this deque. This method differs
        from pollFirst only in that it throws an exception if this deque is empty

        Signatures:

        E removeFirst()

        Returns:

        The head of this deque
        """
        pass
    @javaGenericOverload("removeLast",
                         (make_sig([],java_imports['Object']),(),'/@1/'))    
    def removeLast(self, *args):
        """ Retrieves and removes the last element of this deque. This method differs
        from pollLast only in that it throws an exception if this deque is empty

        Signatures:

        E removeLast()

        Returns:

        The tail of this deque
        """
        pass
    @javaGenericOverload("removeFirstOccurrence",
                         (make_sig([java_imports['Object']],'boolean'),
                          (Object,),None))
    def removeFirstOccurrence(self, *args):
        """ Removes the first occurrence of the specified element from this deque.
        If the deque does not contain the element, it is unchanged. More formally, removes
        the first element e such that (o==null ? e==null : o.equals(e)) (if such an element
        exists). Returns true if this deque contained the specified element (or equivalently,
        if this deque changed as a result of the call)

        Signatures:

        boolean removeFirstOccurrence(Object o)

        Arguments:

        o -- element to be removed from this deque, if present

        Returns:

        true if an element was removed as a result of this call
        """
        pass
    @javaGenericOverload("removeLastOccurrence",
                         (make_sig([java_imports['Object']],'boolean'),
                          (Object,),None))    
    def removeLastOccurrence(self, *args):
        """ Removes the last occurrence of the specified element from this deque. If the
        deque does not contain the element, it is unchanged. More formally, removes the last element
        e such that (o==null ? e==null : o.equals(e)) (if such an element exists). Returns
        true if this deque contained the specified element (or equivalently, if this deque changed
        as a result of the call).

        Signatures:

        boolean removeLastOccurrence(Object o)

        Arguments:

        o -- element to be removed from this deque, if present

        Returns:

        true if an element was removed as a result of this call
        """
        pass
