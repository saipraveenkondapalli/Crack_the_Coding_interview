from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return -1
        return max(self._height(root.left), self._height(root.right)) + 1

    @staticmethod
    def construct_binary_tree_from_list(arr: list):
        arr.sort()
        return Tree._construct_binary_tree(arr, 0, len(arr) - 1)

    @staticmethod
    def _construct_binary_tree(arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(arr[mid])
        root.left = Tree._construct_binary_tree(arr, start, mid - 1)
        root.right = Tree._construct_binary_tree(arr, mid + 1, end)
        return root

    def __str__(self):
        if not self.root:
            return "Empty Tree"

        nodes = deque([self.root])
        next_level = deque()
        result = ""

        while len(nodes) != 0:
            for node in nodes:
                result += str(node.data) + " "
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result += "\n"
            nodes = next_level
            next_level = deque()

        return result
