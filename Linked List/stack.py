#stack implementation in python using singly linked list

class LinkedStack:
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
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    

    #---------------------------------user methods--------------------------------------
    def push(self, element):
        #set new element as head and link it to old head
        self._head = self._Node(element, self._head)
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        
        answer = self._head._element
        
        #set next element as head
        self._head = self._head._next
        self._size -= 1

        #return element in old head
        return answer
    
    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        #return element in head
        return self._head._element


class Empty(Exception):
    pass