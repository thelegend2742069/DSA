#queue implementation in python

class Queues:
    #set default queue size
    DEFAULT_CAP = 8

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAP
        self._size = int(0)
        self._front = int(0)

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        #raise error if queue empty
        if self.is_empty():
            raise Empty("Queue is empty")
        
        return self._data[self._front]
    
    def enqueue(self, e):
        #double queue size if queue is full
        if self._size == len(self._data):
            self.resize(2*self._size)
        
        #add element to queue
        index = (self._front+self._size) % len(self._data)
        self._data[index] = e
        self._size  += 1
    
    def dequeue(self):
        #raise error if queue empty
        if self.is_empty():
            raise Empty("Queue is empty")
        
        #remove element from queue and update front and size
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size  -= 1

        if len(self._data) <= self.DEFAULT_CAP:
            return answer
        
        #halve queue size if elements less than 1/4 of queue
        if 4*self._size == len(self._data):
            self.resize(len(self._data)//2)
        
        return answer
    
    def resize(self, n):
        walk = self._front
        new = [None] * n
        
        #assign values to new list and update list and front
        for i in range(self._size):
            new[i] = self._data[walk]
            walk = (walk+1)%len(self._data)
        
        self._data = new
        self._front = 0


class Empty(Exception):
    pass