class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        return self.items == []
    
    def __str__(self):
        return str(self.items)
    
    def __len__(self):
        return len(self.items)
    


# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     print(stack)
#     print(stack.pop())
#     print(stack)
#     print(stack.peek())
#     print(stack.is_empty())
#     print(stack) Output: [1, 2, 3] 3 [1, 2] 2 False [1, 2]

