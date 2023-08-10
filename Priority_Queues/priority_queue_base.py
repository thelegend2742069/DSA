#priority queue base class

class PriorityQueueBase():
    class Item():
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value
        
        def __lt__(self, other):
            #comapres keys of 2 elements
            return self._key < other._key
        
        def __gt__(self, other):
            #compares keys of 2 elements
            return self._key > other._key
        
    def is_empty(self):
        return len(self) == 0
    