class Node:
    def __init__(self, val):
        self.val = val
        self.rightChild = None
        self.leftChild = None

    def getChildren(self):
        children = []
        if self.leftChild is not None:
            children.append(self.leftChild)

        if self.rightChild is not None:
            children.append(self.rightChild)

    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val = val

class BST:
    def __init__(self):
        self.root= None

    def setRoot(self, val):
        self.root = val

    def getRoot(self):
        return self.root

    def insert(self, val):
        return self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.leftChild:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif val > currentNode.rightChild:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self):
        return findNode(self.root, val)

    def findNode(self, currentNode, val):
        if val == currentNode.val:
            return True
        elif val is None:
            return False
        elif val >= currentNode.val:
            return self.findNode(currentNode.rightChild, val)
        elif val < currentNode.val:
            return self.findNode(currentNode.leftChild, val)

    def valid(self):
        return self.is_valid(self.root, float("-inf"), float("inf"))

    def is_valid(self, currentNode, _min, _max):
        if currentNode.val <= _min:
            return False
        if currentNode.val >= _max:
            return False

        left_ok = True
        right_ok = True

        if currentNode.leftChild is not None:
            left_ok = self.is_valid(currentNode.leftChild, _min, currentNode.val)

        if currentNode.rightChild is not None:
            right_ok = self.is_valid(currentNode.rightChild, currentNode.val, _max)

        return left_ok and right_ok

    def _min(self):
        return self.minimum(self, currentNode, float("inf")

    def minimum(self, currentNode, _min):
        if currentNode:
            if currentNode.val < _min:
                _min = currentNode.val

            self.minimum(currentNode.leftChild, _min)
            self.minimum(currentNode.rightChild, _min)

        return _min
    def _max(self):
