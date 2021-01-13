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
                print("Hash Method: Merge point is at =", id(head1))
                # print("Data =", head1.data)
                break
        if head2 is not None:
            if id(head2) not in address:
                address.add(id(head2))
                head2 = head2.next_node
            else:
                print("Hash Method: Merge point is at =", id(head2))
                # print("Data =", head2.data)
                break


def find_by_stack(head1, head2):
    """
    Time complexity O(m+n)
    :param head1:
    :param head2:
    :return:
    """
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
            print("Stack Method: Merge point is at =", temp)
            break


def find_by_search_and_sort(head1, head2):
    address = []
    while head1 is not None:
        address.append(id(head1))
        head1 = head1.next_node
    address = sorted(address)  # <- sort in log n time
    while head2 is not None:
        if id(head2) in address:  # <- search (binary search)
            print("Search and Sort: Merge point is at =", id(head2))
            break
        else:
            head2 = head2.next_node


def find_by_difference_of_node_counts(head1, head2):
    length1 = 0
    length2 = 0

    current1 = head1
    current2 = head2

    while head1 is not None:
        length1 += 1
        head1 = head1.next_node

    while head2 is not None:
        length2 += 1
        head2 = head2.next_node

    if length1 >= length2:
        difference = length1 - length2
        flag = 1
    else:
        difference = length2 - length1
        flag = 2

    for _ in range(difference):
        if flag == 1:
            current1 = current1.next_node
        else:
            current2 = current2.next_node

    while current1 is not None or current2 is not None:
        if id(current1) == id(current2):
            print("Difference Method: Merge point is at =", id(current1))
            break
        current1 = current1.next_node
        current2 = current2.next_node


find_by_hash(a1, a2)
find_by_stack(a1, a2)
find_by_search_and_sort(a1, a2)
find_by_difference_of_node_counts(a1, a2)
