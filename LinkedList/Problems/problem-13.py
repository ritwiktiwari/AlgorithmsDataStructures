"""
Implementing modular node in the linked list
n%k==0, where n is number of nodes
"""


from LinkedList import LinkedList


class Solution(LinkedList):

    def modular_node_from_beginning(self, k):
        current = self.head
        modular_node = self.head
        counter = 1
        while current.next_node is not None:
            if counter%k==0:
                modular_node = current
            counter += 1
            current = current.next_node
        print(modular_node.data)
    
    def modular_node_from_end(self, k):
        """Get first modular node from the end"""
        current = self.head
        modular_node = self.head
        for _ in range(k):
            current = current.next_node
        while current:
            current = current.next_node
            modular_node = modular_node.next_node
        print(modular_node.data)


ll = Solution()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
print(ll.show())

ll.modular_node_from_beginning(3)
ll.modular_node_from_end(3)
