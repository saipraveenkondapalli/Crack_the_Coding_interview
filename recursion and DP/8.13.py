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

def createStack(boxes):
    boxes.sort(reverse=True)
    maxHeight = 0
    for i in range(len(boxes)):
        height = createStackHelper(boxes, i, boxes[i].h)
        maxHeight = max(maxHeight, height)
    return maxHeight


def createStackHelper(boxes, bottomIndex, height):
    bottom = boxes[bottomIndex]
    maxHeight = 0
    for i in range(bottomIndex+1, len(boxes)):
        if boxes[i] < bottom:
            height = createStackHelper(boxes, i, height+boxes[i].h)
            maxHeight = max(maxHeight, height)
    maxHeight += bottom.h
    return maxHeight


# Solution 2: Memoization
# runtime O(n^2) because we have to check every box for every other box
def createStack2(boxes):
    boxes.sort(reverse=True)
    stackMap = {}
    maxHeight = 0
    for i in range(len(boxes)):
        height = createStackHelper2(boxes, i, stackMap)
        maxHeight = max(maxHeight, height)
    return maxHeight


def createStackHelper2(boxes, bottomIndex, stackMap):
    if bottomIndex in stackMap:
        return stackMap[bottomIndex]
    bottom = boxes[bottomIndex]
    maxHeight = 0
    for i in range(bottomIndex+1, len(boxes)):
        if boxes[i] < bottom:
            height = createStackHelper2(boxes, i, stackMap)
            maxHeight = max(maxHeight, height)
    maxHeight += bottom.h
    stackMap[bottomIndex] = maxHeight
    return maxHeight



if __name__ == "__main__":
    boxes = [Box(1, 1, 1), Box(2, 2, 2), Box(3, 3, 3), Box(4, 4, 4), Box(5, 5, 5)]
    print(createStack(boxes))
