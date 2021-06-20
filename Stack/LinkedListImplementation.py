class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def is_empty(self):
        if self.stack.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.stack.head
        self.stack.head = node

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is already empty")
        else:
            temp = self.stack.head.value
            self.stack.head = self.stack.head.next
            return temp

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            return self.stack.head.value

    def delete(self):
        self.stack.head = None

    def __str__(self):
        values = [str(x.value) for x in self.stack]
        return ' '.join(values)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print("------")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("------")
stack.push(1)
print(stack.peek())
