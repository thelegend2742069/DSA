#hash map implementation using chaining
#to overcome hashing collisions

from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
    def bucket_getitem(self, hash, key):
        '''Returns value associated to key.
        May raise KeyError'''
        bucket = self._table[hash]
        if bucket == None:                                      #raise error if bucket empty
            raise KeyError('Invalid Key: ' + repr(key))
        return bucket[key]

    def bucket_setitem(self, hash, key, value):
        '''Adds key-value pair to table.
        Updates value associated with key if it exists already.'''
        bucket = self._table[hash]
        if bucket == None:                                      #initialise bucket if empty
            bucket = UnsortedTableMap()
        
        old_size = len(bucket)
        bucket[key] = value
        if old_size < len(bucket):                              #increase size if new key
            self._n += 1

    def bucket_delitem(self, hash, key):
        '''Deletes key-value pair from table.
        May Raise KeyError.'''
        bucket = self._table[hash]
        if bucket == None:                                      #raise error if bucket empty
            raise KeyError("Invalid Key: " + repr(key))
        del bucket[key]
    
    def __iter__(self):
        '''Yields keys from the map.'''
        #for each bucket in table
        #if bucket is not empty
        #return all keys in bucket
        for bucket in self._table:
            if bucket:
                for key in bucket:
                    yield key