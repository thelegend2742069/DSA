#deque implementation in python using doubly linked lists

from doubly_linked_list import DoublyLinkedList

class LinkedDeque(DoublyLinkedList):
    #returns frist element
    def first(self):
        return self._header._next._element
    
    #returns last element
    def last(self):
        return self._trailer._prev._element
    
    #adds element to front of queue
    def add_first(self, element):
        self.add_node(element, self._header, self._header._next)
        self._size += 1

    #adds element to end of queue
    def add_last(self, element):
        self.add_node(element, self._trailer._prev, self._trailer)
        self._size += 1
    
    #deletes element at front of queue and returns it
    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")           #raises error if queue is empty
        
        node = self._header._next
        answer = node._element
        self.delete_node(node, self._header, node._next)

        self._size -= 1
        return answer
    
    #deletes element at end of queue and returns it
    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")           #raises error if queue is empty
        
        node = self._trailer._prev
        answer = node._element
        self.delete_node(node, node._prev, self._trailer)

        self._size -= 1
        return answer
    

class Empty(Exception):
    pass