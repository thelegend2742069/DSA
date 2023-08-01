#doubly ended queue implementation in python

class Deque:

    #set default capacity to 8
    DEFAULT_CAP = 8

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAP
        self._front = 0
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def first(self):
        return self._data[self._front]
    
    def last(self):
        index = (self._front + self._size) % len(self._data)
        return self._data[index]
    
    def add_first(self, e):
        #set index
        index = (self._front-1) % len(self._data)
        
        #update queue, front and size
        self._data[index] = e
        self._front = (self._front-1) % len(self._data)
        self._size += 1

        if self._size == len(self._data):
            self.resize(2*len(self._data))

    def add_last(self, e):
        #set index
        index = (self._front + self._size + 1) % len(self._data)
        
        #update queue and size
        self._data[index] = e
        self._size += 1

        
        if self._size == len(self._data):
            self.resize(2*len(self._data))
    
    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        #set index
        index = self._front

        #update queue, front and size
        answer = self._data[index]
        self._data[index] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1

        if self._size <= self.DEFAULT_CAP:
            return answer
        
        if 4*self._size <= len(self._data):
            self.resize(len(self._data)//2)
            return answer
        
    def delete_last(self):        
        if self.is_empty():
            raise Empty("Queue is empty")

        #set index
        index = (self._front + self._size) % len(self._data)

        #update queue and size
        answer = self._data[index]
        self._data[index] = None
        self._size -= 1

        if len(self._data) <= self.DEFAULT_CAP:
            return answer
        
        if 4*self._size <= len(self._data):
            self.resize(len(self._data)//2)
            return answer


    def resize(self, n):
        #set walk and create new queue
        walk = self._front
        new = [None] * n

        #assign old values to new queue
        for i in range(self._size):
            new[i] = self._data[walk]
            walk = (walk+1) % len(self._data)
        
        #assign new queue to self and reset front
        self._data = new
        self._front = 0
    

    
class Empty(Exception):
    pass