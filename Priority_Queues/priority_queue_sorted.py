#sorted priority queue implementation in python
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
        return self._data.first()
    
    def min(self):
        #returns item with min key
        #if multiple items with min key,
        #an arbitrary item will be returned
        if self.is_empty():
            raise Empty("queue is empty")
        
        p = self._data.first()
        item = p.element()
        
        return (item._key, item._value)


    def remove_min(self):
        #deletes and returns item with min key
        #if multiple items with min key,
        #an arbitrary item will be returned
        if self.is_empty():
            raise Empty("queue is empty")
        
        p = self._data.first()
        item = self._data.delete(p)

        return (item._key, item._value)
    
    def add(self, key, value):
        #adds key-value pair to queue
        item = self.Item(key, value)
        walk = self._data.last()

        while walk is not None and item < walk.element():
            walk = self._data.before(walk)
        
        if walk is None:
            self._data.add_first(item)
        else:
            self._data.add_after(walk, item)