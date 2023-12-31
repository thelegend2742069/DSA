#stack implementation in python

class Stack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        #raise error if stack empty
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    
    def pop(self):
        #raise error if stack empty
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
    
class Empty(Exception):
    pass