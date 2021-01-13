# Find middle of linked list

from LinkedList import LinkedList

class Solution(LinkedList):

    def find_middle_element(self):

        hare = self.head
        tortoise = self.head

        while hare.next_node is not None:
            tortoise = tortoise.next_node
            hare = hare.next_node
            if hare.next_node is not None:
                hare = hare.next_node

        print("Middle element is =", tortoise.data)

ll = Solution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print(ll.show())
ll.find_middle_element()
ll.append(6)
print(ll.show())
ll.find_middle_element()
