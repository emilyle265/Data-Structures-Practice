# given a circular linked list, implement an algorithm that 
# returns the node at the beginning of the loop

def loop_detection(self):
    # set slow and fast to self.head
    slow_p = self.head
    fast_p = self.head

    # ensure that slow, fast and fast.next is not None
    while slow_p and fast_p and fast_p.next:
        # move slow to the next node
        slow_p = slow_p.next
        # move fast to the next next node (always further ahead)
        fast_p = fast_p.next.next
        # check for loop
        if slow_p == fast_p:
            print "Found Loop"
            return slow_p
    print "No loop found"