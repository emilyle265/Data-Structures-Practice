# sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into
# any other data structure (such as an array). The stack supports the
# following operations: push, pop, peek, and isEmpty.

def sort_stack(self):
    self.s2 = Stack()
    # self.s = Stack()

    while !(self.s1.isEmpty()):
        # get the end item from original stack
        x = s1.pop()
        while(not self.s2.isEmpty()) and (self.s2.peek() < x)):
            s1.push(s2.pop())
        s2.push(x)
