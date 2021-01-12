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

head = a

tortoise = hare = head

while hare is not None:
    tortoise = tortoise.next_node
    hare = hare.next_node.next_node
    if hare is tortoise:
        print(f"Cycle found at {hare.data}")
        break


