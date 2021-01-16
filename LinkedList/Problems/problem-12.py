# Check if a given linked list is palindrome or not

# car is not palindrome
# dad is palindrome
# level is palindrome
# racecar is palindrome
# daad is palindrome

from LinkedList import LinkedList

class Solution(LinkedList):

    def find_middle_element(self):
        previous = slow = fast = self.head

        while fast is not None and fast.next_node is not None:
            previous = slow
            slow = slow.next_node
            fast = fast.next_node.next_node

        print(previous.data)
        print(slow.data)

    def find_by_stack(self):

        current = current2 = self.head
        my_stack = []

        while current is not None:
            my_stack.append(current.data)
            current = current.next_node

        while current2 is not None:
            if current2.data != my_stack[-1]:
                return False
            else:
                my_stack.pop()
                current2 = current2.next_node
        return True


ll = Solution()
ll.append("r")
ll.append("a")
ll.append("d")
ll.append("a")
ll.append("r")

print(ll.show())

print(ll.find_by_stack())

ll2 = Solution()
ll2.append("d")
ll2.append("a1")
ll2.append("a2")
ll2.append("d")


print(ll2.show())

print(ll2.find_by_stack())
