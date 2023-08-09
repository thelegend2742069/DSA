#tree abstract class

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
        #return a list of positions in the tree elements
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