# Find if linked list has even length or odd

from LinkedList import LinkedList

class Solution(LinkedList):

    def find_length(self):
        current = self.head

        while current is not None and current.next_node is not None:
            current = current.next_node.next_node
            # if current.next_node is not None:
            #     current = current.next_node

        if current is None:
            print("Lenght is even")
        else:
            print("Length is odd")


ll = Solution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print(ll.show())
ll.find_length()
ll.append(7)
print(ll.show())
ll.find_length()
