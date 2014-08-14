from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload,javaGenericOverload
from TASSELpy.java.util.List import List

java_imports = {'AbstractSequentialList':'java/util/AbstractSequentialList'}

class AbstractSequentialList(List):
    """ From docs.oracle.com:

    public abstract class AbstractSequentialList<E>
    extends AbstractList<E>

    This class provides a skeletal implementation of the List interface to
    minimize the effort required to implement this interface backed by a
    "sequential access" data store (such as a linked list). For random
    access data (such as an array), AbstractList should be used in
    preference to this class.

    This class is the opposite of the AbstractList class in the sense that
    it implements the "random access" methods (get(int index), set(int
    index, E element), add(int index, E element) and remove(int index)) on
    top of the list's list iterator, instead of the other way around.

    To implement a list the programmer needs only to extend this class and
    provide implementations for the listIterator and size methods. For an
    unmodifiable list, the programmer need only implement the list
    iterator's hasNext, next, hasPrevious, previous and index methods.

    For a modifiable list the programmer should additionally implement the
    list iterator's set method. For a variable-size list the programmer
    should additionally implement the list iterator's remove and add
    methods.

    The programmer should generally provide a void (no argument) and
    collection constructor, as per the recommendation in the Collection
    interface specification.
    """
    _java_name = java_imports['AbstractSequentialList']
    @javaConstructorOverload(java_imports['AbstractSequentialList'])
    def __init__(self, *args, **kwargs):
        pass
