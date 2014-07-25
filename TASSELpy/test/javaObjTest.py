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
from TASSELpy.javaObj import *
from TASSELpy.java.lang.String import String
from TASSELpy.java.lang.Integer import Integer
from TASSELpy.java.util.ArrayList import ArrayList
import numpy as np

debug = False

java_imports = {'String':'java/lang/String'}
class javaObjTest(unittest.TestCase):
    """ Tests for javaObj in javaObj.py """
    def test_javaObjType(self):
        if debug: print "Testing javaObj type instance with String"
        val = String('TASSELpy')
        self.assertIsInstance(val, javaObj)
    def test_getArray(self):
        if debug: print "Testing javaObj.getArray method with String"
        arr = String.getArray(2)
        arr[0] = 'TASSELpy'
        self.assertEquals(arr[0],'TASSELpy')
    def test_getDblArray(self):
        if debug: print "Testing javaObj.getDblArray method with String"
        arr = String.getDblArray(2,2)
        arr[0][1] = 'TASSELpy'
        arr[1][0] = 'TASSEL'
        self.assertEquals(arr[0][1], 'TASSELpy')
        self.assertEquals(arr[1][0], 'TASSEL')
        self.assertIsNone(arr[0][0])
        self.assertIsNone(arr[1][1])
    def test_wrap_existing_array(self):
        if debug: print "Testing javaObj.wrap_existing_array with String"
        string_class = javabridge.get_env().find_class(java_imports['String'])
        str_constructor = javabridge.get_env().get_method_id(string_class,'<init>','(Ljava/lang/String;)V')
        str1 = javabridge.get_env().new_object(string_class,str_constructor,String('TASSELpy').o)
        str2 = javabridge.get_env().new_object(string_class,str_constructor,String('TASSEL').o)
        arr = javabridge.get_env().make_object_array(2,string_class)
        javabridge.get_env().set_object_array_element(arr, 0, str1)
        javabridge.get_env().set_object_array_element(arr, 1, str2)
        pyarr = String.wrap_existing_array(arr)
        self.assertEquals(pyarr[0], 'TASSELpy')
        self.assertEquals(pyarr[1], 'TASSEL')
        self.assertIsInstance(pyarr[0],String)
        self.assertIsInstance(pyarr[1],String)

class javaArrayTest(unittest.TestCase):
    """ Tests for javaArray in javaObj.py """
    def setUp(self):
        # Set up a test String array
        self.arr = String.getArray(2)
        self.arr[0] = 'TASSELpy'
        self.arr[1] = 'TASSEL'
    def test_setitem(self):
        if debug: print "Testing javaArray __setitem__"
        self.arr[0] = 'Eli'
        self.assertEquals(self.arr[0], 'Eli')
        self.assertRaises(TypeError, lambda x: self.arr.__setitem__(0,x), (1,))
    def test_len(self):
        if debug: print "Testing javaArray __len__"
        self.assertEquals(len(self.arr), 2)
    def test_iter(self):
        if debug: print "Testing javaArray __iter__"
        self.assertEquals([x for x in self.arr],[String('TASSELpy'),String('TASSEL')])
    def test_get_array_type(self):
        if debug: print "Testing javaArray get_array_type"
        self.assertIsInstance(self.arr, javaArray.get_array_type(String))
        self.assertNotIsInstance(self.arr, javaArray.get_array_type(Integer))
    def test_to_numpy_array(self):
        if debug: print "Testing to_numpy_array"
        self.assertIsInstance(self.arr.to_numpy_array(),np.ndarray)
        self.assertIsInstance(self.arr.to_numpy_array().dtype,np.object)
        arr = String.getDblArray(2,2)
        arr[0][1] = 'TASSELpy'
        arr[1][0] = 'TASSEL'
        np_arr = arr.to_numpy_array()
        self.assertEqual(np_arr[0][1],arr[0][1])
        self.assertIsInstance(np_arr,np.ndarray)

class genericJavaObjTest(unittest.TestCase):
    """ Tests for genericJavaObj """
    def test_constructor(self):
        if debug: print "Testing genericJavaObj constructor using ArrayList with Strings"
        arrlist = ArrayList(generic=(String,))
        self.assertIsInstance(arrlist, ArrayList)
        self.assertTrue(hasattr(arrlist,'generic_dict'))
        self.assertEquals(arrlist.generic_dict['/@1/'],String)
    def test_generic_setitem(self):
        if debug: print "Testing setitem on ArrayList with Strings, Integers for genericJavaObj"
        arrlist = ArrayList(generic=(String,))
        arrlist.add(String('TASSELpy'))
        arrlist.add(String('TASSEL'))
        arrlist2 = ArrayList(generic=(Integer,))
        arrlist2.add(Integer(1))
        arrlist2.add(Integer(2))
        arrlist2.add(Integer(3))
        self.assertEquals(arrlist.size(),2)
        self.assertEquals(arrlist2.size(),3)
        arrlist[0] = String('TASSELpy')
        self.assertRaises(KeyError, lambda x: arrlist.__setitem__(0,x),
                             (Integer(1),))
        self.assertRaises(KeyError, lambda x: arrlist2.__setitem__(0,x),
                             (String('1'),))        
    def test_generic_getitem(self):
        if debug: print "Testing getitem on ArrayList with Strings, Integers for genericJavaObj"
        arrlist = ArrayList(generic=(String,))
        arrlist.add(String('TASSELpy'))
        arrlist.add(String('TASSEL'))
        self.assertIsInstance(arrlist[0],String)
        self.assertIsInstance(arrlist[1],String)
        arrlist2 = ArrayList(generic=(Integer,))
        arrlist2.add(Integer(1))
        arrlist2.add(Integer(2))
        arrlist2.add(Integer(3))
        self.assertEquals(arrlist[0],String('TASSELpy'))
        self.assertEquals(arrlist[1],String('TASSEL'))
        self.assertIsInstance(arrlist2[0], Integer)
        self.assertIsInstance(arrlist2[2], Integer)
        self.assertEquals(arrlist2[1],Integer(2))

        

if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
