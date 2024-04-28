"""
Check if a given binary tree is a valid binary search tree.

"""

from utils import Tree, TreeNode


def check_bst(root):
    if not root:
        return True
    if root.left and root.left.data >= root.data:
        return False
    if root.right and root.right.data < root.data:
        return False
    if not check_bst(root.left) or not check_bst(root.right):
        return False
    return True


if __name__ == "__main__":
    tree = Tree()
    tree.root = TreeNode(40)
    tree.root.left = TreeNode(30)
    tree.root.right = TreeNode(50)
    tree.root.left.left = TreeNode(25)
    tree.root.left.right = TreeNode(36)

    print(check_bst(tree.root))
