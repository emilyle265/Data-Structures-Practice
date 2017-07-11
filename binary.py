class Node:
    def __init__(self, val):
        self.val = val
        self.rightChild = None
        self.leftChild = None

    def getVal(self):
        return self.val

    def setVal(self, data):
        self.val = data

    def getChildren(self):
        children = []

        if self.rightChild is not None:
            children.append(rightChild)
        if self.leftChild is not None:
            children.append(leftChild)

class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = val

    def insert(self, val):
        # always start with self.root
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.val:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif val >= currentNode.val:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        # always start with self.root
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if currentNode is None:
            return False
        elif val == currentNode.val:
            return True
        elif val < currentNode.val:
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode, rightChild, val)
