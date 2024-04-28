from tree import TreeNode

"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

Algorithm:
    1. Find the middle element of the array
    2. Make it the root of the tree
    3. Recursively do the same for the left and right sub-arrays
    4. Stop when the subarray is empty

"""


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


def construct_binary_tree_from_arr(arr: list) -> TreeNode | None:
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = construct_binary_tree_from_arr(arr[:mid])
    root.right = construct_binary_tree_from_arr(arr[mid + 1:])
    return root
