"""
Sort the stack, you are allowed to use only one buffer stack
"""

# Time Complexity: O(n^2)
# Space Complexity: O(n)


from stack import Stack


def sort(s1):
    buffer = Stack()
    while not s1.is_empty():
        temp = s1.pop()
        while not buffer.is_empty() and buffer.peek() > temp:
            s1.push(buffer.pop())
        buffer.push(temp)
    while not buffer.is_empty():
        s1.push(buffer.pop())
    return s1


if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(1)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    stack.sort()
    print(stack)
    print(stack.pop())
    stack.push(77)
    stack.push(1)
    print(stack)
    stack.sort()
    print(stack)
