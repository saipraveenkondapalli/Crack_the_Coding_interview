from tree_linked_in import Tree, Node


# Run time is O(N log N) where N is the number of nodes in the tree
def CountPathWithSumFromRoot(node, targetSum, currentSum):
    if node is None: return 0
    currentSum += node.data
    count = 0
    if currentSum == targetSum:
        count += 1
    count += CountPathWithSumFromRoot(node.left, targetSum, currentSum)
    count += CountPathWithSumFromRoot(node.right, targetSum, currentSum)

    return count


def countPathWithSum(root, targetSum):
    if root is None: return 0

    pathsFromRoot = CountPathWithSumFromRoot(root, targetSum, 0)

    leftPaths = countPathWithSum(root.left, targetSum)
    rightPaths = countPathWithSum(root.right, targetSum)

    return pathsFromRoot + leftPaths + rightPaths


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(-3)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(2)
    tree.root.left.left.left = Node(3)
    tree.root.left.left.right = Node(-2)
    tree.root.left.right.right = Node(1)
    tree.root.right.right = Node(11)
    tree.print()
    print(countPathWithSum(tree.root, 8))
