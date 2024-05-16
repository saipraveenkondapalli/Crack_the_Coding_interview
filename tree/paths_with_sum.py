import collections

from utils import Tree, TreeNode as Node

"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which might be positive 
or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to 
start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
"""


# Run time is O(N log N) where N is the number of nodes in the tree
def _count_path_with_sum_from_root(node: Node, target_sum: int, current_sum: int) -> int:
    """

    Args:
        node: Current Node in the tree
        target_sum: the target sum to find in the tree
        current_sum: the current running sum

    Returns: Number of paths that sums up to the target_sum

    """
    if not node:
        return 0

    current_sum += node.data
    count = 0
    if current_sum == target_sum:
        count += 1
    count += _count_path_with_sum_from_root(node.left, target_sum, current_sum)
    count += _count_path_with_sum_from_root(node.right, target_sum, current_sum)

    return count


def count_path_with_sum(root: Node, target_sum: int) -> int:
    """

    Args:
        root: The node to start traversing the tree
        target_sum: The target sum to find in the tree

    Returns: Number of paths that represents that sums up to the target sum

    """
    if root is None:
        return 0

    paths_from_root = _count_path_with_sum_from_root(root, target_sum, 0)

    left_paths = count_path_with_sum(root.left, target_sum)
    right_paths = count_path_with_sum(root.right, target_sum)

    return paths_from_root + left_paths + right_paths


# Optimized solution, use a hash table to store the number of paths that sum up to a certain value
# Run time is O(N) where N is the number of nodes in the tree


# Approach:
# 1. Recursive Traversal: The function traverses the binary tree recursively in a depth-first manner,
#    keeping track of the running sum from the root to the current node.
# 2. Memoization: To optimize the process, the function utilizes memoization. It maintains a dictionary
#    (`path_count`) to store the running sums encountered so far along with their counts. This avoids
#    redundant computations by storing and reusing intermediate results.
# 3. Checking for Paths: At each node, the function calculates the `node_sum`, which represents the sum
#    of values from the root to the current node that would result in the target sum if subtracted. It
#    then checks if there are any paths that sum up to `node_sum` by looking it up in the `path_count`
#    dictionary. If such paths exist, it increments the `total_paths` variable accordingly.
# 4. Incremental Updates: As the function traverses the tree, it updates the `path_count` dictionary to
#    keep track of the running sum encountered so far. This is done by calling the `increment_hash_table`
#    function to increment the count for the current running sum. After processing the current node and
#    its children, the updates are reverted to ensure accurate counts for different paths.

# Example:
# Consider the following binary tree:
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2    11
#  / \   \
# 3  -2   1
# Let's say the target sum is 8. The function will start traversing the tree from the root (10) and
# maintain a running sum as it traverses each path. Here's how the process unfolds:
# - At the root (10), the running sum is 10. The function checks if there are any paths that sum up to
#   `10 - 8 = 2` in the `path_count` dictionary. There are none.
# - It then recursively explores the left subtree. At node 5, the running sum becomes 15. It checks if
#   there are any paths that sum up to `15 - 8 = 7` in the `path_count` dictionary. There are none.
# - The function proceeds to explore the left subtree of node 3. At node 3, the running sum becomes 18.
#   It checks if there are any paths that sum up to `18 - 8 = 10` in the `path_count` dictionary. There's
#   one path, so it increments the `total_paths`.
# - The recursion continues until all paths are explored.


def count_path_with_sum_optimized(root, target_sum):
    """
    Count the number of paths in a binary tree that sum up to a given target sum.

    Args:
        root: The root node of the binary tree.
        target_sum (int): The target sum.

    Returns:
        int: The number of paths that sum up to the target sum.
    """
    return __count_path_with_sum_optimized(root, target_sum, 0, {})


def __count_path_with_sum_optimized(root, target_sum, running_sum, path_count) -> int:
    """
    Helper function to recursively count paths with sum in a binary tree.

    Args:
        root: The current node in the binary tree.
        target_sum (int): The target sum.
        running_sum (int): The running sum from the root to the current node.
        path_count (dict): A dictionary to store running sums and their counts.

    Returns:
        int: The number of paths that sum up to the target sum.
    """
    if root is None:
        return 0

    running_sum += root.data
    node_sum = running_sum - target_sum
    total_paths = path_count.get(node_sum, 0)

    if running_sum == target_sum:
        total_paths += 1

    increment_hash_table(path_count, running_sum, 1)
    total_paths += __count_path_with_sum_optimized(root.left, target_sum, running_sum, path_count)
    total_paths += __count_path_with_sum_optimized(root.right, target_sum, running_sum, path_count)
    increment_hash_table(path_count, running_sum, -1)

    return total_paths


def increment_hash_table(path_count, key, delta):
    """
    Utility function to increment/decrement the count of a key in a dictionary.

    Args:
        path_count (dict): The dictionary to update.
        key: The key to update.
        delta: The amount by which to increment (positive) or decrement (negative) the count.
    """
    new_count = path_count.pop(key, 0) + delta
    if new_count != 0:
        path_count[key] = new_count


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
              after loop current = 10, current+target = 18, lookup current(10),notfound, add 10 to lookup, 18 to lookup 
              then lookup = {8: 1, 18: 1, 10: 0}

           dfs(5, 10), left, currentSum = 10 
           2. Position Node : 5, lookup = {8: 1, 18: 1, 10: 0}, total =0, currentSum = 10
               after loop current = 15, current+target = 23, lookup current(15),notfound, add 15 to lookup, 23 to lookup 
               then lookup = {8: 1, 18: 1, 10: 0, 15: 0, 23: 1}
           dfs(3, 15), left, currentSum = 15

           3. Position Node : 3, lookup = {8: 1, 18: 1, 10: 0, 15: 0, 23: 1}, total =0, currentSum = 15
               after loop current = 18, current+target = 26, lookup current(18), found , then total += lookup[18] = 1, 
               then lookup = {8: 1, 18: 1, 10: 0, 15: 0, 23: 1, 26: 1}
           dfs(3, 18), right, currentSum = 18
           .........
           after right nodes are done, we pop the currentSum + targetSum from the lookup table to avoid counting the
            same path twice
       """


def count_path_with_sum_optimized2(root, target_sum):
    total_paths = 0
    lookup = collections.defaultdict(int)

    lookup[target_sum] = 1

    def dfs(node, current_sum):
        nonlocal total_paths
        if not node:
            return
        current_sum += node.data
        total_paths += lookup[current_sum]
        lookup[current_sum + target_sum] += 1

        dfs(node.left, current_sum)
        dfs(node.right, current_sum)
        lookup.pop(current_sum + target_sum)

    dfs(root, 0)
    return total_paths


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

    print(count_path_with_sum_optimized2(tree.root, 8))
