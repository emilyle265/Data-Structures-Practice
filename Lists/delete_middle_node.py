def deleteMiddle(self):
    current = self.head
    count = 1

    while current.next is not None:
        current.next = current.next.next
        count += 1 

    count = count/2
    print count, 'divided by 2'

    # reset current to self.head
    current = self.head

    while count > -1 and current.next:
        count -= 1
    # 'NoneType' object has no attribute 'next'
    current.next = current.next.next