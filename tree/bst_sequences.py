"""
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
"""

from utils import Tree, TreeNode
from collections import deque


def bst_sequences(root):
    """
    Generate all possible arrays that could have led to this Binary Search Tree (BST).

    Args:
        root (TreeNode): The root node of the BST.

    Returns:
        List[List[int]]: A list of all possible arrays that could have led to this BST.
    """
    if not root:
        # Base case: if root is None, return a list containing an empty list.
        return [[]]

    # Prefix stores the current node's data.
    prefix = [root.data]

    # Recursively call bst_sequences on the left and right subtrees.
    left = bst_sequences(root.left)
    right = bst_sequences(root.right)

    result = []

    # Iterate over all combinations of sequences from the left and right subtrees
    for l in left:
        for r in right:
            # Initialize an empty list to store the weaved lists
            weaved = []
            # Weave together the current left and right sequences with the prefix, in all possible ways
            weave_lists(l, r, weaved, prefix)
            # Add the weaved sequences to the result
            result.extend(weaved)
    # Return the result
    return result


def weave_lists(first, second, results, prefix):
    """
    Helper function to weave together two lists in all possible ways while maintaining their relative order using backtracking.

    Args:
        first (List[int]): The first list.
        second (List[int]): The second list.
        results (List[List[int]]): The list to store the weaved lists.
        prefix (List[int]): The prefix to append before each weaved list.
    """
    # If either list is empty, append the remaining elements of the other list to prefix and add the result to results.
    if not first or not second:
        result = prefix[:]
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    # Remove the first element from first, add it to prefix, and recursively call weave_lists.
    # This is exploring all weaves that start with an element from first.
    head_first = first.pop(0)
    prefix.append(head_first)
    weave_lists(first, second, results, prefix)
    # After the recursive call, remove the added element from prefix and add it back to first.
    # This is the "backtracking" step, undoing the previous choice.
    prefix.pop()
    first.insert(0, head_first)

    # Do the same thing for second, exploring all weaving's that start with an element from second.
    head_second = second.pop(0)
    prefix.append(head_second)
    weave_lists(first, second, results, prefix)
    # Again, undo the choice after exploring all possibilities. This is the second "backtracking" step.
    prefix.pop()
    second.insert(0, head_second)


if __name__ == "__main__":
    t = Tree()
    t.root = TreeNode(2)
    t.root.left = TreeNode(1)
    t.root.right = TreeNode(3)
    print(bst_sequences(t.root))
