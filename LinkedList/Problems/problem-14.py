"""
Implementing fractional node
find n/k th node from
"""

from LinkedList import LinkedList


class Solution(LinkedList):

    def fractional_node(self, k):
        """
        n/k th node
        """
        current = self.head
        fractional_node = self.head
        i = 1
        while current:
            if i % k == 0:
                fractional_node = fractional_node.next_node
            i += 1
            current = current.next_node
        print(fractional_node.data)


ll = Solution()
ll2 = Solution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

ll.fractional_node(k=3)

ll2.append(2)
ll2.append(7)
ll2.append(9)
ll2.append(5)
ll2.append(3)

ll2.fractional_node(3)