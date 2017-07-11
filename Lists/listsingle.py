class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        current = self.head

        if self.head is None:
            self.head = self.tail = new_node
        else:
            # MEMORIZE THIS: adding to the end, before tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
            # how to add to the beginning, before head?
            # new_node.next = self.head
            # self.head = new_node

    def remove(self, data):
        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next

    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return True

        return false

    def _print(self):
        current = self.head

        while current is not None:
            print current.data,
            current = current.next