class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        current = self.head
        new_node = Node(data)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            while current.next is not None:
                current = current.next
            # add to front
            # new_node.next = self.head
            # self.head = new_node

            # add to back
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node


    def remove(self, data):
        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next

    def removeDupes(self):
        lst = []

        current = self.head

        while current.next is not None:
            if current.next.data not in lst:
                current = current.next
                lst.append(current.data)
            else:
                current.next = current.next.next

    def _print(self):
        current = self.head

        while current is not None:
            print current.data,
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        

    
ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)

new_ll = LinkedList()


