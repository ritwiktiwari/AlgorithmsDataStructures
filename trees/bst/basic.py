class Node(object):
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertNode(self.root,data)
    
    def insertNode(self, root, data):
        if data<root.data:
            if root.leftChild is None:
                root.leftChild = Node(data)
            else:
                self.insertNode(root.leftChild,data)

        else:
            if root.rightChild is None:
                root.rightChild = Node(data)
            else:
                self.insertNode(root.rightChild, data)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, root):
        if root.leftChild is not None:
            return self.getMin(root.leftChild)
        else:
            return root.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, root):
        if root.rightChild is not None:
            return self.getMax(root.rightChild)
        else:
            return root.data   

    def inorder(self):
        if self.root is not None:
            return self.traverseInorder(self.root)
    def traverseInorder(self, root):
        if root.leftChild is not None:
            self.traverseInorder(root.leftChild)
        print(root.data)
        if root.rightChild is not None:
            self.traverseInorder(root.rightChild)

    def predorder(self):
        if self.root is not None:
            return self.traversePreorder(self.root)
    def traversePreorder(self, root):
        print(root.data)
        if root.leftChild is not None:
            self.traversePreorder(root.leftChild)
        if root.rightChild is not None:
            self.traversePreorder(root.rightChild)

    def postorder(self):
        if self.root is not None:
            return self.traversePostorder(self.root)
    def traversePostorder(self, root):
        if root.leftChild is not None:
            self.traversePostorder(root.leftChild)
        if root.rightChild is not None:
            self.traversePostorder(root.rightChild)
        print(root.data)    

bst = BinarySearchTree()
bst.insert(25)
bst.insert(35)
bst.insert(2)
bst.insert(1)
bst.insert(4)
bst.insert(9)
bst.insert(26)

print(bst.getMinValue())
print(bst.getMaxValue())

print('\n')
print('Inorder Traversal')
bst.inorder()
print('\n')
print('Postorder Traversal')
bst.postorder()
print('\n')
print('Preorder Traversal')
bst.predorder()