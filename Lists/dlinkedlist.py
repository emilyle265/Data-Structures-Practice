class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def add(self, data):
        new_node = Node(data)
        current = self.head

        if self.head is None:
            self.head = self.tail = new_node
        else:
            # new_node.previous = self.tail
            # new_node.next = None 
            # self.tail.next = new_node
            # self.tail = new_node #why? because we are making the new_node the last node so the tail needs to be the last node.
            while current.next is not None:
                current = current.next

            # ADDING TO THE FRONT
            new_node.next = self.head
            self.head = new_node

    def remove(self, value):
        current = self.head

        while current.next is not None:
            current = current.next
            if current.data == value:
                current.previous = current.previous.previous 
                current.next = current.previous.next.next

    def _print(self):
        current = self.head

        while current is not None:
            print current.data,
            current = current.next

    def search(self, data):
        current = self.head

        while current.next is not None:
            current = current.next
            if current.data == data:
                return True

        return False

dll = DoubleLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.add(5)
dll.add(6)