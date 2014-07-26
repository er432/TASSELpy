import javabridge
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Float import metaFloat
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.utils.helper import make_sig

java_imports = {'LDResult':'net/maizegenetics/analysis/popgen/LDResult'}

## LDResult Class
class LDResult(Object):
    _java_name = java_imports['LDResult']
    """
    Container class for reporting LD results.  This class could still
    be expanded to include the two sites with various sort approaches.
    The reason for this functionality is so that classes can calculate
    LD for billions of site pairs, but only retain the most
    significant.
    """
    ## Constructs an LDResult
    # @param site1
    # @param site2
    # @param r2
    # @param dprime
    # @param p
    # @param n
    @javaConstructorOverload(java_imports['LDResult'],
            (make_sig([],'void'),()),
            (make_sig(['int','int','float','float','float','int'],'void'),
                      (metaInteger,metaInteger,metaFloat,metaFloat,metaFloat,metaInteger)))
    def __init__(self, *args, **kwargs):
        """
        Constructs an LDResult

        Signatures:

        LDResult() # Deprecated
        LDResult(int site1, int site2, float r2, float dprime, float p, int n)

        Arguments:

        site1
        site2
        r2
        dprime
        p
        n
        """
        pass
    ## Gets the r2 value
    # @return The r2 value
    @javaOverload("r2",
                  (make_sig([],'float'),(),None))
    def _r2(self, *args):
        pass
    def r2(self, *args):
        """
        Gets the r2 value

        Signatures:

        float r2()

        Returns:

        The r2 value
        """
        try:
            r2 = self._r2()
            return r2
        except javabridge.JavaException:
            return javabridge.get_field(self.o, "r2","F")
    ## Gets the D' value
    # @return The D' value
    @javaOverload("dPrime",
                  (make_sig([],'float'),(),None))
    def _dPrime(self, *args):
        pass
    def dPrime(self, *args):
        """
        Gets the D' value

        Signatures:

        float dPrime()

        Returns:

        The D' value
        """
        try:
            dPrime = self._dPrime()
            return dPrime
        except javabridge.JavaException:
            return javabridge.get_field(self.o, "dprime","F")
    ## Gets the p-value for r2
    # @return The p-value
    @javaOverload("p",
                  (make_sig([],'float'),(),None))
    def _p(self, *args):
        pass
    def p(self, *args):
        """
        Gets the p-value for r2

        Signatures:

        float p()

        Returns:

        The p value
        """
        try:
            p = self._p()
            return p
        except javabridge.JavaException:
            return javabridge.get_field(self.o, "p","F")
    ## Gets the number of individuals used to calculate LD
    # @return The number of individuals used to calculate LD
    @javaOverload("n",
                  (make_sig([],'int'),(),None))
    def _n(self, *args):
        pass
    def n(self, *args):
        """
        Gets the number of individuals used to calculate LD

        Signatures:

        int n()

        Returns:

        The number of individuals used to calculate LD
        """
        try:
            n = self._n()
            return n
        except javabridge.JavaException:
            return javabridge.get_field(self.o, "n","I")
    ## Gets the first site
    # @return Index of the first site
    @javaOverload("site1",
                  (make_sig([],'int'),(),None))
    def site1(self, *args):
        """
        Gets the first site

        Signatures:

        int site1()

        Returns:

        Index of the first site
        """
        pass
    ## Gets the second site
    # @return Index of the second site
    @javaOverload("site2",
                  (make_sig([],'int'),(),None))
    def site2(self, *args):
        """
        Gets the second site

        Signatures:

        int site2()

        Returns:

        Index of the second site
        """
        pass
    ### Create Builder ###
    class Builder(Object):
        _java_name = java_imports['LDResult']+'$Builder'
        ## Constructs an LDResult builder
        # @param site1 Index of the first site
        # @param site2 Index of the second site
        @javaConstructorOverload(java_imports['LDResult']+'$Builder',
                (make_sig(['int','int'],'void'),(metaInteger,metaInteger)))
        def __init__(self, *args, **kwargs):
            """
            Constructs an LDResult builder

            Signatures:

            Builder(int site1, int site2)

            Arguments:

            site1 -- Index of the first site
            site2 -- Index of the second site
            """
            pass
        ## Builds the LDResult
        # @return The LDResult
        @javaOverload("build",
                      (make_sig([],java_imports['LDResult']),(),
                       lambda x: LDResult(obj=x)))
        def build(self, *args):
            """
            Builds the LDResult

            Signatures:

            LDResult build()

            Returns:

            The LDResult
            """
            pass
        ## Adds the r2 value
        # @param value The r2 vlaue
        # @return The builder with the r2 value included
        @javaOverload("r2",
                      (make_sig(['float'],java_imports['LDResult']+'$Builder'),
                       (metaFloat,),lambda x: LDResult.Builder(obj = x)))
        def r2(self, *args):
            """
            Adds the r2 value

            Signatures:

            Builder r2(float value)

            Arguments:

            value -- The r2 value

            Returns:

            The builder with the r2 value included
            """
            pass
        ## Adds the dprime value
        # @param value The dprime vlaue
        # @return The builder with the dprime value included
        @javaOverload("dprime",
                      (make_sig(['float'],java_imports['LDResult']+'$Builder'),
                       (metaFloat,),lambda x: LDResult.Builder(obj = x)))
        def dprime(self, *args):
            """
            Adds the dprime value

            Signatures:

            Builder dprime(float value)

            Arguments:

            value -- The dprime value

            Returns:

            The builder with the dprime value included
            """
            pass
        ## Adds the p value
        # @param value The p vlaue
        # @return The builder with the p value included
        @javaOverload("p",
                      (make_sig(['float'],java_imports['LDResult']+'$Builder'),
                       (metaFloat,),lambda x: LDResult.Builder(obj = x)))
        def p(self, *args):
            """
            Adds the p value

            Signatures:

            Builder p(float value)

            Arguments:

            value -- The p value

            Returns:

            The builder with the p value included
            """
            pass
        ## Adds the n value
        # @param value The n vlaue
        # @return The builder with the n value included
        @javaOverload("n",
                      (make_sig(['int'],java_imports['LDResult']+'$Builder'),
                       (metaInteger,),lambda x: LDResult.Builder(obj = x)))
        def n(self, *args):
            """
            Adds the n value

            Signatures:

            Builder n(int value)

            Arguments:

            value -- The n value

            Returns:

            The builder with the n value included
            """
            pass
