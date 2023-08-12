#heap based priority queue
#heap implemented using an array

from priority_queue_base import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def _parent(self, index):
        parent_index = index-1 // 2
        return parent_index
    
    def _left(self, index):
        left_index = 2*index + 1
        return left_index
    
    def _right(self, index):
        right_index = 2*index + 2
        return right_index
    
    def _has_left(self, parent_index):
        return len(self._data) > 2*parent_index + 1

    def _has_right(self, parent_index):
        return len(self._data) > 2*parent_index + 2

    def _swap(self, first, second):
        self._data[first], self._data[second] = self._data[second], self._data[first]

    def _upheap(self, element_index):
        parent_index = self._parent(element_index)
        element = self._data[element_index]
        parent = self._data[parent_index]
        
        if element_index > 0 and element < parent:
            self._swap(element_index, parent_index)
            self._upheap(parent_index)
    
    def _downheap(self, element_index):
        if self._has_left(element_index):
            left = self._left(element_index)
            smaller = left

            if self._has_right(element_index):
                right = self._right(element_index)

                if self._data[right] < self._data[left]:
                    smaller = right
            
            if self._data[smaller] < self._data[element_index]:
                self._swap(element_index, smaller)
                self._downheap(smaller)