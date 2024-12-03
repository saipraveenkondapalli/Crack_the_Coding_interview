"""
stack Boxes - You have a stack of n boxes, with widths w, heights h, and depths d.
The boxes cannot be rotated and can only be stacked on top of one another
if each box in the stack is strictly larger than the box above it in width, height, and depth.
Implement a method to compute the height of the tallest possible stack.
The height of a stack is the sum of the heights of each box.

"""


class Box:
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    def __lt__(self, other):
        return self.w < other.w and self.h < other.h and self.d < other.d

    def __str__(self):
        return str(self.w) + " " + str(self.h) + " " + str(self.d)

# Solution 1: Brute Force
# runtime O(n^2) because we have to check every box for every other box

def create_stack(boxes):
    boxes.sort(reverse=True)
    max_height = 0
    for i in range(len(boxes)):
        height = create_stack_helper(boxes, i, boxes[i].h)
        max_height = max(max_height, height)
    return max_height


def create_stack_helper(boxes, bottom_index, height):
    bottom = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index + 1, len(boxes)):
        if boxes[i] < bottom:
            height = create_stack_helper(boxes, i, height + boxes[i].h)
            max_height = max(max_height, height)
    max_height += bottom.h
    return max_height


# Solution 2: Memoization
# runtime O(n^2) because we have to check every box for every other box
def create_stack2(boxes):
    boxes.sort(reverse=True)
    stack_map = {}
    max_height = 0
    for i in range(len(boxes)):
        height = create_stack_helper2(boxes, i, stack_map)
        max_height = max(max_height, height)
    return max_height


def create_stack_helper2(boxes, bottom_index, stack_map):
    if bottom_index in stack_map:
        return stack_map[bottom_index]
    bottom = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index + 1, len(boxes)):
        if boxes[i] < bottom:
            height = create_stack_helper2(boxes, i, stack_map)
            max_height = max(max_height, height)
    max_height += bottom.h
    stack_map[bottom_index] = max_height
    return max_height



if __name__ == "__main__":
    b = [Box(1, 1, 1), Box(2, 2, 2), Box(3, 3, 3), Box(4, 7, 4), Box(5, 5, 5)]
    print(create_stack(b))
