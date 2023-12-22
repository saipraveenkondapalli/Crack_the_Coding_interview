"""
Check if a given binary tree is a valid binary search tree.

"""

from tree import Tree, TreeNode


def Check_BST1(root):
    if root is None:
        return True
    if root.left and root.left.data >= root.data:
        return False
    if root.right and root.right.data < root.data:
        return False
    if not Check_BST1(root.left) or not Check_BST1(root.right): # same as if Check_BST1(root.left) == False or Check_BST1(root.right) == False:

        return False
    return True


if __name__ == "__main__":
    tree = Tree()
    tree.root = TreeNode(40)
    tree.root.left = TreeNode(30)
    tree.root.right = TreeNode(50)
    tree.root.left.left = TreeNode(25)
    tree.root.left.right = TreeNode(36)
    
    print(Check_BST1(tree.root))
