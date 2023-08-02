from stack import LinkedStack

number = LinkedStack()

number.push(5)
number.push(3)
number.push(6)
number.push(1)
print(number.top())

print("len =", len(number))

print(number.pop())
print("len =", len(number))
print(number.pop())
print(number.pop())
print(number.pop())

number.pop()    #should raise stack is empty error