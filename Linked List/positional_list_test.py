from positional_list import PositionalList

fruits = PositionalList()

b = fruits.add_last("banana")
m = fruits.add_first("mango")
fruits.add_first("coconut")
print(fruits.first().element())
print(len(fruits))
print(fruits.delete(m))
c = fruits.add_first("cherry")
print(fruits.before(b).element())
print(fruits.last().element())
fruits.add_last("apple")
print(fruits.is_empty())
print(fruits.after(c).element())
print(fruits.last().element())