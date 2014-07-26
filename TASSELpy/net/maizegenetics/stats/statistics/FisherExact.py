from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.helper import make_sig
import numpy as np

java_imports = {'FisherExact':'net/maizegenetics/stats/statistics/FisherExact'}

class FisherExact(Object):
    _java_name = java_imports['FisherExact']
    """
    This does a Fisher Exact test.  The Fisher's Exact test procedure
    calculates an exact probability value for the relationship between
    two dichotomous variables, as found in a two by two crosstable. The
    program calculates the difference between the data observed and the
    data expected, considering the given marginal and the assumptions
    of the model of independence. It works in exactly the same way as
    the Chi-square test for independence; however, the Chi-square gives
    only an estimate of the true probability value, an estimate which
    might not be very accurate if the marginal is very uneven or if
    there is a small value (less than five) in one of the cells.

    It uses an array of factorials initialized at the beginning to
    provide speed.  There could be better ways to do this.
    """
    ## Constructor for FisherExact table
    @javaConstructorOverload(java_imports['FisherExact'],
            (make_sig(['int'],'void'),(metaInteger,)),
            (make_sig(['int','boolean'],'void'), (metaInteger,metaBoolean)))
    def __init__(self, *args, **kwargs):
        """
        Constructor for FisherExact table

        FisherExact(int maxSize)
        FisherExact(int maxSize, boolean useLookup)

        Arguments:

        FisherExact(int maxSize)
            maxSize -- the maximum sum that will be encountered by the table (a+b+c+d)
        FisherExact(int maxSize, boolean useLookup)
            maxSize -- the maximum sum that will be encountered by the table (a+b+c+d)
            useLookup -- doesn't appear to actually be used
        """
        pass
    ## Calculates the P-value for this specific state
    # a,b,c, and d are the 4 cells in a 2x2 table
    # @return The p-value
    @javaOverload("getP",
                  (make_sig(['int','int','int','int'],'double'),
                   (metaInteger,metaInteger,metaInteger,metaInteger),np.float64))
    def getP(self, *args):
        """
        Calculates the P-value for this specific state

        final double getP(int a, int b, int c, int d)

        Arguments:

        a, b, c, and d are the 4 cells in a 2x2 table

        Returns:

        The p-value
        """
        pass
    ## Calculates the one-tail P-value for the Fisher Exact test. Deterimes whether to
    # calculate the right or left-tial, thereby always returning the smallest p-value
    # @return one-tailed P-value (right or left, whichever is smallest)
    @javaOverload("getCumlativeP",
                  (make_sig(['int','int','int','int'],'double'),
                   (metaInteger,metaInteger,metaInteger,metaInteger),np.float64))
    def getCumulativeP(self, *args):
        """
        Calculates the one-tail P-value for the Fisher Exact test. Determines whether to
        calculate the right- or left- tail, thereby always returning the smallest p-value

        Signatures:

        final double getCumlativeP(int a, int b, int c, int d)
        
        Arguments:

        a, b, c, and d are the 4 cells in a 2x2 table

        Returns:

        one-tailed P-value (right or left, whichever is smallest)
        """
        pass
    ## Calculates the right-tail P-value for the Fisher Exact test.
    # a,b,c, and d are the 4 cells in a 2x2 table
    # @return right-tailed P-value
    @javaOverload("getRightTailedP",
                  (make_sig(['int','int','int','int'],'double'),
                   (metaInteger,metaInteger,metaInteger,metaInteger),np.float64))
    def getRightTailedP(self, *args):
        """
        Calculates the right-tail P-value for the Fisher Exact test.

        Signatures:

        final double getRightTailedP(int a, int b, int c, int d)
        
        Arguments:

        a, b, c, and d are the 4 cells in a 2x2 table

        Returns:

        right-tailed P-value
        """
        pass
    ## Calculates the right-tail P-value for the Fisher Exact test.
    # a,b,c, and d are the 4 cells in a 2x2 table
    # @param maxP maximum p-value allowed
    # @return right-tailed P-value
    @javaOverload("getRightTailedPQuick",
                  (make_sig(['int','int','int','int','double'],'double'),
                   (metaInteger,metaInteger,metaInteger,metaInteger,metaDouble),np.float64))
    def getRightTailedPQuick(self, *args):
        """
        Calculates the right-tail P-value for the Fisher Exact test.

        Signatures:

        final double getRightTailedPQuick(int a, int b, int c, int d, double maxP)
        
        Arguments:

        a, b, c, and d are the 4 cells in a 2x2 table
        maxP -- maximum p-value possible
        
        Returns:

        right-tailed P-value
        """
        pass
    ## Calculates the left-tail P-value for the Fisher Exact test.
    # a,b,c, and d are the 4 cells in a 2x2 table
    # @return left-tailed P-value
    @javaOverload("getLeftTailedP",
                  (make_sig(['int','int','int','int'],'double'),
                   (metaInteger,metaInteger,metaInteger,metaInteger),np.float64))
    def getLeftTailedP(self, *args):
        """
        Calculates the left-tail P-value for the Fisher Exact test.

        Signatures:

        final double getLeftTailedP(int a, int b, int c, int d)
        
        Arguments:

        a, b, c, and d are the 4 cells in a 2x2 table

        Returns:

        left-tailed P-value
        """
        pass
    ## Calculates the two-tail P-value for the Fisher Exact test.
    # a,b,c, and d are the 4 cells in a 2x2 table
    # @return two-tailed P-value
    @javaOverload("getTwoTailedP",
                  (make_sig(['int','int','int','int'],'double'),
                   (metaInteger,metaInteger,metaInteger,metaInteger),np.float64))
    def getTwoTailedP(self, *args):
        """
        Calculates the two-tail P-value for the Fisher Exact test.

        Signatures:

        final double getTwoTailedP(int a, int b, int c, int d)
        
        Arguments:

        a, b, c, and d are the 4 cells in a 2x2 table

        Returns:

        two-tailed P-value
        """
        pass
