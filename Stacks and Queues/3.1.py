"""
Three in One: Describe how you could use a single array to implement three stacks.

"""

# Solution, approach 1, using a fixed division
"""
In this method, we divide the array in three equal parts and allow the individual stacks to grow in that limited space.
For the stack, we will keep track of the sizes of each stack, and always be aware of how much space each stack has.
"""

class Stack1:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [0] * (stack_size * 3)
        self.sizes = [0] * 3
    
    def is_full(self, stack_num): # check if the stack is full
        return self.sizes[stack_num] == self.stack_size
    
    def push(self, statck_num, value):
        # check if the stack is full
        if self.is_full(statck_num):
            raise Exception("Stack is full")
        # increment the stack pointer and then update the top value
        self.sizes[statck_num] += 1
        self.array[self.index_of_top(statck_num)] = value
    
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value
    
    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1
    
    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        return self.array[self.index_of_top(stack_num)]
