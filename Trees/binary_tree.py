#binary tree abstract class
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
    
    def positions(self):
        #generate an iteration of positions in the tree
        return self.inorder_traverse()


    #----------------------------traversal method--------------------------------
    def inorder_traverse(self):
        #generate an iteration of all postitions in a tree
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        #generate an iteration of positions in subtree rooted at p

        if self.left(p) is not None:
            #inorder traverse left child of p
            for other in self._subtree_inorder(self.left(p)):
                yield other

        yield p

        if self.right(p) is not None:
            #inorder traverse right child of p
            for other in self._subtree_inorder(self.right(p)):
                yield other