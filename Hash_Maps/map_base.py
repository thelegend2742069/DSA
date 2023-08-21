#base class for maps
from collections.abc import MutableMapping

class MapBase(MutableMapping):
    #------------------------------------Item Class------------------------------------
    class Item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value
        
        def __eq__(self, other):                #return true if keys equal
            return self._key == other._key
        
        def __ne__(self, other):                #return true if keys not equal
            return not (self == other)
        
        def __lt__(self, other):                #compare keys
            return self._key < other._key
        
        def __gt__(self, other):                #compare keys
            return self._key > other._key