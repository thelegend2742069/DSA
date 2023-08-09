#positional list implementaion in python

from doubly_linked_list import DoublyLinkedList

class PositionalList(DoublyLinkedList):
    #-------------------------------------Position Class----------------------------------------
    class Position:
        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node
        
        def __ne__(self, other):
            return not (self == other)
    
    #-------------------------------------utility methods-----------------------------------------
    def _validate(self, p):
        #check if p is a valid position                             #raise error if:
        if not isinstance(p, self.Position):                            #p is not a position
            raise TypeError("p is not Position type")
        
        if p._container is not self:                                    #p belongs to some other list
            raise ValueError("p doest not belong to this list")
        
        if p._node._next is None:                                       #p has been depreciated
            raise ValueError("p is depreciated")
        
        return p._node
    
    def _make_position(self, node):
        #return a position for node
        if node is self._header or node is self._trailer:
            return None
        
        return self.Position(self, node)
    
    #-------------------------------------accessor methods-----------------------------------------
    def first(self):
        #return first element of list
        return self._make_position(self._header._next)
    
    def last(self):
        #return last element of list
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        #return position of node before p
        if self.is_empty():
            return Empty("list is empty")
        
        return self._make_position(p._node._prev)
    
    def after(self, p):
        #return position of node after p
        if self.is_empty():
            return Empty("list is empty")
        
        return self._make_position(p._node._next)
    
    def __iter__(self):
        #iterate over elements of list
        cursor = self.first()

        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
        
    #-------------------------------------mutator methods-----------------------------------------
    def add_first(self, element):
        #add element to start of list and return its position
        new = self.add_node(element, self._header, self._header._next)
        return self._make_position(new)
    
    def add_last(self, element):
        #add element to end of list and return its position
        new = self.add_node(element, self._trailer._prev, self._trailer)
        return self._make_position(new)

    def add_before(self, p, element):
        #add element before p and return its position
        original = self._validate(p)
        new = self.add_node(element, original._prev, original)
        return self._make_position(new)
    
    def add_after(self, p, element):
        #add element after p and return its position
        original = self._validate(p)
        new = self.add_node(element, original, original._next)
        return self._make_position(new)
    
    def replace(self, p, element):
        #replace value at p with new value(element)
        node = self._validate(p)
        node._element = element
        return p
    
    def delete(self, p):
        #delete node at p
        node = self._validate(p)
        return self.delete_node(node, node._prev, node._next)
        


class Empty(Exception):
    pass