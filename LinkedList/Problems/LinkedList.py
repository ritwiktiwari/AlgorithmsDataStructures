
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = new_node

    def show(self):
        data = ""
        current = self.head
        while current:
            data += f"{current.data} "
            current = current.next_node
        return data

