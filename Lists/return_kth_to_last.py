# implement algorith to find kth to last element of a singly linked list

def add(self, data):
    current = self.head
    new_node = Node(data)

    while current.next is not None:
        current = current.next 

    # adding to end
    new_node.next = None
    self.tail.next = new_node
    self.tail = new_node

# this is kth to first, not last...need to fix
def kth_to_last(self, k):
    current = self.head
    count = k

    while current.next is not None and count > 0:
        current = current.next

    return current.data


# need to figure out how to get kth_to_last
def kth_to_first(self, k):
    current = self.head
    count = k

    while current.next is not None and count > 0:
        current = current.next
        count -= 1

    return current.data