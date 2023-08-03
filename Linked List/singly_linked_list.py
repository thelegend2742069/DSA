class SinglyLinkedList:
    #---------------------------------Node Class--------------------------------------
    class _Node:
        #stores element and next link for a node
        
        #__slots__ reduces memory usage
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    #------------------------------internal methods------------------------------------
    def __init__(self):
        self._head = self._Node(None, None)
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def add_node(self, element):
        new = self._Node(element, self._head)
        self._head = new
        self._size += 1
    
    def delete_node(self, node):
        answer = node._element
        self._head = node._next
        node._element = node._next = None
        self._size -= 1
        return answer
