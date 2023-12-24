import collections

from tree import Tree, TreeNode as Node


# Run time is O(N log N) where N is the number of nodes in the tree
def CountPathWithSumFromRoot(node, targetSum, currentSum):
    if not node: return 0

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


# Optimized solution, use a hash table to store the number of paths that sum up to a certain value
# Run time is O(N) where N is the number of nodes in the tree

def countPathWithSumOptimized(root, targetSum):
    return __countPathWithSumOptimized(root, targetSum, 0, {})


def __countPathWithSumOptimized(root, targetSum, runningSum, pathCount):
    if root is None: return 0

    runningSum += root.data
    sum = runningSum - targetSum
    totalPaths = pathCount.get(sum, 0)

    if runningSum == targetSum:
        totalPaths += 1

    incrementHashTable(pathCount, runningSum, 1)
    totalPaths += __countPathWithSumOptimized(root.left, targetSum, runningSum, pathCount)
    totalPaths += __countPathWithSumOptimized(root.right, targetSum, runningSum, pathCount)
    incrementHashTable(pathCount, runningSum, -1)

    return totalPaths


def incrementHashTable(pathCount, key, delta):
    newCount = pathCount.get(key, 0) + delta
    if newCount == 0:
        pathCount.pop(key)
    else:
        pathCount[key] = newCount


# optimized DFS method
"""
       we are using current sum + target sum as the key because we are looking for the number of paths that sums up to `target` sum
       so if we have a path that sums up to current sum + target sum, then we have a path that sums up to target sum
       example
       target sum = 8
       current sum = 5
       current sum + target sum = 13
       if we have a path that sums up to 13, then we have a path that sums up to 8
       tree:
               10
               /  \
               5   -3
               / \    \
               3   2   11
               / \   \
               3  -2   1
           1. Position Node : 10, lookup = {8: 1}, total =0, currentSum = 0
              after loop current = 10, current+target = 18, lookup current(10),notfound, add 10 to lookup, 18 to lookup then lookup = {8: 1, 18: 1, 10: 0}

           dfs(5, 10), left, currentSum = 10 
           2. Position Node : 5, lookup = {8: 1, 18: 1, 10: 0}, total =0, currentSum = 10
               after loop current = 15, current+target = 23, lookup current(15),notfound, add 15 to lookup, 23 to lookup then lookup = {8: 1, 18: 1, 10: 0, 15: 0, 23: 1}
           dfs(3, 15), left, currentSum = 15

           3. Position Node : 3, lookup = {8: 1, 18: 1, 10: 0, 15: 0, 23: 1}, total =0, currentSum = 15
               after loop current = 18, current+target = 26, lookup current(18), found , then total += lookup[18] = 1, then lookup = {8: 1, 18: 1, 10: 0, 15: 0, 23: 1, 26: 1}
           dfs(3, 18), right, currentSum = 18
           .........
           after right nodes are done, we pop the currentSum + targetSum from the lookup table to avoid counting the same path twice
       """
def countPathWithSumOptimized2(root, targetSum):
    total = 0
    lookup = collections.defaultdict(int)

    lookup[targetSum] = 1

    def dfs(node, currentSum):
        nonlocal total
        if not node: return
        currentSum += node.data
        total += lookup[currentSum]
        lookup[currentSum + targetSum] += 1

        dfs(node.left, currentSum)
        dfs(node.right, currentSum)
        lookup.pop(currentSum + targetSum)

    dfs(root, 0)
    return total


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
    
    print(countPathWithSumOptimized2(tree.root, 8))
