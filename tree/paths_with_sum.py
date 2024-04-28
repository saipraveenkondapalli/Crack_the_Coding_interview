import collections

from utils import Tree, TreeNode as Node

"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which might be positive 
or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to 
start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
"""


# Run time is O(N log N) where N is the number of nodes in the tree
def count_path_with_sum_from_root(node, target_sum, current_sum):
    if not node:
        return 0

    current_sum += node.data
    count = 0
    if current_sum == target_sum:
        count += 1
    count += count_path_with_sum_from_root(node.left, target_sum, current_sum)
    count += count_path_with_sum_from_root(node.right, target_sum, current_sum)

    return count


def count_path_with_sum(root, target_sum):
    if root is None:
        return 0

    paths_from_root = count_path_with_sum_from_root(root, target_sum, 0)

    left_paths = count_path_with_sum(root.left, target_sum)
    right_paths = count_path_with_sum(root.right, target_sum)

    return paths_from_root + left_paths + right_paths


# Optimized solution, use a hash table to store the number of paths that sum up to a certain value
# Run time is O(N) where N is the number of nodes in the tree

def count_path_with_sum_optimized(root, target_sum):
    return __count_path_with_sum_optimized(root, target_sum, 0, {})


def __count_path_with_sum_optimized(root, target_sum, running_sum, path_count):
    if root is None: return 0

    running_sum += root.data
    total_sum = running_sum - target_sum
    total_paths = path_count.get(total_sum, 0)

    if running_sum == target_sum:
        total_paths += 1

    increment_hash_table(path_count, running_sum, 1)
    total_paths += __count_path_with_sum_optimized(root.left, target_sum, running_sum, path_count)
    total_paths += __count_path_with_sum_optimized(root.right, target_sum, running_sum, path_count)
    increment_hash_table(path_count, running_sum, -1)

    return total_paths


def increment_hash_table(path_count, key, delta):
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


def count_path_with_sum_optimized2(root, target_sum):
    total = 0
    lookup = collections.defaultdict(int)

    lookup[target_sum] = 1

    def dfs(node, current_sum):
        nonlocal total
        if not node:
            return
        current_sum += node.data
        total += lookup[current_sum]
        lookup[current_sum + target_sum] += 1

        dfs(node.left, current_sum)
        dfs(node.right, current_sum)
        lookup.pop(current_sum + target_sum)

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

    print(count_path_with_sum_optimized2(tree.root, 8))
