from deque import LinkedDeque

d = LinkedDeque()

d.add_last(5)
d.add_first(3)
d.add_first(7)
print(d.first())
print(d.delete_last())
print(len(d))
print(d.delete_last())
print(d.delete_last())
d.add_first(6)
print(d.last())
d.add_first(8)
print(d.is_empty())
print(d.last())