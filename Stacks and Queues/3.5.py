"""
Sort the stack, you are allowed to use only one buffer stack
"""

# Time Complexity: O(n^2)
# Space Complexity: O(n)


from stack import Stack

def sort(stack):
    buffer = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not buffer.is_empty() and buffer.peek() > temp:
            stack.push(buffer.pop())
        buffer.push(temp)
    while not buffer.is_empty():
        stack.push(buffer.pop())
    return stack
    

if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(1)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    print(stack)
    sort(stack)
    print(stack)


