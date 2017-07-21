def Node:
    def __init__(self, val):
        self.val = val
        self.rightChild = None
        self.leftChild = None

    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if self.rightChild:
            children.append(self.rightChild)
        if self.leftChild:
            children.append(self.leftChild)

        return children

def BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.setRoot(val)
        else:
            self.addNode(self.root, val)

    def addNode(self, currentNode, val):
        if val <= currentNode.val:
            if currentNode.leftChild:
                self.addNode(currentNode.leftChild, val)
            else:
                # if left child doens't exist, add new node to the empty left child
                currentNode.leftChild = Node(val)
        elif val > currentNode.val:
            if currentNode.rightChild:
                self.addNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def delete(self, val):
        if self.root is None:
            return None:
        else:
            self.deleteNode(self.root, val)

    # not sure how to finish delete
    def deleteNode(self, currentNode, val):
        if not currentNode:
            return None

        if currentNode.val > val:
            currentNode.leftChild = self.deleteNode(currentNode.leftChild, val)
        elif currentNode.val < val:
            currentNode.rightChild = self.deleteNode(currentNode.rightChild, val)
        else:
            if not currentNode.leftChild:
                currentNode = currentNode.rightChild
            elif not currentNode.rightChild:
                currentNode = currentNode.leftChild
            else:
                successor = currentNode.rightChild
                while successor.left:
                    successor = successor.leftChild

                currentNode.val = successor.val
                currentNode.rightChild = self.delete(currentNode.rightChild, successor.val)
