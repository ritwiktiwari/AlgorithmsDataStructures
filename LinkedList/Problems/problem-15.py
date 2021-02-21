from LinkedList import LinkedList


class Solution(LinkedList):
    """
    Merge two sorted linked list and return them via a array
    """

    def merge_and_sort(self, linked_list2):
        current1 = self.head
        current2 = linked_list2.head
        list1 = []
        current1_flag = True
        current2_flag = True
        while True:
            if current1 and current1.data < current2.data:
                list1.append(current1.data)
                current1 = current1.next_node
                if not current1:
                    current1_flag = False
                    break
            else:
                list1.append(current2.data)
                current2 = current2.next_node
                if not current2:
                    current2_flag = False
                    break

        while current1_flag:
            list1.append(current1.data)
            if current1.next_node is not None:
                current1 = current1.next_node
            else:
                current2_flag = False

        while current2_flag:
            list1.append(current2.data)
            if current2.next_node is not None:
                current2 = current2.next_node
            else:
                current2_flag = False
        return list1


ll = Solution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

ll2 = Solution()
ll2.append(-6)
ll2.append(-5)
ll2.append(-4)
ll2.append(5)
ll2.append(6)
ll2.append(7)
ll2.append(8)

print(ll.merge_and_sort(ll2))
