#bottom up heap implemetation
#useful when you have an unsorted list
#to be made in a heap

#normally adding items will be O(nlog(n))
#but with bottom up heap it is O(n)

from heap_priority_queue import HeapPriorityQueue

class BottomUpHeap(HeapPriorityQueue):
    #----------------------------constructor-------------------------------
    def __init__(self, contents = ()):
        self._data = [(key, value) for (key, value) in contents]

        #sort heap if multiple elements
        if len(self._data)>1:
            self._heapify()
    #------------------------------method----------------------------------
    def _heapify(self):
        #no sorting required for leaf items
        #downheap all elements one level above leaf
        parent_index = len(self._data) - 1
        for index in range(parent_index, -1, -1):
            self._downheap(index)