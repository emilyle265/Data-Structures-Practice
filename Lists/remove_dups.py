def removeDupes(self):
    lst = []

    current = self.head

    while current.next is not None:
        if current.next.data not in lst:
            current = current.next
            lst.append(current.data)
        else:
            current.next = current.next.next

    
