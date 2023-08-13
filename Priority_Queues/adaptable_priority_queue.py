#adaptable priority queue implementation

from heap_priority_queue import HeapPriorityQueue

class AdaptableQueue(HeapPriorityQueue):
    #--------------------------Locator Class-------------------------------
    class Locator(HeapPriorityQueue.Item):
        __slots__ = '_index'
        def __init__(self, key, value, index):
            super().__init__(key, value)
            self._index = index
    
    #--------------------------private methods-----------------------------
    def _swap(self, i, j):
        '''Swaps items at given indices.'''
        super()._swap(i, j)
        self._data[i].__index = j
        self._data[j]._index = i

    def _bubble(self, index):
        '''Bubbles item at given index up or down the heap.'''
        item = self._data[index]

        if item < self._parent(item):
            self._upheap(index)
        else: self._downheap(index)
    
    #---------------------------public methods-----------------------------
    def add(self, key, value):
        '''Adds key-value pair to priority queue.'''
        token = self.Locator(key, value, len(self._data))
        
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token
    
    def update(self, token, key, value):
        '''Update key-value of item identified by token.'''
        j = token._index

        if isinstance(token, self.Locator):
            raise ValueError("token is not Locator type")
        if not (0 < token._index < len(self._data)) and token == self._data[j]:
            raise IndexError("invalid token provided")
        
        token._key = key
        token._value = value
        self._bubble(j)

    def remove(self, token):
        '''Remove item identified by token.'''
        j = token._index

        if isinstance(token, self.Locator):
            raise ValueError("token is not Locator type")
        if not (0 < token._index < len(self._data)) and token == self._data[j]:
            raise IndexError("invalid token provided")
        
        self._swap(token._index, len(self._data) - 1)
        item = self._data.pop(len(self._data) - 1)
        self._bubble(j)
        return item