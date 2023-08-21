#hash map base class implementation
#bucket msut be implemented in the child class
from map_base import MapBase
from random import randrange

class HashMapBase(MapBase):
    #------------------------------------------constructor------------------------------------------
    def __init__(self, cap = 11, p = 109345121):
        self._table = [None] * cap                      #initialise table
        self._n = 0                                     #number of elements in table
        self._prime = p                                 
        self._scale = 1 + randrange(self._prime-1)
        self._shift = randrange(self._prime)

    #--------------------------------------------methods--------------------------------------------
    def hash_function(self, key):
        '''Return hash of the given key.'''
        return (hash(key)*self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self):
        '''Return number of items in the map.'''
        return self._n
    
    def __getitem__(self, key):
        '''Returns value associated with key.
        May raise KeyError.'''
        hash = self.hash_function(key)
        return self.bucket_getitem(hash, key)            #may raise key error
    
    def __setitem__(self, key, value):
        '''Sets value to key. Overwrites value if it exists already.'''
        hash = self.hash_function(key)
        self.bucket_setitem(hash, key, value)
        
        if self._n > len(self._table)//2:                #resize to keep load < 0.5
            self._resize(2*len(self._table) - 1)         #2^x -1 is often prime, better for modulus

    def __delitem__(self, key):
        ''''Removes value associated with key.
        May raise KeyError.'''
        hash = self.hash_function(key)
        self.bucket_delitem(hash, key)                    #may raise key error
        self._n -= 1

    def _resize(self, cap):
        '''Resizes table to length cap.'''
        old = list(self.items)
        self._table = [None] * cap
        self._n = 0                             #set number to 0, recalculated during additions
        for (key, value) in old:                #add key-value pairs to resized table
            self[key] = value