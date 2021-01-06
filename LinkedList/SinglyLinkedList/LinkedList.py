class Node:

    def __init__(self, data: int = None, next_node: "Node" = None):
        self.data = data
        self.next_node = next_node

    def set_data(self, data):
        self.data = data

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def has_next(self) -> bool:
        """
        returns true if node points to next node else false
        """
        return self.next_node is not None


class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def _set_length(self) -> None:
        self.length += 1

    def get_length(self) -> int:
        return self.length

    def traverse(self) -> str:
        """
        traverse entire linked list and append data in str,
        time complexity = O(n), for scanning the list of size n
        space complexity = O(1), for creating a temporary variable
        """
        data = ""
        current = self.head
        while current is not None:
            data += f"{current.get_data()} "
            current = current.get_next_node()
        return data

    def insert_at_beginning(self, data: int) -> None:
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node
        self._set_length()

    def insert_at_end(self, data: int) -> None:
        current = self.head
        new_node = Node(data)
        if current is not None:
            while current.next_node is not None:
                current = current.get_next_node()
            current.set_next_node(new_node)
        else:
            new_node.set_next_node(self.head)
            self.head = new_node
        self._set_length()

    def insert_after_position(self, data: int, position: int) -> None:
        if self.get_length() < position:
            return
        elif self.get_length() == 0:
            return self.insert_at_beginning(data)
        else:
            current = self.head
            new_node = Node(data)
            for _ in range(position-1):
                current = current.get_next_node()
            new_node.set_next_node(current.get_next_node())
            current.set_next_node(new_node)
            self._set_length()


ll = LinkedList()
ll.insert_after_position(101, 0)
ll.insert_at_end(24)
ll.insert_at_beginning(5)
ll.insert_at_beginning(4)
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_end(6)
ll.insert_at_end(7)
ll.insert_at_end(8)
ll.insert_after_position(100, 5)
ll.insert_at_end(8)
print(ll.traverse())
