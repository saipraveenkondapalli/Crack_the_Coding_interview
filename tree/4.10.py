"""
Check Subtree: T1 is a large tree, check whether T2 is a subtree of T1
"""

from tree import Tree, TreeNode as Node

# simple solution

def pre_order(root):
    result = []

    def help(node):
        if not node:
            result.append("X") # X is a placeholder for None
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



def  checkIfsubTree(t1, t2):
    # Run time complexity is O(n+m) where n is the number of nodes in t1 and m is the number of nodes in t2
    string1 = []
    string2 = []
    getOrder(t1, string1)
    getOrder(t2, string2)
    string1 = list(map(str, string1))
    string2 = list(map(str, string2))
    return ''.join(string2) in ''.join(string1)


def getOrder(node, string):
    if node is None:
        string.append('X')
        return

    string.append(node.data)
    getOrder(node.left, string)
    getOrder(node.right, string)



if __name__ == "__main__":
    t1 = Tree()
    t1.root = Node(1)
    t1.root.left = Node(2)
    t1.root.right = Node(3)
    t1.root.left.left = Node(4)
    t1.root.left.right = Node(5)
    t1.root.right.left = Node(6)
    t1.root.right.right = Node(7)
    t1.root.right.left.right = Node(8)
    t1.root.right.right.right = Node(9)

    t2 = Tree()
    t2.root = Node(3)
    t2.root.left = Node(6)
    t2.root.right = Node(7)
    t2.root.left.right = Node(8)
    t2.root.right.right = Node(9)

    print(checkIfsubTree(t1.root, t2.root))
