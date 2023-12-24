"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

"""

from tree import Tree, TreeNode

def next_in_order_node(node: TreeNode):
    if node is None:
        return None

    if node.right:
        return _left_most_node(node.right)

    return _next_parent_node(node)

def _left_most_node(node: TreeNode):
    if node is None:
        return None

    while node.left:
        node = node.left

    return node


def _next_parent_node(node: TreeNode):
    if node is None:
        return None

    if node.parent is None:
        return None

    if node.parent.left == node:
        return node.parent

    return _next_parent_node(node.parent)






if __name__ == "__main__":
    tree  = Tree.construct_binary_tree_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9], with_parent=True)

    print(tree.root.left.left.data)

    print(next_in_order_node(tree.root.left.left).data)

