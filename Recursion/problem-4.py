"""
Sort a stack using recursion
"""

from Stack import Stack


def insert(stack: Stack, value: int) -> Stack:
    if stack.elements < 1 or stack.top() < value:
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)
    return stack


def sort(stack: Stack) -> Stack:
    if stack.elements < 1:
        pass
    else:
        temp = stack.pop()
        sort(stack)
        insert(stack, temp)
    return stack


my_stack = Stack()
my_stack.push(5)
my_stack.push(0)
my_stack.push(1)
my_stack.push(2)
my_stack.push(9)
my_stack.push(3)
print(sort(my_stack))
