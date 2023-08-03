#stack implementation in python using singly linked list

from singly_linked_list import SinglyLinkedList

class LinkedStack(SinglyLinkedList):
    #adds element to top of stack
    def push(self, element):
        self.add_node(element)
        self._size += 1

    #removes element from top of stack and returns it
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")       #raises error if stack is empty
        
        answer = self.delete_node(self._head)
        self._size -= 1

        return answer
    
    #returns element at top of stack
    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")       #raises error if stack is empty

        return self._head._element


class Empty(Exception):
    pass