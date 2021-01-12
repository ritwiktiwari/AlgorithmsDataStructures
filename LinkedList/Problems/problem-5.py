# Add a node in a sorted linked list

from LinkedList import Node, LinkedList


class Solution(LinkedList):

    def ordered_insertion(self, data):
        current = self.head
        previous = None
        new_node = Node(data)
        while current and current.data < data:
            previous = current
            current = current.next_node

        new_node.next_node = previous.next_node
        previous.next_node = new_node


ll = Solution()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(5)
ll.append(6)
print(ll.show())
ll.ordered_insertion(7)
print(ll.show())
ll.ordered_insertion(3)
print(ll.show())
