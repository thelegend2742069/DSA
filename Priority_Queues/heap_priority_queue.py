#heap based priority queue
#heap implemented using an array

from priority_queue_base import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    #----------------------------------constructor-----------------------------------------
    def __init__(self):
        self._data = []

    #----------------------------------private methods-------------------------------------
    def _parent(self, index):
        '''Returns index of parent.'''
        parent_index = index-1 // 2
        return parent_index
    
    def _left(self, index):
        '''Returns index of left child.'''
        left_index = 2*index + 1
        return left_index
    
    def _right(self, index):
        '''Returns index of right child.'''
        right_index = 2*index + 2
        return right_index
    
    def _has_left(self, parent_index):
        '''Returns true if item has a left child.'''
        return len(self._data) > 2*parent_index + 1

    def _has_right(self, parent_index):
        '''Returns true if item has a right child.'''
        return len(self._data) > 2*parent_index + 2

    def _swap(self, first, second):
        '''Swaps items at given indices.'''
        self._data[first], self._data[second] = self._data[second], self._data[first]

    def _upheap(self, element_index):
        '''Bubbles item at given index up the tree.'''
        parent_index = self._parent(element_index)
        element = self._data[element_index]
        parent = self._data[parent_index]
        
        #if provided element is not root 
        #and has smaller key than parent
        #bubble it up the heap
        if element_index > 0 and element < parent:
            self._swap(element_index, parent_index)
            self._upheap(parent_index)                  #recurse
    
    def _downheap(self, element_index):
        '''Bubbles item at given index down the heap.'''
        if self._has_left(element_index):
            left = self._left(element_index)
            #smaller is left child
            smaller = left

            #smaller is right child if it exists
            #and has lesser key than left child
            if self._has_right(element_index):
                right = self._right(element_index)

                if self._data[right] < self._data[left]:
                    smaller = right
            
            #if key is more than children key
            #then downheap
            if self._data[smaller] < self._data[element_index]:
                self._swap(element_index, smaller)
                self._downheap(smaller)

    #----------------------------------public methods---------------------------------------
    def __len__(self):
        '''Return length of priority queue.'''
        return len(self._data)
    
    def is_empty(self):
        '''Returns true if queue is empty.'''
        return len(self._data) == 0
    
    def add(self, key, value):
        '''Adds key-value pair to priority queue.'''
        #add item to end of list and bubble it up
        self._data += self.Item(key, value)
        self._upheap(self._data[-1])
    
    def min(self):
        '''Returns item with minimum key.
        Arbitrary item selected if multiple elements with minimum key.
        
        Empty error if queue is empty.'''
        if self.is_empty():
            raise ValueError("queue is empty")

        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        '''Removes and returns item with minimum key.
        Arbitrary item selected if multiple elements with minimum key.

        Empty error if queue is empty.'''
        if self.is_empty():
            raise ValueError("queue is empty")
        
        #swap root and last item
        self._swap(0, len(self)-1)
        item = self._data.pop()

        #bubble down new root
        self._downheap(0)
        return (item._key, item._value)