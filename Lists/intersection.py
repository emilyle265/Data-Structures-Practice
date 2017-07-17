def intersection(self, headA, headB):
    pa, pb = headA, headB
    countA, countB = 0, 0

    # if one head is none before loop starts, return None
    if headA == None or headB == None:
        return None

    current = pa
    while current is not None:
        countA += 1 

    current = pb
    while current is not None:
        countB += 1 

    pa, pb = headA, headB

    while countA > 0 and countB > 0:
        if countA > countB:
            pa = pa.next
            countA -= 1 
        if countB > countA:
            pb = pb.next
            countB -= 1
        if countA == countB:
            if pa.data == pb.data:
                return pa
            else:
                pa = pa.next
                pb = pb.next
                countA -= 1 
                countB -= 1 

    return None
