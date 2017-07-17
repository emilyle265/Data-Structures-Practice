# you have 2 #s represented by LL, where each node contains a single
# digit. The digits are stored in reversed order, such that the 1's digit 
# is at the head of the list. Write a function that adds the two numbers
# and returns the sum as a linked list

def sum_lists(self, list1, list2):
    num1 = ''
    num2 = ''

    if list1 == None:
        return list2
    if list2 == None:
        return list1

    # loop through list1 and add each 'number' to num1
    self.head = list1
    current = self.head
    while current is not None:
        num1 += str(current.data)
        current = current.next

    # loop through list2 and add each 'number' to num2
    self.head = list2
    current = self.head
    while current is not None:
        num2 += str(current.data)
        current = current.next

    _sum = str(int(num1) + int(num2))

    new_list = LinkedList()

    count = 0
    while count < len(_sum):
        new_list.add(_sum[count])
        count += 1

    return new_list


list1 = LinkedList()
list1.add(6)
list1.add(1)
list1.add(7)

list2 = LinkedList()
list2.add(2)
list2.add(9)
list2.add(5)






    

