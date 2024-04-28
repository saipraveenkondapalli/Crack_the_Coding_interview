"""
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, 
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more 
than one.
"""

from utils import Tree
import sys


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def isBalanced(root):
    # Runtime is O(n log n) because we are calling height() for each node in the tree
    if not root:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if abs(lh - rh) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True

    return False


def isBalanced2(root):
    """
    Runtime is O(n) because we are marking failed subtrees with sys.maxsize * -1 and returning the error early
    """
    return _is_balanced3(root) > 0


def _is_balanced2(root):
    if not root:
        return -1

    left = _is_balanced2(root.left)
    if left == sys.maxsize * -1:
        return sys.maxsize * -1

    right = _is_balanced2(root.right)
    if right == sys.maxsize * -1:
        return sys.maxsize * -1

    if abs(left - right) > 1:
        return sys.maxsize * -1
    return 1 + max(left, right)


def _is_balanced3(root):
    if not root:
        return 0
    try:
        left = _is_balanced3(root.left)
        right = _is_balanced3(root.right)
        if abs(left - right) > 1:
            raise UnBalancedException()
        return 1 + max(left, right)
    except UnBalancedException:
        return False


class UnBalancedException(Exception):
    pass


if __name__ == "__main__":
    arr = [x for x in range(20)]
    tree = Tree.construct_binary_tree_from_list(arr)
    print(isBalanced(tree.root))
    print(isBalanced2(tree.root))
