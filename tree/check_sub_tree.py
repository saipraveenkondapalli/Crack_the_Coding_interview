"""
Check Subtree: T1 is a large tree, check whether T2 is a subtree of T1
"""

from utils import Tree, TreeNode as Node


# simple solution

def pre_order(root):
    result = []

    def _help(node):
        if not node:
            result.append("X")  # X is a placeholder for None
            return
        result.append(str(node.data))
        _help(node.left)
        _help(node.right)

    _help(root)
    return result


def is_subtree(t1, t2):
    order1 = pre_order(t1)
    order2 = pre_order(t2)
    print(order1, order2)
    return "".join(order1).find("".join(order2)) != -1


def check_if_sub_tree(t1, t2):
    # Run time complexity is O(n+m) where n is the number of nodes in t1 and m is the number of nodes in t2
    string1 = []
    string2 = []
    get_order(t1, string1)
    get_order(t2, string2)
    string1 = list(map(str, string1))
    string2 = list(map(str, string2))
    return ''.join(string2) in ''.join(string1)


def get_order(node, string):
    if node is None:
        string.append('X')
        return

    string.append(node.data)
    get_order(node.left, string)
    get_order(node.right, string)


if __name__ == "__main__":
    sample_tree_1 = Tree()
    sample_tree_1.root = Node(1)
    sample_tree_1.root.left = Node(2)
    sample_tree_1.root.right = Node(3)
    sample_tree_1.root.left.left = Node(4)
    sample_tree_1.root.left.right = Node(5)
    sample_tree_1.root.right.left = Node(6)
    sample_tree_1.root.right.right = Node(7)
    sample_tree_1.root.right.left.right = Node(8)
    sample_tree_1.root.right.right.right = Node(9)

    sample_tree_2 = Tree()
    sample_tree_2.root = Node(3)
    sample_tree_2.root.left = Node(6)
    sample_tree_2.root.right = Node(7)
    sample_tree_2.root.left.right = Node(8)
    sample_tree_2.root.right.right = Node(9)

    print(check_if_sub_tree(sample_tree_1.root, sample_tree_2.root))
