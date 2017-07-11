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
            children.append(self.rightChild)
        if self.leftChild is not None:
            children.append(self.leftChild)

        return children

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def setRoot(self, val):
        self.root = Node(val)

    def getRoot(self):
        return self.root

    def insert(self, val):
        # always start with self.root
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
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
            return self.findNode(currentNode.rightChild, val)

    def delete(self, val):
        if self.root is None:
            return "Nothing to remove!"
        else:
            self.deleteNode(self.root, val)

    # not working 
    def deleteNode(self, currentNode, val):
        if currentNode.val == val:
            currentNode.leftChild = None
            currentNode.rightChild = None
        elif currentNode.rightChild == val:
            self.deleteNode(currentNode.rightChild, val)
        elif currentNode.leftChild == val:
            self.deleteNode(currentNode.leftChild, val)

    def print_traverse(self):
        current_level = [self.root]
        while current_level:
            for item in current_level:
                print 'node: ', item.getVal()
                print 'children: ', item.getChildren()
            next_level = list()
            for node in current_level:
                if node.leftChild:
                    next_level.append(node.leftChild)
                if node.rightChild:
                    next_level.append(node.rightChild)
                current_level = next_level

        




tree = BST()
tree.setRoot(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
