class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.nextNode
    
    def reverse(self):
        reverse_link_list = LinkedList()
        current = self.head
        while current:
            reverse_link_list.insert(current.data)
            current = current.nextNode
        reverse_link_list.print_list()

    def reverse_inplace(self):
        # init previous and current as none; current as head
        previous = None
        current = self.head
        next = None
        while current is not None:
            next = current.nextNode        # Store next node
            current.nextNode = previous    # Update the reference of current node
            # Increment previous and current
            previous = current
            current = next
        self.head = previous

link = LinkedList()
link.insert(20)
link.insert(4)
link.insert(15)
link.insert(10)
link.print_list()
link.reverse()
link.reverse_inplace()
link.print_list()