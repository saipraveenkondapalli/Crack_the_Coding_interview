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

from tree_linked_in import Tree, Node


def depth(node):
    d = 0
    while node:
        node = node.parent
        d += 1
    return d


def goUp(node, delta):
    while delta > 0 and node != None:
        node = node.parent
        delta -= 1
    return node


def commonAncestor(p, q):
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p
    second = p if delta > 0 else q
    second = goUp(second, abs(delta))
    while (first != second and first != None and second != None):
        first = first.parent
        second = second.parent
    return None if (first == None or second == None) else first


"""
 
 we could trace p's path upwards and check if q is on that path.
 
"""


def covers(root, p):  # check if p is on the path from root to p, helper function for solution 2 ,3
    if not root:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)


# ------------------------------------------------- Solution 3 -------------------------------------------------
def getSibilings(node):  # helper function for solution2, get the sibling of a node
    if node == None or node.parent == None:
        return None
    parent = node.parent
    return parent.right if parent.left == node else parent.left


def commonAncestor2(root, p, q):  # solution 2
    if not covers(root, p) or not covers(root, q): # Error check - one node is not in tree
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    sibling = getSibilings(p)
    parent = p.parent
    while not covers(sibling, q):
        sibling = getSibilings(parent)
        parent = parent.parent
    return parent

# Solution 3
# Runtime: O(n) for a balanced tree
def withoutParent(root, p, q):  # solution 3, without parent pointer
    if not covers(root, p) or not covers(root, q):
        return None
    return ancestorHelper(root, p, q)


def ancestorHelper(root, p, q):
    if root == None or root == p or root == q:
        return root

    pIsOnLeft = covers(root.left, p)
    qIsOnLeft = covers(root.left, q)
    if pIsOnLeft != qIsOnLeft:
        return root

    childSide = root.left if pIsOnLeft else root.right
    return ancestorHelper(childSide, p, q)




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
    tree.print()
    p, q = tree.root.left.left, tree.root.left.right  # 4,5
    # ans = commonAncestor2(p,q)   with links to the parent
    # ans = commonAncestor(p,q)  # with links to the parent
    ans = withoutParent(tree.root, p, q)  # without links to the parent
    if ans:
        print(f"The common ancestor of {p.data} and {q.data} is {ans.data}")
    else:
        print(f"No common ancestor for {p.data} and {q.data}")
