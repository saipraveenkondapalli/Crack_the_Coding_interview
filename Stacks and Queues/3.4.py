"""
Queue via stacks: Implement a MyQueue class which implements a queue using two stacks.

"""

from stack import Stack

class MyQueue:
    def __init__(self) -> None:
        self.new = Stack()
        self.old = Stack()
    
    def size(self):
        return self.new.size + self.old.size
    
    def add(self, val):
        self.new.push(val)
    
    def shiftStack(self):
        if self.old.is_empty():
            while(not self.new.is_empty()):
                self.old.push(self.new.pop())


    def remove(self):
        self.shiftStack()
        return self.old.pop()
    
    def peek(self):
        self.shiftStack()
        return self.old.peek()




    
if __name__ == "__main__":
    queue = MyQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print(queue.remove())
    queue.add(4)
   
    print(queue.remove())

