from TASSELpy.javaObj import javaObj
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig

java_imports = {'Object':'java/lang/Object',
                'String':'java/lang/String'}
class Object(javaObj):
    """
    Acts like Java.lang.Object
    """
    _java_name = java_imports['Object']
    ## Instantiates a Java Object
    @javaConstructorOverload(java_imports['Object'],
                             (make_sig([],'void'),()))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Java object

        Signatures:

        Object()
        """
        pass
    ## Creates and returns a copy of this object
    # @return A copy of this object
    @javaOverload("clone",
            (make_sig([],java_imports['Object']),(),lambda x: Object(obj=x)))
    def clone(self, *args):
        """
        Creates and returns a copy of this object

        Signatures:

        protected Object clone()

        Returns:

        A copy of this object
        """
        pass
    ## Returns a string representation of the object
    # @return The string representation of the object
    @javaOverload("toString",
                  (make_sig([],java_imports['String']),(),None))
    def toString(self, *args):
        """
        Returns a string representation of the object

        Signatures:

        String toString()

        Returns:

        The string representaiton of the object
        """
        pass
    ## Indicates whether some other object is "equal to" this one
    # @param obj The object you want to test for equality
    # @return true if equal
    @javaOverload("equals",
                  (make_sig([java_imports['Object']],'boolean'),(javaObj,),None))
    def equals(self, *args):
        """
        Indicates whether some other object is "equal to" this one

        Signatures:

        boolean equals(Object obj)

        Arguments:

        obj -- The object you want to test for equality

        Returns:

        true if equal
        """
        pass
    ## Returns a hash code value for this object
    # @return Hash code value for this object
    @javaOverload("hashCode",
            (make_sig([],'int'),(),None))
    def hashCode(self, *args):
        """
        Returns a hash code vlaue for the object

        Signatures:

        int hashCode()

        Returns:

        Hash code value for this object
        """
        pass
    #################
    # Python magic methods
    #################
    def __eq__(self, other):
        if isinstance(other, javaObj):
            return self.equals(other)
        else:
            return False
    def __hash__(self):
        return self.hashCode()
    def __str__(self):
        return self.toString()
