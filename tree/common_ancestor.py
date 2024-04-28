from utils import Tree, TreeNode as Node

"""
Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
"""
# Solution Assumptions: Each node has parent pointer
# Solution 1: Traverse up from each node until you find a common node
# Runtime: O(d) where d is the depth of the deeper node
# Space: O(1)

"""
Design custom Node class
"""


def depth(node: Node) -> int:
    """
    Get the depth of a node from the root
    Args:
        node: TreeNode

    Returns:  depth of the node from the root
    """
    distance = 0
    while node:
        node = node.parent
        distance += 1
    return distance


def go_up(node, delta):
    while delta > 0 and node:
        node = node.parent
        delta -= 1
    return node


def common_ancestor(p, q):
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p  # get shallower node
    second = p if delta > 0 else q  # get deeper node
    second = go_up(second, abs(delta))  # move deeper node up
    print(delta, first, second)
    while first != second and first and second:
        first = first.parent
        second = second.parent
    return first or second


"""
we could also trace p's path upwards and check if q is on that path.
"""


def covers(root, p):  # check if p is on the path from root to p, helper function for solution 2 ,3
    if not root:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)


# ------------------------------------------------- Solution 3 -------------------------------------------------
def get_siblings(node):  # helper function for solution2, get the sibling of a node
    if node is None or node.parent is None:
        return None
    parent = node.parent
    return parent.right if parent.left == node else parent.left


def common_ancestor2(root, p, q):  # solution 2
    if not covers(root, p) or not covers(root, q):  # Error check - one node is not in tree
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    sibling = get_siblings(p)
    parent_node = p.parent
    while not covers(sibling, q):
        sibling = get_siblings(parent_node)
        parent_node = parent_node.parent
    return parent_node


# Solution 3
# Runtime: O(n) for a balanced tree
def without_parent(root, p, q):  # solution 3, without parent pointer
    if not covers(root, p) or not covers(root, q):
        return None
    return ancestor_helper(root, p, q)


def ancestor_helper(root, p, q):
    if root is None or root == p or root == q:
        return root

    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)
    if p_is_on_left != q_is_on_left:
        return root

    child_side = root.left if p_is_on_left else root.right
    return ancestor_helper(child_side, p, q)


# ------------------------------------------------- Solution 4 -------------------------------------------------


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.left.parent = tree.root
    tree.root.right = Node(3)
    tree.root.right.parent = tree.root
    tree.root.left.left = Node(4)
    tree.root.left.left.parent = tree.root.left
    tree.root.left.right = Node(5)
    tree.root.left.right.parent = tree.root.left

