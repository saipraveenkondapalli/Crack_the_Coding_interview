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




