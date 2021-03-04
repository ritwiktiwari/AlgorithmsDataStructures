"""
Reverse a stack using recursion
O(1) space
"""

from Stack import Stack


def insert(stack: Stack, value: int):
    if stack.size() < 1:
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)
    return stack


def reverse(stack: Stack):
    if not stack.size() < 1:
        temp = stack.pop()
        reverse(stack)
        insert(stack, temp)
    return stack


my_stack = Stack()
my_stack.push(5)
my_stack.push(0)
my_stack.push(1)
my_stack.push(2)
my_stack.push(9)
my_stack.push(3)
print(my_stack)
print(reverse(my_stack))
