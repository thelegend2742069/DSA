#queue implementation in python

class Queues:

    def __init__(self):
        self._data = [None]*8
        self._size = int(0)
        self._front = int(0)

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        
        return self._data[self._front]
    
    def enqueue(self, e):
        if self._size == self.__len__():
            self.resize(2*self._size)
        
        index = (self._front+self._size)%self.__len__()
        self._data[index] = e
        self._size  += 1
    
    def dequeue(self):

        if self.is_empty():
            raise Empty("Queue is empty")
        
        answer = self._data[self._front]

        self._data[self._front] = None
        self._front = (self._front+1)%self.__len__()
        self._size  -= 1

        if self.__len__()<=8:
            return answer
        
        if 4*self._size == self.__len__():
            self.resize(self.__len__()//2)
        
        return answer
    
    def resize(self, n):
        walk = self._front
        
        new = [None]*n
        
        for i in range(self._size):
            new[i] = self._data[walk]
            walk = (walk+1)%self.__len__()
        
        self._data = new
        self._front = 0
        print(self._data)



class Empty(Exception):
    pass