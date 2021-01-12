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


def tortoise_hare(head):
    """
    Also known as Floyd Cycle Finding Algorithm
    :param head:
    :return:
    """
    tortoise = hare = head
    while hare is not None:
        tortoise = tortoise.next_node
        hare = hare.next_node.next_node
        if hare is tortoise:
            print(f"Cycle found at {tortoise.data}")
            break


def hash_table(head):
    my_address_hash = set()
    current = head
    while current is not None:
        if id(current) not in my_address_hash:
            my_address_hash.add(id(current))
            current = current.next_node
        else:
            print(f"Cycle found at {current.data}")
            break


tortoise_hare(a)
hash_table(a)
