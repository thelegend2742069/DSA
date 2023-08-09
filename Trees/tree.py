#tree abstract class
from ..Queues.queue import Queues

class Tree:
    #------------------------------Position Class------------------------------
    class Position:
        def element(self):
            #element stored at position
            raise NotImplementedError("Method must be implemented in SubClass")
        
        def __eq__(self, other):
            raise NotImplementedError("Method must be implemented in SubClass")

        def __ne__(self, other):
            return self == other
        
    
    #-----------------------------abstract methods------------------------------
    def root(self):
        #returns position of tree's root (None if empty)
        raise NotImplementedError("Method must be implemented in SubClass")
    
    def parent(self, p):
        #returns position of parent of p
        raise NotImplementedError("Method must be implemented in SubClass")
    
    def num_children(self, p):
        #returns number of children of p
        raise NotImplementedError("Method must be implemented in SubClass")
    
    def children(self, p):
        #generates iteration of position of p's children
        raise NotImplementedError("Method must be implemented in SubClass")
    
    def __len__(self):
        raise NotImplementedError("Method must be implemented in SubClass")
    

    #----------------------------concrete methods--------------------------------
    def is_empty(self):
        return len(self) == 0
    
    def is_root(self, p):
        #checks if p is root
        return p == self.root()
    
    def is_leaf(self, p):
        #checks if p is leaf
        return self.num_children(p) == 0
    
    def positions(self):
        #generate an iteration of all positions in the tree
        raise NotImplementedError("no traversal method selected to call")
    
    def __iter__(self):
        #generate an iteration of tree elements
        for p in self.positions():
            yield p.element()
    
    def depth(self, p):
        #returns depth of position
        if p.is_root():
            return 0
        return 1 + self.depth(self.parent(p))
    
    def height(self, p=None):
        #returns height of position (full tree if no position)
        if p is None:
            return self.height(self.root())
        
        if p.is_leaf():
            return 0
        
        return 1 + max(self.height_calc(c) for c in self.children(p))
        

    #----------------------------traversal methods-------------------------------
    
    def preorder_traverse(self):
        #iterate over positions in preorder traversal
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        #iterate over positions of a subtree rooted at p
        #in preorder traversal

        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder_traverse(self):
        #iterate over positions in postorder traversal
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    def _subtree_postorder(self, p):
        #iterate over positions of a subtree rooted at p
        #in postorder traversal
        
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p
    
    def breadth_first_traverse(self):
        #iterate over positions in preorder traversal

        #make a queue containing root node
        if not self.is_empty():
            node_queue = Queues()
            node_queue.enqueue(self.root())
        
        while not node_queue.is_empty():
            #yield last node in queue
            p = node_queue.dequeue()
            yield p

            #add children nodes in queue
            for c in self.children(p):
                node_queue.enqueue(c)