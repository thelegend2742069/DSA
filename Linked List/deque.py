#deque implementation in python using doubly linked lists

class LinkedDeque:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self) -> None:
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def add_node(self, element, predecessor, successor):
        node = self._Node(element, predecessor, successor)
        successor._prev = node
        predecessor._next = node
    
    def delete_node(self, node, predecessor, successor):
        node._prev = node._next = node._element = None
        successor._prev = predecessor
        predecessor._next = successor
        
    
    def first(self):
        return self._header._next._element
    
    def last(self):
        return self._trailer._prev._element
    
    def add_first(self, element):
        self.add_node(element, self._header, self._header._next)
        self._size += 1

    def add_last(self, element):
        self.add_node(element, self._trailer._prev, self._trailer)
        self._size += 1
    
    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        
        node = self._header._next
        answer = node._element
        self.delete_node(node, self._header, node._next)
        self._size -= 1

        return answer
    
    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        
        node = self._trailer._prev
        answer = node._element
        self.delete_node(node, node._prev, self._trailer)
        self._size -= 1
        #print(answer)
        return answer
    

class Empty(Exception):
    pass