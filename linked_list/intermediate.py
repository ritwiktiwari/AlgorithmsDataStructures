class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.counter = 0
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.nextNode

    def size(self):
        print(self.counter)

    def insert_end(self,data):
        newNode = Node(data)
        current = self.head
        if self.head is None:
            self.head = newNode
            self.counter+=1
        else:
            while current.nextNode is not None:
                current = current.nextNode
            current.nextNode = newNode
            self.counter+=1
        

linkedlist = LinkedList()
linkedlist.insert_end(1)
linkedlist.insert_end(2)
linkedlist.insert_end(3)
linkedlist.insert_end(4)
print("printing list")
linkedlist.print_list()
print("printing size")
linkedlist.size()

