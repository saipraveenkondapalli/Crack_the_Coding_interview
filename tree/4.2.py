"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

"""

"""

Algorithm:
    1. Find the middle element of the array
    2. Make it the root of the tree
    3. Recursively do the same for the left and right subarrays
    4. Stop when the subarray is empty

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def minimal_tree(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = minimal_tree(arr[:mid])
    root.right = minimal_tree(arr[mid+1:])
    return root



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = minimal_tree(arr)
    """
    The Output tree looks like this :
                5
                 
        3                    8
    2      4             7       9
1                     6

    
    """