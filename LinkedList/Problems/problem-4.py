# Find Loop in the Linked List

from LinkedList import Node

# Creating Circular Linked List

h = Node(8)
g = Node(7, h)
f = Node(6, g)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)
h.next_node = c


def find_loop(head):
    my_address_hash = set()
    current = head
    while current is not None:
        if id(current) not in my_address_hash:
            my_address_hash.add(id(current))
            current = current.next_node
        else:
            return current
    return False


def find_length(head):
    current = find_loop(head)
    temp = current
    count = 0
    if current:
        while temp.next_node is not current:
            temp = temp.next_node
            count += 1
        return count
    return 0


print(find_length(a))
