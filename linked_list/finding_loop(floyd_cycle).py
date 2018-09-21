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
    
    
    def detect_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast:
            slow = slow.nextNode
            fast = fast.nextNode.nextNode
            if slow==fast:
                return True
        return False


link = LinkedList()
link.insert(20)
link.insert(4)
link.insert(15)
link.insert(10)
# link.print_list()

link.head.nextNode.nextNode.nextNode.nextNode = link.head

print(link.detect_loop())
