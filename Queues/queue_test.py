from queue import Queues
'''
q = Queues()

q.enqueue(5)
q.enqueue(3)
print(q.__len__())
print(q.dequeue())
print(q.is_empty())
print(q.dequeue())
print(q.is_empty())

q.enqueue(6)
q.enqueue(9)
print(q.first())
q.enqueue(4)
print(q.__len__())
print(q.dequeue())
'''
resizeTest = Queues()

for i in range(100):
    resizeTest.enqueue(0)
    print(len(resizeTest), i)

print("increment finished")

for i in range(100):
    resizeTest.dequeue()
    print(len(resizeTest), 100-i)