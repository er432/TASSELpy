from TASSELpy.java.util.Iterator import Iterator
from TASSELpy.java.lang.Object import Object
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaGenericOverload,javaConstructorOverload
from TASSELpy.javaObj import genericJavaObj

java_imports = {'Iterable':'java/lang/Iterable',
                'Iterator':'java/util/Iterator'}
class Iterable(genericJavaObj, Object):
    """
    Implementing this interface allows an object to be the target of the
    "foreach" statement

    Signature: Iterable<T>
    """
    _java_name = java_imports['Iterable']
    def __iter__(self):
        it = self.iterator()
        while it.hasNext():
            yield it.next()
    @javaConstructorOverload(java_imports['Iterable'])
    def __init__(self, *args, **kwargs):
        ## Allow specification of bracketed type
        super(Iterable, self).__init__(*args, **kwargs)
    ## Returns an iterator over a set of elements of type T
    # @return An iterator
    @javaGenericOverload("iterator",
        (make_sig([],java_imports['Iterator']),(),
         dict(type=Iterator,generic=('/@1/',))))
    def iterator(self, *args):
        """
        Returns an iterator over a set of elements of type T

        Signatures:

        Iterator<T> iterator()

        Returns:

        An iterator
        """
        pass
        
