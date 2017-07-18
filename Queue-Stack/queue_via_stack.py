# implement a queue class which implements a queue using 2 stacks
# Queue -- FIFO
# Stack -- LIFO

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def _print(self):
        for item in self.items:
            print item,

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0


class QueueViaStack:
    def __init__(self):
        # create s1 to push original data
        self.s1 = Stack()
        # create s2 to push s1 items reversed, so it's flipped
        self.s2 = Stack()

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        if not self.s1.isEmpty():
            while self.s1.size() > 0:
                self.s2.push(self.s1.pop())

    def size(self):
        return len(self.items)

    def _printS2(self):
        self.s2._print()

    def _printS1(self):
        self.s1._print()

q = QueueViaStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print 'Printing for S1'
q._printS1()

q.dequeue()

print 'Printing for S2'
q._printS2()