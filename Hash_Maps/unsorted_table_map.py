from typing import Iterator
from map_base import MapBase

class UnsortedTableMap(MapBase):
    #------------------------constructor------------------------------
    def __init__(self):
        self._table = []
    
    def __getitem__(self, key):
        for item in self._table:
            if key == item._key:
                return item._value
        
        raise KeyError('Invalid Key: ' + repr(key))
    
    def __setitem__(self, key, value):
        for item in len(self._table):
            if key == item._key:
                item._value = value
                return
        
        self._table.append(self.Item(key, value))

    def __delitem__(self, key):
        for i in self._table:
            if key == self._table[i]:
                self._table.pop(i)
                return
        
        raise KeyError('Invalid Key: ' + repr(key))

    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield item._key