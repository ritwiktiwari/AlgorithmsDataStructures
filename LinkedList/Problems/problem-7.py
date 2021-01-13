# Find the merge point of two linked lists

from LinkedList import Node

h = Node(8)
g = Node(7, h)
f = Node(6, g)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)

b1 = Node(21, a)
a1 = Node(11, b1)

c2 = Node(32, a)
b2 = Node(22, c2)
a2 = Node(12, b2)


def find_by_hash(head1, head2):
    """
    Time complexity O(max(m,n))
    :param head1:
    :param head2:
    :return:
    """
    address = set()
    while head1 is not None or head2 is not None:
        if head1 is not None:
            if id(head1) not in address:
                address.add(id(head1))
                head1 = head1.next_node
            else:
                print("Merge point is at =", id(head1))
                print("Data =", head1.data)
                break
        if head2 is not None:
            if id(head2) not in address:
                address.add(id(head2))
                head2 = head2.next_node
            else:
                print("Merge point is at =", id(head2))
                print("Data =", head2.data)
                break


def find_by_stack(head1, head2):
    temp = None

    stack1 = []
    stack2 = []

    while head1 is not None:
        stack1.append(id(head1))
        head1 = head1.next_node

    while head2 is not None:
        stack2.append(id(head2))
        head2 = head2.next_node

    while len(stack1) != 0 or len(stack2) != 0:
        if stack1[-1] == stack2[-1]:
            temp = stack1.pop()
            stack2.pop()
        else:
            print("Merge point is at =", temp)
            break


find_by_hash(a1, a2)
find_by_stack(a1, a2)
