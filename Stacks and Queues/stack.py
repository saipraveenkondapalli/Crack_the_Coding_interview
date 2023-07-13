"""
Custom stack implementation that will be used to slove the problems.

"""
from linked_lists import LinkedList


class Stack:
    def __init__(self) -> None:
        self.items = []
    
    # push an item to the top of the stack
    def push(self, item):
        self.items.append(item)
    
    # pop an item from the top of the stack
    def pop(self):
        return self.items.pop()
    
    # return the top item of the stack
    def peek(self):
        return self.items[-1]

    def sort(self):
        buffer = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not buffer.is_empty() and buffer.peek() > temp:
                self.push(buffer.pop())
            buffer.push(temp)
        while not buffer.is_empty():
            self.push(buffer.pop())
        return

    # return the size of the stack
    def is_empty(self):
        return self.items == []

    def __str__(self) -> str:
        return str(self.items)

    def __len__(self) -> int:
        return len(self.items)
        

"""

stack implementation using a linked list

"""


class Stack2:
    def __init__(self) -> None:
        self.items = LinkedList()
    
    # push an item to the top of the stack
    def push(self, item):
        self.items.appendAthead(item)
    
    # removes the top element of the stack
    def pop(self):
        temp = self.items.head
        self.items.head = self.items.head.next
        return temp.data
    
    # returns the top element on the stack
    def peek(self):
        return self.items.head.data
    
    # return the whether the stack is empty or not
    def is_empty(self):
        return self.items.head == None


    def __str__(self):
        return str(self.items)
    
    def __len__(self):
        return len(self.items)


"""
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.is_empty())
    print(stack)

    stack2 = Stack2()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    print(stack2)
    print(stack2.pop())
    print(stack2)
    print(stack2.peek())
    print(stack2.is_empty())
    print(stack2)
    print(len(stack2))"""