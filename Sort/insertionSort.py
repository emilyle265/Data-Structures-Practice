def insertionSort(alist):
    #since we want to swap an item with previous one, we start from 1
    for index in range(1,len(alist)):
        # reducing i directly will mess our for loop, so we reduce its copy j instead
        position = index

    #position>0 bcoz no point going till alist[0] since there is no value to its left to be swapped
    while position>0 and alist[position-1]>alist[position]:
        alist[position]=alist[position-1]
        #take alist[position] all the way left to the place where it has a 
        # smaller/no value to its left.
        position = position-1

    return alist