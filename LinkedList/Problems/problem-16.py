from LinkedList import LinkedList


class Solution(LinkedList):
    """
    Sum of linked list via recursion
    """

    def sum(self):
        current = self.head

        def inner(head):
            if head is None:
                return 0
            else:
                return head.data + inner(head.next_node)

        return inner(current)


ll = Solution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(9)

print(ll.sum())
