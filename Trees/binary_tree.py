#binary tree abstract class
#most of the code is same as tree.py
from tree import Tree

class BinaryTree(Tree):    
    #-----------------------------abstract methods------------------------------
    def left(self, p):
        #return left child of p (None if no left chlid)
        raise NotImplementedError("Method must be implemented in SubClass")
    
    def right(self, p):
        #return right child of p (None if no right chlid)
        raise NotImplementedError("Method must be implemented in SubClass")


    #----------------------------concrete methods--------------------------------
    def sibling(self, p):
        #returns sibling of p
        parent = self.parent()

        if self.is_root(parent):    #no sibling if root
            return None

        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        #generates iteration of position of p's children
        if self.left(p) is not None:
            yield self.left(p)
        
        if self.right(self, p) is not None:
            yield self.right(p)