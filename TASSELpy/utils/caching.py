from bisect import bisect_left

class doubleLinkedListNode(object):
    """ A node in a double linked list
    """
    def __init__(self):
        """ Instantiates a double linked list node
        """
        # Pointer to the previous node
        self._predecessor = None
        # Pointer to the next node
        self._successor = None
        # The element for the node
        self._element = None
    def getPredecessor(self):
        """ Gets the predecessor of the node

        Returns
        -------
        The predecessor node
        """
        return self._predecessor
    def setPredecessor(self, predecessor):
        """ Sets the predecessor of the node

        Parameters
        ----------
        predecessor : doubleLinkedListNode or None
            The predecessor node
        """
        if predecessor is None:
            pass
        elif not isinstance(predecessor, doubleLinkedListNode):
            raise TypeError("predecessor is not doubleLinkedListNode")
        self._predecessor = predecessor
    def getSuccessor(self):
        """ Gets the successor node

        Returns
        -------
        The successor node
        """
        return self._successor
    def setSuccessor(self, successor):
        """ Sets the successor of the node

        Parameters
        ----------
        successor : doubleLinkedListNode or None
            The successor node
        """
        if successor is None:
            pass
        elif not isinstance(successor, doubleLinkedListNode):
            raise TypeError("successor is not doubleLInkedListNode")
        self._successor = successor
    def getElement(self):
        """ Gets the element for this node

        Returns
        -------
        The element for this node
        """
        return self._element
    def setElement(self, element):
        """ Sets the element in this node

        Parameters
        ----------
        element : object
            The element to go in this node
        """
        self._element = element

class doubleLinkedList(object):
    """ A list of items that have pointers to previous and succeeding items
    """
    def __init__(self):
        """ Instantiates a doubleLinkedList
        """
        self._size = 0
        self._front = doubleLinkedListNode()
        self._back = self._front
    def __len__(self):
        return self._size
    def __iter__(self):
        node = self._front
        while node.getElement():
            yield node.getElement()
            node = node.getSuccessor()
    def append(self, element):
        """ Appends an element to the linked list

        Parameters
        ----------
        element : object
            The element to place at the rear of the list. If this is a
            doubleLinkedListNode, it will be added directly instead of being
            put into another doubleLinkedListNode first
        """
        if isinstance(element, doubleLinkedListNode):
            former_last = self._back.getPredecessor()
            self._back.setPredecessor(element)
            element.setSuccessor(self._back)
            if former_last:
                element.setPredecessor(former_last)
                former_last.setSuccessor(element)
            if self._front == self._back:
                self._front = element
        else:
            self._back.setElement(element)
            new_back = doubleLinkedListNode()
            self._back.setSuccessor(new_back)
            new_back.setPredecessor(self._back)
            self._back = new_back
        self._size += 1
    def getFirst(self):
        """ Gets the first element in the linked list

        Returns
        -------
        The first element in the list
        """
        return self._front.getElement()
    def getLast(self):
        """ Gets the last element in the linked list

        Returns
        -------
        The last element in the linked list
        """
        if len(self) > 0:
            return self._back.getPredecessor().getElement()
    def pop(self):
        """ Gets and removes the last element in the linked list

        Returns
        -------
        The last element in the list
        """
        if len(self) == 0:
            raise IndexError("pop from empty list")
        removeNode = self._back.getPredecessor()
        self._back.setPredecessor(removeNode.getPredecessor())
        removeNode.getPredecessor().setSuccessor(self._back)
        self._size -= 1
        return removeNode.getElement()
    def popleft(self):
        """ Gets and removes the first element in the linked list

        Returns
        ------
        The first element in the list
        """
        if len(self) == 0:
            raise IndexError("popleft from empty list")
        removeNode = self._front
        self._front.getSuccessor().setPredecessor(None)
        self._front = self._front.getSuccessor()
        self._size -= 1
        return removeNode.getElement()
    def removeNode(self, node):
        """ Removes a node from the linked list

        Parameters
        ----------
        node : doubleLinkedListNode object
            The node to be removed
        """
        pred_node = node.getPredecessor()
        succ_node = node.getSuccessor()
        if pred_node:
            pred_node.setSuccessor(succ_node)
        if succ_node:
            succ_node.setPredecessor(pred_node)
        self._size -= 1
class LRUcache(dict):
    """ A least recently used cache
    """
    def __init__(self, retrieveFunc, maxsize=1000, *args, **kwargs):
        """ Instantiates the LRUcache

        Parameters
        ----------
        retrieveFunc : callable
            Function that takes a key as an argument and returns the value
            corresponding to that key
        maxsize : int
            The maximum size the cache can keep before kicking keys out
        """
        if not hasattr(retrieveFunc, '__call__'):
            raise TypeError("retrieveFunc not callable")
        # Call the dictionary constructor
        super(LRUcache, self).__init__(*args, **kwargs)
        self._retrieveFunc = retrieveFunc
        self._maxsize = maxsize
        # Create dictionary of key -> node object and doublelinkedList
        # of keys
        self._keyNodeDict = {}
        self._keyQueue = doubleLinkedList()
        for key in self:
            node = doubleLinkedListNode()
            node.setElement(key)
            self._keyNodeDict[key] = node
            self._keyQueue.append(node)
    def __setitem__(self, key, val):
        """ Adds a new item to the cache

        Parameters
        ----------
        key : hashable
            The key to use for indexing the val
        val : object
            The value
        """
        if len(self._keyQueue) == self._maxsize:
            # Pop out the least recently used key/value pair if at the
            # maximum size
            pop_key = self._keyQueue.popleft()
            del self[pop_key]
            del self._keyNodeDict[pop_key]
        # Check if the key already in the cache, and then
        # determine how to act
        if key in self:
            # If key already in the cache, put it at the end of the queue
            removeNode = self._keyNodeDict[key]
            self._keyQueue.removeNode(removeNode)
            self._keyQueue.append(removeNode)
            # Put it in the regular dictionary
            dict.__setitem__(self, key, val)
        else:
            appendNode = doubleLinkedListNode()
            appendNode.setElement(key)
            self._keyQueue.append(appendNode)
            self._keyNodeDict[key] = appendNode
            dict.__setitem__(self, key, val)
    def __getitem__(self, key):
        """ Gets an item from the cache

        Parameters
        ----------
        key : Hashable
            Key value
        """
        if key in self:
            # If key already present, move to the end of the queue
            removeNode = self._keyNodeDict[key]
            self._keyQueue.removeNode(removeNode)
            self._keyQueue.append(removeNode)
        # Use the superclass function to return the value
        return dict.__getitem__(self, key)
    def __missing__(self, key):
        """ Called when there is a cache miss

        Finds and sets the item using the retrieveFunc supplied

        Parameters
        ----------
        key : Hashable

        Returns
        -------
        The value associated with the key
        """
        val = self._retrieveFunc(key)
        self[key] = val
        return dict.__getitem__(self, key)
