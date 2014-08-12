from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaGenericOverload
from TASSELpy.java.util.Collection import Collection

java_imports = {'Object':'java/lang/Object',
                'Queue':'java/util/Queue'}
class Queue(Collection):
    """
    From docs.oracle.com:

    public interface Queue<E>
    extends Collection<E>

    A collection designed for holding elements prior to
    processing. Besides basic Collection operations, queues provide
    additional insertion, extraction, and inspection operations. Each of
    these methods exists in two forms: one throws an exception if the
    operation fails, the other returns a special value (either null or
    false, depending on the operation). The latter form of the insert
    operation is designed specifically for use with capacity-restricted
    Queue implementations; in most implementations, insert operations
    cannot fail.
    """
    _java_name = java_imports['Queue']
    @javaConstructorOverload(java_imports['Queue'])
    def __init__(self, *args, **kwargs):
        super(Queue, self).__init__(*args, **kwargs)
    @javaGenericOverload("add",
                         (make_sig([java_imports['Object']],'boolean'),('/@1/',),None))
    def add(self, *args):
        """ Inserts the specified element into this queue if it is possible
        to do so immediately without violating capacity restrictions, returning
        true upon success and throwing IllegalStateException if no space
        is currently available

        Signatures:

        boolean add(E e)

        Arguments:

        e -- the element to add

        Returns:

        true
        """
        pass
    @javaGenericOverload("element",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def element(self, *args):
        """ Retrieves, but does not remove, the head of this queue. This method
        differs from peek only in that it throws an exception if this queue is empty

        Signatures:

        E element()

        Returns:

        The head of this queue
        """
        pass
    @javaGenericOverload("offer",
                         (make_sig([java_imports['Object']],'boolean'), ('/@1/',), None))
    def offer(self, *args):
        """ Inserts the specified element into this queue if it is possible to do so
        immediately without violating capacity restrictions. When using a capacity-restricted
        queue, this method is generally preferable to add(E), which can fail to insert an element
        only by throwing an exception

        Signatures:

        boolean offer(E e)

        Arguments:

        e -- the element to add

        Returns:

        true if the element was added to this queue, else false
        """
        pass
    @javaGenericOverload("peek",
                         (make_sig([],java_imports['Object']),(),'/@1/'))
    def peek(self, *args):
        """ Retrieves, but does not remove, the head of this queue, or returns null if
        this queue is empty

        Signatures:

        E peek()

        Returns:

        the head of this queue, or null if queue is empty
        """
        pass
    @javaGenericOverload("peek",
                         (make_sig([],java_imports['Object']),(),'/@1/'))    
    def poll(self, *args):
        """ Retrieves and removes the head of this queue, or returns null
        if this queue is empty

        Signatures:

        E poll()

        Returns:

        the head of this queue, or null if the queue is empty
        """
        pass
