# Break a circular linked list in to two equal parts

from LinkedList import Node

h = Node(8)
g = Node(7, h)
f = Node(6, g)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)
h.next_node = a

def break_in_two(head):
    previous = head
    slow = head
    fast = head

    while True:
        previous = slow
        slow = slow.next_node
        fast = fast.next_node.next_node
        if fast is head:
            break
    previous.next_node = None
    head2 = slow
    return (head, head2)


break_in_two(a)
