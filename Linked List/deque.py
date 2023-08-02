#deque implementation in python using doubly linked lists

class LinkedDeque:
    #---------------------------------Node Class--------------------------------------
    class _Node:
        #stores element and next link for a node
        
        #__slots__ reduces memory usage
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    #------------------------------internal methods------------------------------------
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
    
    def delete_node(self, node, predecessor, successor):
        #deletes node between predecessor and successor
        node._prev = node._next = node._element = None
        successor._prev = predecessor
        predecessor._next = successor
        

    #---------------------------------user methods--------------------------------------
    def first(self):
        #returns first element
        return self._header._next._element
    
    def last(self):
        #returns last element
        return self._trailer._prev._element
    
    def add_first(self, element):
        #adds element to front of queue
        self.add_node(element, self._header, self._header._next)
        self._size += 1

    def add_last(self, element):
        #adds element to end of queue
        self.add_node(element, self._trailer._prev, self._trailer)
        self._size += 1
    
    def delete_first(self):
        #deletes element at front of queue and returns it
        if self.is_empty():
            raise Empty("Deque is empty")
        
        node = self._header._next
        answer = node._element
        self.delete_node(node, self._header, node._next)

        self._size -= 1
        return answer
    
    def delete_last(self):
        #deletes element at end of queue and returns it
        if self.is_empty():
            raise Empty("Deque is empty")
        
        node = self._trailer._prev
        answer = node._element
        self.delete_node(node, node._prev, self._trailer)

        self._size -= 1
        return answer
    

class Empty(Exception):
    pass