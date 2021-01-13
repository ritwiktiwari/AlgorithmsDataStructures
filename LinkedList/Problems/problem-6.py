# Reverse a linked list
from LinkedList import LinkedList


class Solution(LinkedList):

    def reverse_iterative(self):
        current_pointer = self.head
        if current_pointer is None:
            return
        if current_pointer.next_node is None:
            return
        previous_pointer = None
        next_pointer = current_pointer.next_node
        while next_pointer is not None:
            current_pointer.next_node = previous_pointer
            previous_pointer = current_pointer
            current_pointer = next_pointer
            next_pointer = next_pointer.next_node

        current_pointer.next_node = previous_pointer
        self.head = current_pointer

    # def reverse_recursive(self, current):
    #     if current is None or current.next_node is None:
    #         return current
    #     else:
    #         node1 = self.reverse_recursive(current.next_node)
    #         current.next_node.next_node = current
    #         current.next = None
    #     return node1
    #
    # def reverse_ll(self):
    #     return self.reverse_recursive(self.head)


ll = Solution()
ll.append(5)
ll.append(4)
ll.append(3)
ll.append(2)
ll.append(1)
print(ll.show())

ll.reverse_iterative()
print(ll.show())

# print(ll.reverse_ll())
# print(ll.show())