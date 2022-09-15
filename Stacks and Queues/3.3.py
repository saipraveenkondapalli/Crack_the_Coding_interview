"""
Stack of plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
 Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
 Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
 behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

"""


from stack import Stack

class SetOfStacks:
    def __init__(self, threshold) -> None:
        self.threshold = threshold
        self.stacks = [Stack()]
    
    def push(self, item):
        if len(self.stacks[-1]) == self.threshold:
            self.stacks.append(Stack()) 
        
        self.stacks[-1].push(item)
    
    def pop(self):
        last = self.stacks[-1]
        if val:
            val = last.pop()
            if len(last) == 0:
                self.stacks.pop()
            
            return val
        raise Exception("Stack is empty")


# Follow up: Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.above = None
        self.below = None

class Stack2:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size = 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below
    
    def push(self, data):
        if self.size >= self.capacity:
            return False
        
        self.size += 1
        n = Node(data)
        if self.size == 1:
            self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True
    
    def pop(self):
        if self.is_empty():
            return None
        
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.data
    
    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return b.data
    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.is_empty():
            self.stacks.pop()
        elif len(self.stacks) > index + 1:
            v = self.left_shift(index + 1, False)
            stack.push(v)
        
        return removed_item
    def pop_at(self, index):
        return self.left_shift(index, True) if len(self.stacks) > index else None
    
    
    



if __name__ == "__main__":
    stacks = SetOfStacks(2)
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    stacks.push(6)
    print(stacks.stacks)

    print(stacks.pop())
    print(stacks.pop())
    print(stacks.pop())
    
