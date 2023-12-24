from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    """
    A class representing a binary tree.

    Attributes:
        root: The root node of the binary tree.

    Methods:
        height(): Returns the height of the binary tree.
        construct_binary_tree_from_list(arr: list, with_parent=False): Constructs a binary tree from a sorted list.
    """

    def __init__(self):
        self.root = None

    def height(self):
        """
        Returns the height of the binary tree.

        Returns:
            The height of the binary tree.
        """
        return self._height(self.root)

    def _height(self, root):
        """
        Helper method to calculate the height of the binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            The height of the binary tree.
        """
        if root is None:
            return -1
        return max(self._height(root.left), self._height(root.right)) + 1

    @staticmethod
    def construct_binary_tree_from_list(arr: list, with_parent=False):
        """
        Constructs a binary tree from a sorted list.

        Args:
            arr: The sorted list of elements.
            with_parent: A boolean indicating whether to include parent references in the tree nodes.

        Returns:
            A new Tree object with the constructed binary tree.
        """
        arr.sort()
        new_tree = Tree()
        new_tree.root = Tree._construct_binary_tree(arr, 0, len(arr) - 1, with_parent)
        return new_tree

    @staticmethod
    def _construct_binary_tree(arr, start, end, with_parent: bool, parent=None):
        """
        Helper method to construct a binary tree from a sorted list.

        Args:
            arr: The sorted list of elements.
            start: The starting index of the sublist.
            end: The ending index of the sublist.
            with_parent: A boolean indicating whether to include parent references in the tree nodes.
            parent: The parent node of the current node.

        Returns:
            The root node of the constructed binary tree.
        """

        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(arr[mid])
        if with_parent:
            root.parent = parent

        root.left = Tree._construct_binary_tree(arr, start, mid - 1, with_parent, root)
        root.right = Tree._construct_binary_tree(arr, mid + 1, end, with_parent, root)
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
