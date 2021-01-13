# Reverse linked list in pairs,
# LL1 = 1 2 3 4 5
# Reversed = 2 1 4 3 5

from LinkedList import LinkedList

class Solution(LinkedList):

    def reverse(self):
        current = self.head

        while current is not None and current.next_node is not None:
            current.data, current.next_node.data = current.next_node.data, \
            current.data
            current = current.next_node.next_node


ll = Solution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print(ll.show())

ll.reverse()
print(ll.show())
