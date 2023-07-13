from tree_linked_in import Tree, Node


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


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.left.right = Node(7)
    tree.print()
    print(isBalanced(tree.root))
