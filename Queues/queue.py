#queue implementation in python

class Queues:

    def __init__(self):
        self._data = [None]*8
        self._size = int(0)
        self._front = int(0)

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def first(self):
        if self.is_empty():
            return Empty("Queue is empty")
        
        return self._data[self._front]
    
    def enqueue(self, e):
        if self._size == self.__len__():
            self.resize(2*self._size)
        
        self._data[(self._front+self._size)%self.__len__()] = e
        self._size  += 1
    
    def dequeue(self):
        if 4*self._size == self.__len__():
            self.resize(self._size/2)
        
        answer = self._data[self._front]

        self._data[self._front] = None
        self._front = (self._front+1)%self._size
        self._size  -= 1
        
        return answer
    
    def resize(self, n):
        walk = self._front
        new = [None]*int(n)
        
        for i in range(self._size):
            new[i] = self._data[walk]
            walk = (walk+1)%len(self._data)
        
        self._data = new
        self._front = 0




class Empty(Exception):
    pass