# imaging stack of plates. If the stack sgets too high, it might topple. Therefore,
# in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should
# be composed of several stacks and should create a new stack once the previous ones exceeds
# capacity. 

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        if (len(self.stacks) == 0) or (len(self.stacks[-1]) == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks) == 0:
            return None

        data = self.stacks[-1].pop()

        # i don't get line 23-24, what is line 24 actually popping since there's
        # no specific indexing here?

        # if the last stack in list is empty, pop()?
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return data
    
    # Pop operation on a specifit sub-stack. (Index begins with 1)
    # Not "rolling over" version. OK with some stacks not at full capacity
    def popAt(self, index):
        if index < 1 or index > len(self.stacks) or len(self.stacks[index-1]) == 0:
            return None
        else:
            return self.stacks[index-1].pop() 