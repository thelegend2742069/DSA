#unsorted priority queue implementation in python
from priority_queue_base import PriorityQueueBase
from ..Linked_List.positional_list import PositionalList, Empty

class PriorityQueueUnsorted(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def _find_min(self):
        #returns position of item with min key
        #if multiple items with min key,
        #an arbitrary item will be returned

        min = self._data.first()
        walk = self._data.after(min)

        while walk is not None:
            if walk.element() < min.element():
                min = walk
            walk = self._data.after(walk)
        
        return min
    
    def min(self):
        #returns item with min key
        #if multiple items with min key,
        #an arbitrary item will be returned
        
        p = self._find_min()
        item = p.element()

        return (item._key, item._value)


    def remove_min(self):
        #deletes and returns item with min key
        #if multiple items with min key,
        #an arbitrary item will be returned
        if self.is_empty():
            raise Empty("queue is empty")
        
        p = self._find_min()
        item = self._data.delete(p)

        return (item._key, item._value)
    
    def add(self, key, value):
        #adds key-value pair to queue
        self._data.add_last(self.Item(key, value))