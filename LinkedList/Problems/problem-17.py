from LinkedList import LinkedList


class Solution(LinkedList):
    """
    Given a list L1 = {A1,A2,...An} reorder it to
    {A1, An, A2, An-1...} without using any extra space
    """

    def _split(self):
        fast = slow = mid = self.head
        while fast and fast.next_node:
            slow = mid
            mid = mid.next_node
            fast = fast.next_node.next_node
        slow.next_node = None
        return slow, mid

    @staticmethod
    def _reverse(head):
        current_pointer = head
        if not current_pointer:
            return
        prev_pointer = None
        next_pointer = current_pointer.next_node

        while next_pointer:
            current_pointer.next_node = prev_pointer
            prev_pointer = current_pointer
            current_pointer = next_pointer
            next_pointer = next_pointer.next_node
        current_pointer.next_node = prev_pointer
        return current_pointer

    @staticmethod
    def _merge(list1, list2):
        while list2:
            temp_list2_next = list2.next_node
            temp_list1_next = list1.next_node
            list2.next_node = list1.next_node
            list1.next_node = list2
            list2 = temp_list2_next
            list1 = temp_list1_next

    def reorder(self):
        """
        Split
        Reverse
        Merge
        """
        current = self.head
        mid, list2 = self._split()
        list2 = self._reverse(list2)
        self._merge(current, list2)


ll = Solution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

ll.reorder()
print(ll.show())
