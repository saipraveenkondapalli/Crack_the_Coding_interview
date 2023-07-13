"""
Check Sub Tree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""

from tree import Tree, Node


# simple solution

def pre_order(root):
    result = []

    def help(node):
        if not node:
            result.append("X")
            return
        result.append(str(node.data))
        help(node.left)
        help(node.right)

    help(root)
    return result


def is_subtree(t1, t2):
    order1 = pre_order(t1)
    order2 = pre_order(t2)
    print(order1, order2)
    return "".join(order1).find("".join(order2)) != -1


if __name__ == "__main__":
    t1 = Tree()
    t1.root = Node(1)
    t1.root.left = Node(2)
    t1.root.right = Node(3)
    t1.root.left.left = Node(4)
    t1.root.left.right = Node(5)
    t1.root.right.left = Node(6)
    t1.root.right.right = Node(7)

    t2 = Tree()
    t2.root = Node(2)
    t2.root.left = Node(4)
    t2.root.right = Node(5)

    print(is_subtree(t1.root, t2.root))
