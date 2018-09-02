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

    def insert_beg(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.counter+=1
        else:
            newNode.nextNode = self.head
            self.head = newNode
            self.counter+=1

    def remove_beg(self):
        if self.head is None:
            print("Linked List is already empty")
        else:
            currentNode = self.head
            self.head = self.head.nextNode
            self.counter-=1
            del currentNode

    def remove_end(self):
        if self.head is None:
            print("Linked List is already empty")
        else:
            current_head = self.head
            while current_head.nextNode.nextNode is not None:
                current_head = current_head.nextNode
            current_node = current_head
            current_head.nextNode = None
            del current_node
            self.counter-=1    
        
 
linkedlist = LinkedList()
linkedlist.remove_beg()
linkedlist.insert_end(1)
linkedlist.insert_end(2)
linkedlist.insert_end(3)
linkedlist.insert_end(4)
print("printing list")
linkedlist.print_list()
linkedlist.insert_beg(22)
print("printing list after addition of 22 in the beginning")
linkedlist.print_list()
linkedlist.remove_beg()
print("printing list")
linkedlist.print_list()
print("printing size")
linkedlist.size()
linkedlist.insert_end(55)
linkedlist.print_list()
linkedlist.remove_end()
linkedlist.print_list()

