# Find nth node from the end of the linked list
from LinkedList import LinkedList


class Solution(LinkedList):

    def mth_node_from_last(self, m):
        current = temp = self.head
        n = 0
        while current is not None:
            current = current.next_node
            n += 1
        print(f"mth node from last is (n-m+1)th node from front")
        print(f"(n-m+1)th = {n-m+1}th node from front")
        for i in range(n-m):
            temp = temp.next_node
        print(temp, temp.data)


ll = Solution()
ll.prepend(1)
ll.prepend(2)
ll.prepend(3)
ll.prepend(4)
ll.prepend(5)
ll.prepend(6)
ll.prepend(7)
ll.prepend(8)
print(ll.show())
ll.mth_node_from_last(5)
ll.mth_node_from_last(1)
ll.mth_node_from_last(2)

