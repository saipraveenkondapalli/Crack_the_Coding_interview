"""
Stack min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.

"""

from stack import Stack


class StackMin(Stack):
    def __init__(self) -> None:
        super().__init__()
        self.s2 = Stack()  # second stack to keep track of the minimum element

    def push(self, item):
        if item <= self.min():
            self.s2.push(item)
        super().push(item)

    def pop(self):
        item = super().pop()
        if item == self.min():
            self.s2.pop()
        return item

    def min(self):
        if self.s2.is_empty():
            return float('inf')
        return self.s2.peek()


if __name__ == "__main__":
    stack = StackMin()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.is_empty())
    print(stack)
    print(stack.min())
