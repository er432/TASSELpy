from TASSELpy.java.util.Iterator import Iterator
from TASSELpy.utils.Overloading import javaOverload,javaGenericOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig

java_imports = {'ListIterator':'java/util/ListIterator',
                'Object':'java/lang/Object'}

class ListIterator(Iterator):
    _java_name = java_imports['ListIterator']
    @javaConstructorOverload(java_imports['ListIterator'])
    def __init__(self, *args, **kwargs):
        super(ListIterator,self).__init__(*args, **kwargs)
    ## Inserts the specified element into the list
    # @param e the element you want to add to the list
    @javaGenericOverload("add",
            (make_sig([java_imports['Object']],'void'),('/@1/',),None))
    def add(self, *args):
        """
        Inserts the specified element into the list

        Signatures:

        void add(E e)

        Arguments:

        e -- the element you want to add to the list
        """
        pass
    ## Returns true if this list iterator has more elements when traversing the list
    # in the reverse direction
    # @return true if the list iterator has more elements in the reverse direction
    @javaOverload("hasPrevious",
                  (make_sig([],'boolean'),(),None))
    def hasPrevious(self, *args):
        """
        Returns true if this list iterator has more elements when traversing the list
        in the reverse direction

        Signatures:

        boolean hasPrevious()

        Returns:

        true if the list iterator has more elements in the reverse direction
        """
        pass
    ## Returns the index of the element that would be returned by a subsequent call to
    # next()
    # @return the element that would be returned by a subsequent call to next()
    @javaOverload("nextIndex",
                  (make_sig([],'int'),(),None))
    def nextIndex(self, *args):
        """
        Returns the index of the element that would be returned by a subsequent call to
        next()

        Signatures:

        int nextIndex()

        Returns:

        the index of the element that would be returned by a subsequent call to next()
        """
        pass
    ## Returns the previous element in the list and moves the cursor position backwards
    # @return the previous element in the list
    @javaGenericOverload("previous",
                  (make_sig([],java_imports['Object']),('/@1/',),None))
    def previous(self, *args):
        """
        Returns the previous element in the list and moves the cursor position backwards

        Signatures:

        E previous()

        Returns:

        The previous element in the list
        """
        pass
    ## Returns the index of the element that would be returned by a subsequent call
    # to previous()
    # @return the index of the element that would be returned by a subsequent call to
    # previous()
    @javaOverload("previousIndex",
                  (make_sig([],'int'),(),None))
    def previousIndex(self, *args):
        """
        Returns the index of the element that would be returned by a subsequent call
        to previous()

        Signatures:

        int previousIndex()

        Returns:

        The index of the element that would be returned by a subsequent call to previous()
        """
        pass
    ## Replaces the last element returned by next() or previous() with the specified element
    # @param e the element with which to replace the last element returned by next or previous
    @javaGenericOverload("set",
                         (make_sig([java_imports['Object']],'void'),('/@1/',),None))
    def set(self, *args):
        """
        Replaces the last element returned by next() or previous() with the specified
        element

        Signatures:

        void set(E e)

        Arguments:

        e -- the element with which to replace the last element returned by next or previous
        """
        pass
