class stacks_in_array():
    def __init__(self, stack_size):
        #create three stacks in the array and give input stack size on each 
        # stack. The stack size parameter is the size per ONE stack.
        # This does not allocate additional space in the array
        self.array = [None] * stack_size * 3
        self.stack_size = stack_size

        self.stack1_bottom = 0
        self.stack1_top = self.stack1_bottom + self.stack_size

        self.stack2_bottom = self.stack1_top
        self.stack2_top = self.stack2_bottom + self.stack_size

        self.stack3_bottom = self.stack2_top
        self.stack3_top = self.stack3_bottom + self.stack_size

        # get stack index for all 3 stacks
        self.stack1_idx = 0
        self.stack2_idx = self.stack1_idx + self.stack_size
        self.stack3_idx = self.stack2_idx + self.stack_size

    # push to the next available position (end of) stack
    def push_stack1(self, val):
        if self.stack1_idx == self.stack1_top:
            print("stack1 is full")
            return False
        else:
            self.array[self.stack1_idx] = val
            self.stack1_idx = self.stack1_idx + 1
            return True

    def push_stack2(self, val):
        if self.stack2_idx == self.stack2_top:
            print("stack2 is full")
            return False
        else:
            self.array[self.stack2_idx] =  val
            self.stack2_idx = self.stack2_idx + 1
            return True

    def push_stack3(self, val):
        if self.stack3_idx == self.stack3_top:
            print("stack3 is full")
            return False
        else:
            self.array[self.stack3_idx] =  val
            self.stack3_idx = self.stack3_idx + 1
            return True

    # pop from end of stack
    def pop_stack1(self):
        if self.stack1_idx > self.stack1_bottom:
            self.stack1_idx = self.stack1_idx - 1
            self.array[self.stack1_idx] = None
            return True
        else:
            print("stack1 is empty")
            return False

    def pop_stack2(self):
        if self.stack2_idx > self.stack2_bottom:
            self.stack2_idx = self.stack2_idx - 1
            self.array[self.stack2_idx] = None
            return True
        else:
            print("stack1 is empty")
            return False

    def pop_stack3(self):
        if self.stack3_idx > self.stack3_bottom:
            self.stack3_idx = self.stack3_idx - 1
            self.array[self.stack3_idx] = None
            return True
        else:
            print("stack3 is empty")
            return False


    def printArray(self):
        return str(self.array)