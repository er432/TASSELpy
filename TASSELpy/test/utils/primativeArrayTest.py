import unittest
import javabridge
from TASSELpy.TASSELbridge import TASSELbridge
try:
    try:
        javabridge.get_env()
    except AttributeError:
        TASSELbridge.start()
    except AssertionError:
        TASSELbridge.start()
except:
    raise RuntimeError("Could not start JVM")
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.javaObj import javaArray
from TASSELpy.java.lang.Byte import metaByte
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Long import metaLong
from TASSELpy.java.lang.Float import metaFloat
from TASSELpy.java.lang.Double import metaDouble
import numpy as np

class primativeArrayTest(unittest.TestCase):
    def test_byteArray(self):
        print "Testing byteArray"
        arr = javaPrimativeArray.make_array('byte',2)
        self.assertIsInstance(arr, javaPrimativeArray.get_array_type('byte'))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0] = np.int8(2)
        arr[1] = np.int8(3)
        self.assertIsInstance(arr[0], metaByte)
        self.assertEqual(arr[1],np.int8(3))
    def test_byteDblArray(self):
        print "Testing double byteArray"
        arr = javaPrimativeArray.make_dbl_array('byte',2,3)
        self.assertIsInstance(arr, javaArray.get_array_type(javaPrimativeArray.get_array_type('byte')))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0][0] = np.int8(2)
        arr[1][1] = np.int8(3)
        self.assertIsInstance(arr[0][0], metaByte)
        self.assertEqual(arr[1][1],np.int8(3))
    def test_intArray(self):
        print "Testing intArray"
        arr = javaPrimativeArray.make_array('int',2)
        self.assertIsInstance(arr, javaPrimativeArray.get_array_type('int'))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0] = np.int32(2)
        arr[1] = np.int32(3)
        self.assertIsInstance(arr[0], metaInteger)
        self.assertEqual(arr[1],np.int32(3))
    def test_intDblArray(self):
        print "Testing double intArray"
        arr = javaPrimativeArray.make_dbl_array('int',2,3)
        self.assertIsInstance(arr, javaArray.get_array_type(javaPrimativeArray.get_array_type('int')))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0][0] = np.int32(2)
        arr[1][1] = np.int32(3)
        self.assertIsInstance(arr[0][0], metaInteger)
        self.assertEqual(arr[1][1],np.int32(3))
    def test_longArray(self):
        print "Testing longArray"
        arr = javaPrimativeArray.make_array('long',2)
        self.assertIsInstance(arr, javaPrimativeArray.get_array_type('long'))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0] = np.int64(2)
        arr[1] = np.int64(3)
        self.assertIsInstance(arr[0], metaLong)
        self.assertEqual(arr[1],np.int64(3))
    def test_longDblArray(self):
        print "Testing double longArray"
        arr = javaPrimativeArray.make_dbl_array('long',2,3)
        self.assertIsInstance(arr, javaArray.get_array_type(javaPrimativeArray.get_array_type('long')))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0][0] = np.int64(2)
        arr[1][1] = np.int64(3)
        self.assertIsInstance(arr[0][0], metaLong)
        self.assertEqual(arr[1][1],np.int64(3))
    def test_floatArray(self):
        print "Testing floatArray"
        arr = javaPrimativeArray.make_array('float',2)
        self.assertIsInstance(arr, javaPrimativeArray.get_array_type('float'))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0] = np.float32(2)
        arr[1] = np.float32(3)
        self.assertIsInstance(arr[0], metaFloat)
        self.assertEqual(arr[1],np.float32(3))
    def test_floatDblArray(self):
        print "Testing double floatArray"
        arr = javaPrimativeArray.make_dbl_array('float',2,3)
        self.assertIsInstance(arr, javaArray.get_array_type(javaPrimativeArray.get_array_type('float')))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0][0] = np.float32(2)
        arr[1][1] = np.float32(3)
        self.assertIsInstance(arr[0][0], metaFloat)
        self.assertEqual(arr[1][1],np.float32(3))
    def test_doubleArray(self):
        print "Testing doubleArray"
        arr = javaPrimativeArray.make_array('double',2)
        self.assertIsInstance(arr, javaPrimativeArray.get_array_type('double'))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0] = np.float64(2)
        arr[1] = np.float64(3)
        self.assertIsInstance(arr[0], metaDouble)
        self.assertEqual(arr[1],np.float64(3))
    def test_doubleDblArray(self):
        print "Testing double doubleArray"
        arr = javaPrimativeArray.make_dbl_array('double',2,3)
        self.assertIsInstance(arr, javaArray.get_array_type(javaPrimativeArray.get_array_type('double')))
        self.assertIsInstance(arr.o, javabridge.JB_Object)
        arr[0][0] = np.float64(2)
        arr[1][1] = np.float64(3)
        self.assertIsInstance(arr[0][0], metaDouble)
        self.assertEqual(arr[1][1],np.float64(3))
    def test_to_numpy_array(self):
        print "Testing to_numpy_array with double"
        # Single array
        arr = javaPrimativeArray.make_array('double',2)
        arr[0] = np.float64(2)
        arr[1] = np.float64(3)
        np_arr = arr.to_numpy_array()
        self.assertIsInstance(np_arr,np.ndarray)
        self.assertEqual(arr[0],np_arr[0])
        self.assertEqual(arr[1],np_arr[1])
        self.assertIsInstance(arr[0],np.float64)
        # Double array
        arr = javaPrimativeArray.make_dbl_array('double',2,3)
        arr[0][0] = np.float64(2)
        arr[1][1] = np.float64(3)
        np_arr = arr.to_numpy_array()
        self.assertIsInstance(np_arr,np.ndarray)
        self.assertEqual(arr[0][0],np_arr[0][0])
        self.assertEqual(arr[1][1],np_arr[1][1])
        self.assertIsInstance(np_arr[0][0],np.float64)
if __name__ == "__main__":
    unittest.main(exit=False)
    TASSELbridge.stop()
