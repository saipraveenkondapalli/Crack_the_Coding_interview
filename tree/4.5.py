"""
Check if a given binary tree is a valid binary search tree.

"""

from tree_linked_in import Tree, Node


def Check_BST1(root):
    if root is None:
        return True
    if root.left and root.left.data >= root.data:
        return False
    if root.right and root.right.data <= root.data:
        return False
    if not Check_BST1(root.left) or not Check_BST1(root.right): # same as if Check_BST1(root.left) == False or Check_BST1(root.right) == False:

        return False
    return True


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(40)
    tree.root.left = Node(30)
    tree.root.right = Node(50)
    tree.root.left.left = Node(25)
    tree.root.left.right = Node(36)
    tree.print()
    print(Check_BST1(tree.root))
