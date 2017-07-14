def intersection(self, headA, headB):
    pa, pb = headA, headB

    # if one head is none before loop starts, return None
    if headA == None or headB == None:
        return None

    while pa != pb:
        if pa == None:
            pa = headB
        else:
            pa = pa.next

        if pb == None:
            pb = headA
        else:
            pb = pb.next