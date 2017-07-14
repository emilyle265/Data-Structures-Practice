# partition the linked list such that all data less than k will be before all
# data more than k, with k being anywhere in the right partition

def partition(self, k):
    current = self.head
    new_ll = LinkedList()

    # get left side
    while current is not None:
        if current.data < k:
            new_ll.add(current.data)
        current = current.next

    # get right side
    current = self.head 
    while current is not None:
        if current.data >= k:
            new_ll.add(current.data)
        current = current.next

    return new_ll._print()