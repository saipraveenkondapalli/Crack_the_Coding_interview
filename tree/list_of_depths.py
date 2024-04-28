from utils import LinkedList, TreeNode, Tree
from collections import deque

"""
List of Depths: Given a binary tree, design an algorithm that creates a linked list of all the nodes at each depth
(e.g., if you have a tree with depth D, you'll have D linked lists).
"""


def convert_to_linked_list(user_list: list) -> LinkedList:
    cur_linked_list = LinkedList()
    for item in user_list:
        cur_linked_list.append_at_tail(item)
    return cur_linked_list


def get_nodes_at_depth(root: TreeNode, depth: int, nodes=None) -> list:
    if nodes is None:
        nodes = []
    if depth == 0:
        nodes.append(root.data)

    if root.left:
        get_nodes_at_depth(root.left, depth - 1, nodes)

    if root.right:
        get_nodes_at_depth(root.right, depth - 1, nodes)
    return nodes


"""
Run time is O(n^2) because we are calling getNodesAtDepth for each level
Space complexity is O(n) because we are storing the nodes in a list
"""


def list_of_depths(root) -> [LinkedList]:
    height = root.height()
    result = []  # list of linked lists
    for item in range(height + 1):  # if height is 3 then we have 4 levels
        cur_lev_nodes = (get_nodes_at_depth(root.root, item, []))  # gets the nodes at depth item
        result.append(convert_to_linked_list(cur_lev_nodes))

    return result


# solution 2

def solution2(root: Tree) -> [LinkedList]:
    # Run Time is O(n) because we are visiting each node once
    # Space complexity is O(n) because we are storing the nodes in a list
    # using breadth first search

    q = deque()
    q.append(root.root)
    result = []
    while q:
        count = len(q)
        cur_level = []
        while count > 0:
            cur_node = q.popleft()
            if cur_node:
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
                cur_level.append(cur_node.data)
            count -= 1
            result.append(convert_to_linked_list(cur_level))
    return result


if __name__ == "__main__":
    tree = Tree()
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.left = TreeNode(6)
    tree.root.right.right = TreeNode(7)
    tree.root.left.left.left = TreeNode(8)
    tree.root.left.left.right = TreeNode(9)
    tree.root.left.right.left = TreeNode(12)

    linked_lists: [LinkedList] = list_of_depths(tree)
