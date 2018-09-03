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
        while(current):
            print(current.data)
            current = current.nextNode

    def detect_loop(self):
        current = self.head
        check = set()
        while current is not None:
            if current in check:
                return True
            check.add(current.data)
            current = current.nextNode
        return False


link = LinkedList()
link.insert(20)
link.insert(4)
link.insert(15)
link.insert(10)
link.print_list()

# link.head.nextNode.nextNode.nextNode.nextNode = link.head

print(link.detect_loop())