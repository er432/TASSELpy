from TASSELpy.utils.Overloading import javaOverload,javaGenericOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import genericJavaObj
from TASSELpy.java.lang.Object import Object

java_imports = {'Iterator':'java/util/Iterator',
                'Object':'java/lang/Object'}
class Iterator(genericJavaObj, Object):
    """
    From docs.oracle.com:
    
    An iterator over a collection. Iterator takes the place of Enumeration
    in the Java Collections Framework. Iterators differ from enumerations in 2
    wyas:

    Iterators allow the caller to remove elements from the underlying collection during
    the iteration with well-defined semantics.

    Method names have been improved
    """
    _java_name = java_imports['Iterator']
    @javaConstructorOverload(java_imports['Iterator'])
    def __init__(self, *args, **kwargs):
        super(Iterator, self).__init__(**kwargs)
    ## Define iterator function for the iterator
    def __iter__(self):
        while self.hasNext():
            yield self.next()
    ## Returns true if the iteration has more elements. (In other words,
    # returns true if next() would return an elemen rather than throwing
    # an exception
    # @return true if the iteration has more elements
    @javaOverload("hasNext",
                  (make_sig([],'boolean'),(),None))
    def hasNext(self, *args):
        """
        Returns true if the iteration has more elements. (In other
        words, returns true if next() would return an element
        rather than throwing an exception.

        Signatures:

        boolean hasNext()

        Returns:

        true if the iteration has more elements
        """
        pass
    ## Returns the next element in the iteration
    # @return the next element in the iteration
    @javaGenericOverload("next",
                  (make_sig([],java_imports['Object']),(),"/@1/"))
    def next(self, *args):
        """
        Returns the next element in the iteration

        Signatures:

        E next()

        Returns:

        the next element in the iteration

        Throws:

        NoSuchElementException if iteration has no more elements
        """
        pass
    ## Removes from the underyling collection the last element returned by this iterator.
    # The method can be called only once per call to next(). The behavior of an iterator is
    # unspecified if the underlying collection is modified while the iteration is in progress
    # in any way other than by calling this method
    @javaOverload("remove",
                  (make_sig([],'void'),(),None))
    def remove(self, *args):
        """
        Removes from the underlying collection the last element returned by this iterator.
        The method can be called only once per call to next(). The behavior of an iterator is
        unspecified if the underlying collection is modified while the itartion is in progress
        in any way othe rthan by calling this method.

        Signatures:

        void remove()

        Throws:

        UnsupportedOperationException -- if remove operation is not supported by this iterator
        IllegalStateException -- if the next method has not yet been called, or the remove method
                                 has already been called after the last call to the next method
        """
        pass
