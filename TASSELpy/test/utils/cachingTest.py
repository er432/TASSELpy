import unittest
from TASSELpy.utils.caching import doubleLinkedList, doubleLinkedListNode
from TASSELpy.utils.caching import LRUcache
from TASSELpy.TASSELbridge import TASSELbridge
import javabridge
try:
    try:
        javabridge.get_env()
    except AttributeError:
        TASSELbridge.start()
    except AssertionError:
        TASSELbridge.start()
except:
    raise RuntimeError("Could not start JVM")

debug = False

class doubleLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.list = doubleLinkedList()
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(4)
    def test_getFirst(self):
        if debug: print("Testing getFirst")
        self.assertEqual(self.list.getFirst(),1)
    def test_getLast(self):
        if debug: print("Testing getLast")
        self.assertEqual(self.list.getLast(),4)
    def test_pop(self):
        if debug: print("Testing pop")
        popped = self.list.pop()
        self.assertEqual(popped,4)
        self.assertEqual(len(self.list),3)
        self.assertEqual(self.list.getLast(),3)
    def test_popleft(self):
        if debug: print("Testing popleft")
        popped = self.list.popleft()
        self.assertEqual(popped,1)
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list.getFirst(),2)
    def test_removeNode(self):
        if debug: print("Testing removeNode")
        newNode1 = doubleLinkedListNode()
        newNode2 = doubleLinkedListNode()
        newNode1.setElement(5)
        newNode2.setElement(6)
        self.list.append(newNode1)
        self.list.append(newNode2)
        self.assertEqual(len(self.list),6)
        self.assertEqual(self.list.getLast(),6)
        self.list.removeNode(newNode1)
        nodeList = [x for x in self.list]
        self.assertEqual([1,2,3,4,6],nodeList)

class LRUcacheTest(unittest.TestCase):
    def test_all(self):
        if debug: print("Testing LRUcache")
        retrieveFunc = lambda x: int(x)
        cache = LRUcache(retrieveFunc, maxsize=3)
        self.assertEqual(cache['1'],1)
        self.assertEqual(cache['2'],2)
        self.assertEqual(cache['3'],3)
        self.assertEqual(cache['4'],4)
        self.assertEqual(len(cache),3)
        self.assertEqual([x for x in cache._keyQueue],['2','3','4'])
        cache['1'] = 1
        self.assertEqual(len(cache),3)
        self.assertEqual([x for x in cache._keyQueue],['3','4','1'])
if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
