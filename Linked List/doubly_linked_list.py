#doubly linked list implementation

class DoublyLinkedList:
    #---------------------------------Node Class--------------------------------------
    class _Node:
        #stores element and next link for a node
        
        #__slots__ reduces memory usage
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    #----------------------------------methods----------------------------------------
    def __init__(self) -> None:
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer      #set header's next element as trailer
        self._trailer._prev = self._header      #set trailer's next element as header
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def add_node(self, element, predecessor, successor):
        #inserts element between predecessor and successor
        node = self._Node(element, predecessor, successor)
        successor._prev = node
        predecessor._next = node
        self._size += 1
    
    def delete_node(self, node, predecessor, successor):
        #deletes node between predecessor and successor
        answer = node._element
        node._prev = node._next = node._element = None
        successor._prev = predecessor
        predecessor._next = successor
        self._size -= 1
        return answer