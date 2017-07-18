def isPalindrome(self, head):
    if not head or not head.next:
        return True
    
    # find mid point
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # swap - reverse the second half
    cur = slow.next
    slow.next = None
    pre = None
    
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    
    # compare values from two halves
    tail = pre
    while head and tail:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.next
    
    return True