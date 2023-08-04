#binary tree based on linked lists implemented in python

from binary_tree import BinaryTree
class LinkedBinary(BinaryTree):
    #------------------------------Node Class-------------------------------
    class Node:
        def __init__(self, element, parent, left, right):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    #-----------------------------Position Class-----------------------------
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            return not self == other
        
    #----------------------------utility methods------------------------------    
    def element(self):
        return self._node._element

    def _validate(self, p):
        if not isinstance(p, self.Position):                                    #check if p is a position
            raise TypeError("this is not a position")
        
        if p._container is not self:                                            #check if position belongs to this tree
            raise ValueError("position does not belong to this tree")
        
        if p._node.parent == p._node:                                           #check if node is depreciated
            raise ValueError("node has been depreciated")                       #depreciated nodes are their own parents

        return p._node
    
    def make_position(self, node):
        if node is None:
            return None
        
        return self.Position(self, node)

    #---------------------------Binary Tree Constructor-----------------------
    def __init__(self):
        self._root = None
        self._size = 0
    
    #------------------------------accessor methods---------------------------
    def __len__(self):
        return self._size
    
    def root(self):
        return self._root
    
    def parent(self, p):
        node = self._validate(p)
        return self.make_position(node._parent)
    
    def left(self, p):
        node = self._validate(p)
        return self.make_position(node._left)
    
    def right(self, p):
        node = self._validate(p)
        return self.make_position(node._right)
    
    def num_children(self, p):
        node = self._validate(p)
        num = 0
        if node._left is not None:
            num += 1
        if node._right is not None:
            num += 1
        return num
    
    
    def add_root(self, element):
        if self._root is not None:
            raise ValueError("root already exists")
        node = self.Node(element)
        self._root = node
        self._size += 1
        return self.make_position(node)
    
    def add_left(self, element, position):

        parent = self._validate(position)
        if parent._left is not None:
            raise ValueError("left child already exists")
        
        left = self.Node(element, parent)
        parent._left = left
        self._size += 1
        return self.make_position(left)
    
    def add_right(self, element, position):

        parent = self._validate(position)
        if parent._right is not None:
            raise ValueError("right child already exists")
        
        right = self.Node(element, parent)
        parent._right = right
        self._size += 1
        return self.make_position(right)
    
    def replace(self, position, element):
        node = self._validate(position)
        old = node._element
        node._element = element
        return old
    
    def delete(self, position):
        node = self._validate(position)
        if self.num_children(position):
            raise ValueError("cannot delete node: has two children")
        
        child = node._left if node._left else node._right

        if self.is_root(node):
            self._root = child
        else:
            parent = node._parent
            if parent._left is node:
                parent._left = child
            else:
                parent._right = child
        
        node._parent = node
        self._size -= 1

        return node._element
    
    def attach(self, position, tree1, tree2):
        leaf = self._validate(position)
        
        if not self.is_leaf(position):
            raise ValueError("node already has children")

        if type(self) is not type(tree1) or type(self) is not type(tree2):
            raise TypeError("trees are not of same type")
        
        if not tree1.is_empty():
            tree1._root._parent = leaf
            leaf._left = tree1._root
            tree1._root = None
            tree1._size = 0
        
        if not tree2.is_empty():
            tree2._root._parent = leaf
            leaf._left = tree2._root
            tree2._root = None
            tree2._size = 0
            
        self._size += len(tree1) + len(tree2)

        