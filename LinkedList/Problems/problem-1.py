# Implement Stack Using Linked List

class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.head is not None:
            temp_node = self.head
            data = temp_node.data
            self.head = temp_node.next_node
            del temp_node
            self.size -= 1
            return data
        return None

    def show(self):
        data = ""
        current = self.head
        while current:
            data += f"{current.data} "
            current = current.next_node
        return data


stack = Stack()
stack.insert(5)
stack.insert(4)
stack.insert(3)
stack.insert(2)
stack.insert(1)
print(stack.pop())
print(stack.size)
print(stack.show())
