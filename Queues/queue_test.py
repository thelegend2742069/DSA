from queue import Queues

q = Queues()

print(q._data)
q.enqueue(5)
print(q._data)
q.enqueue(3)
print(q._data)
print(q._size)

print(q.dequeue(), q._data)
print(q.is_empty())
print(q.dequeue(), q._data)
print(q.is_empty())

q.enqueue(7)
print(q._data)
q.enqueue(9)
print(q._data)
print(q.first())
q.enqueue(4)
print(q._data)
print(q._size)
print(q.dequeue(), q._data)


resizeTest = Queues()

for i in range(100):
    resizeTest.enqueue(i)
    print(i, len(resizeTest))

print("increment finished")

for i in range(95):
    resizeTest.dequeue()
    print(95-i, len(resizeTest))
