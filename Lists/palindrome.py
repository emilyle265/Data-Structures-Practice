def reverse(self, head):
    p = head.next
    while p and p.next:
        tmp = p.next
        p.next = p.next.next
        tmp.next = head.next
        head.next = tmp
             
def isPalindrome(self):
    """
    :type head: ListNode
    :rtype: bool
    """
     
    #get middle pointer
    p1 = Node(0)
    p1.next = self.head
    p2 = p1
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
     
    # reverse second half of list
    self.reverse(p1)
     
    # check palindrome
    p1 = p1.next
    p2 = self.head
    while p1:
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.next
        
    return True
 