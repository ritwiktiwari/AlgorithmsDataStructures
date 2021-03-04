"""
Delete middle element of stack using recursion,
where middle element is defined as (size/2)+1
O(1) space
"""

from Stack import Stack


def delete_middle(stack: Stack, k: int) -> Stack:
    if k == 1:
        stack.pop()
    else:
        temp = stack.pop()
        delete_middle(stack, k - 1)
        stack.push(temp)
    return stack


def delete(stack: Stack) -> Stack:
    if not stack.size() < 1:
        k = (stack.size() / 2) + 1
        return delete_middle(stack, k)


my_stack = Stack()
my_stack.push(5)
my_stack.push(0)
my_stack.push(1)
my_stack.push(2)
my_stack.push(9)
my_stack.push(3)
print(delete(my_stack))
