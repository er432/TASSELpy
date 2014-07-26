from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaStaticOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Byte import metaByte
from TASSELpy.java.lang.Float import metaFloat
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.java.lang.Long import metaLong
from TASSELpy.javaObj import javaObj
import numpy as np

java_imports = {'Array':'java/lang/reflect/Array',
                'Object':'java/lang/Object'}
class Array(Object):
    """
    public final class Array extends Object

    The Array class provides static methods to dynamically create and access Java arrays

    Array permits widening conversions to occur during a get or set operation, but throws
    an IllegalArgumentException if a narrowing conversion would occur
    """
    ## Returns the value of the indexed component in the specified array object
    # @param array The array
    # @param index The index of the object you want to get
    # @return The object you want to get
    @javaStaticOverload(java_imports['Array'],'get',
            (make_sig([java_imports['Object'],'int'],java_imports['Object']),
             (javaObj,metaInteger),lambda x: Object(obj=x)))
    def get(*args):
        """
        Returns the value of the indexed component in the specified array object

        Signatures:

        static Object get(Object array, int index)

        Arguments:

        array -- The array
        index -- The index of the object you want to get

        Returns:

        The object you want to get
        """
        pass
    ## Returns the value of of the indexed component in the specified array object, as a boolean
    # @param array The array
    # @param index The index of the boolean you want to get
    # @return The value as a boolean
    @javaStaticOverload(java_imports['Array'],'getBoolean',
                        (make_sig([java_imports['Object'],'int'],'boolean'),
                         (javaObj,metaInteger),None))
    def getBoolean(*args):
        """
        Returns the value of the indexed component in the specified array object, as a boolean

        Signatures:

        static boolean getBoolean(Object array, int index)

        Argumnts:

        array -- The array
        index -- The index of the boolean you want to get

        Returns:

        The value as a boolean
        """
        pass
    ## Returns the value of of the indexed component in the specified array object, as a byte
    # @param array The array
    # @param index The index of the byte you want to get
    # @return The value as a byte
    @javaStaticOverload(java_imports['Array'],'getByte',
                        (make_sig([java_imports['Object'],'int'],'byte'),
                         (javaObj,metaInteger),np.int8))
    def getByte(*args):
        """
        Returns the value of the indexed component in the specified array object, as a byte

        Signatures:

        static byte getByte(Object array, int index)

        Argumnts:

        array -- The array
        index -- The index of the byte you want to get

        Returns:

        The value as a byte
        """
        pass
    ## Returns the value of of the indexed component in the specified array object, as a char
    # @param array The array
    # @param index The index of the char you want to get
    # @return The value as a char
    @javaStaticOverload(java_imports['Array'],'getChar',
                        (make_sig([java_imports['Object'],'int'],'char'),
                         (javaObj,metaInteger),None))
    def getChar(*args):
        """
        Returns the value of the indexed component in the specified array object, as a char

        Signatures:

        static char getChar(Object array, int index)

        Argumnts:

        array -- The array
        index -- The index of the char you want to get

        Returns:

        The value as a char
        """
        pass
    ## Returns the value of of the indexed component in the specified array object, as a double
    # @param array The array
    # @param index The index of the double you want to get
    # @return The value as a double
    @javaStaticOverload(java_imports['Array'],'getDouble',
                        (make_sig([java_imports['Object'],'int'],'double'),
                         (javaObj,metaInteger),np.float64))
    def getDouble(*args):
        """
        Returns the value of the indexed component in the specified array object, as a double

        Signatures:

        static double getDouble(Object array, int index)

        Argumnts:

        array -- The array
        index -- The index of the double you want to get

        Returns:

        The value as a double
        """
        pass
    ## Returns the value of of the indexed component in the specified array object, as a float
    # @param array The array
    # @param index The index of the float you want to get
    # @return The value as a float
    @javaStaticOverload(java_imports['Array'],'getFloat',
                        (make_sig([java_imports['Object'],'int'],'float'),
                         (javaObj,metaInteger),None))
    def getFloat(*args):
        """
        Returns the value of the indexed component in the specified array object, as a float

        Signatures:

        static float getFloat(Object array, int index)

        Argumnts:

        array -- The array
        index -- The index of the float you want to get

        Returns:

        The value as a float
        """
        pass
    ## Returns the value of of the indexed component in the specified array object, as a int
    # @param array The array
    # @param index The index of the int you want to get
    # @return The value as a int
    @javaStaticOverload(java_imports['Array'],'getInt',
                        (make_sig([java_imports['Object'],'int'],'int'),
                         (javaObj,metaInteger),None))
    def getInt(*args):
        """
        Returns the value of the indexed component in the specified array object, as a int

        Signatures:

        static int getInt(Object array, int index)

        Argumnts:

        array -- The array
        index -- The index of the int you want to get

        Returns:

        The value as a int
        """
        pass
    ## Returns the length of the specified array object, as an int
    # @param array The array
    # @return The length of the array
    @javaStaticOverload(java_imports['Array'],'getLength',
                        (make_sig([java_imports['Object']],'int'),(javaObj,),None))
    def getLength(*args):
        """
        Returns the length of the specified array object, as an int

        Signatures:

        static int getLength(Object array)

        Arguments:

        array -- The array

        Returns:

        The length of the array
        """
        pass
    ## Returns the value of of the indexed component in the specified array object, as a long
    # @param array The array
    # @param index The index of the long you want to get
    # @return The value as a long
    @javaStaticOverload(java_imports['Array'],'getLong',
                        (make_sig([java_imports['Object'],'int'],'long'),
                         (javaObj,metaInteger),np.int64))
    def getLong(*args):
        """
        Returns the value of the indexed component in the specified array object, as a long

        Signatures:

        static long getLong(Object array, int index)

        Argumnts:

        array -- The array
        index -- The index of the long you want to get

        Returns:

        The value as a long
        """
        pass
    ## Returns the value of of the indexed component in the specified array object, as a short
    # @param array The array
    # @param index The index of the short you want to get
    # @return The value as a short
    @javaStaticOverload(java_imports['Array'],'getShort',
                        (make_sig([java_imports['Object'],'int'],'short'),
                         (javaObj,metaInteger),None))
    def getShort(*args):
        """
        Returns the value of the indexed component in the specified array object, as a short

        Signatures:

        static short getShort(Object array, int index)

        Argumnts:

        array -- The array
        index -- The index of the short you want to get

        Returns:

        The value as a short
        """
        pass
    ## Sets the value of the indexed component of the specified array object at the specified new value
    # @param array The array
    # @param index Where you want to put the object
    # @param value The object you want to put in the Array
    @javaStaticOverload(java_imports['Array'],'set',
                        (make_sig([java_imports['Object'],'int',java_imports['Object']],'void'),
                         (javaObj,metaInteger,javaObj),None))
    def set(*args):
        """
        Sets the vlaue of the indexed component of the specified array object ot the specified new value

        Signatures:

        static void set(Object array, int index, Object value)

        Arguments:

        array -- The array
        index -- Where you want to put the object
        value -- The object you want to put in the array
        """
        pass
    ## Sets the value of the indexed component of the specified array object to the specified boolean
    # value
    # @param array The array
    # @param index Where you want to put the boolean
    # @param value the boolean value
    @javaStaticOverload(java_imports['Array'],'setBoolean',
                        (make_sig([java_imports['Object'],'int','boolean'],'void'),
                         (javaObj,metaInteger,metaBoolean),None))
    def setBoolean(*args):
        """
        Sets the value of the indexed component of the specified array object to the specified boolean
        value

        Signatures:

        static void setBoolean(Object array, int index, boolean v)

        Arguments:

        array -- The array
        index -- Where you want to put the boolean
        value -- The boolean value
        """
        pass
    ## Sets the value of the indexed component of the specified array object to the specified byte
    # value
    # @param array The array
    # @param index Where you want to put the byte
    # @param value the byte value
    @javaStaticOverload(java_imports['Array'],'setByte',
                        (make_sig([java_imports['Object'],'int','byte'],'void'),
                         (javaObj,metaInteger,metaByte),None))
    def setByte(*args):
        """
        Sets the value of the indexed component of the specified array object to the specified byte
        value

        Signatures:

        static void setByte(Object array, int index, byte v)

        Arguments:

        array -- The array
        index -- Where you want to put the byte
        value -- The byte value
        """
        pass
    ## Sets the value of the indexed component of the specified array object to the specified double
    # value
    # @param array The array
    # @param index Where you want to put the double
    # @param value the double value
    @javaStaticOverload(java_imports['Array'],'setDouble',
                        (make_sig([java_imports['Object'],'int','double'],'void'),
                         (javaObj,metaInteger,metaDouble),None))
    def setDouble(*args):
        """
        Sets the value of the indexed component of the specified array object to the specified double
        value

        Signatures:

        static void setDouble(Object array, int index, double v)

        Arguments:

        array -- The array
        index -- Where you want to put the double
        value -- The double value
        """
        pass
    ## Sets the value of the indexed component of the specified array object to the specified float
    # value
    # @param array The array
    # @param index Where you want to put the float
    # @param value the float value
    @javaStaticOverload(java_imports['Array'],'setFloat',
                        (make_sig([java_imports['Object'],'int','float'],'void'),
                         (javaObj,metaInteger,metaFloat),None))
    def setFloat(*args):
        """
        Sets the value of the indexed component of the specified array object to the specified float
        value

        Signatures:

        static void setFloat(Object array, int index, float v)

        Arguments:

        array -- The array
        index -- Where you want to put the float
        value -- The float value
        """
        pass
    ## Sets the value of the indexed component of the specified array object to the specified int
    # value
    # @param array The array
    # @param index Where you want to put the int
    # @param value the int value
    @javaStaticOverload(java_imports['Array'],'setInt',
                        (make_sig([java_imports['Object'],'int','int'],'void'),
                         (javaObj,metaInteger,metaInteger),None))
    def setInt(*args):
        """
        Sets the value of the indexed component of the specified array object to the specified int
        value

        Signatures:

        static void setInt(Object array, int index, int v)

        Arguments:

        array -- The array
        index -- Where you want to put the int
        value -- The int value
        """
        pass
    ## Sets the value of the indexed component of the specified array object to the specified long
    # value
    # @param array The array
    # @param index Where you want to put the long
    # @param value the long value
    @javaStaticOverload(java_imports['Array'],'setLong',
                        (make_sig([java_imports['Object'],'int','long'],'void'),
                         (javaObj,metaInteger,metaLong),None))
    def setLong(*args):
        """
        Sets the value of the indexed component of the specified array object to the specified long
        value

        Signatures:

        static void setLong(Object array, int index, long v)

        Arguments:

        array -- The array
        index -- Where you want to put the long
        value -- The long value
        """
        pass





