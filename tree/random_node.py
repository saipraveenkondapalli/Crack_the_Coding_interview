"""
Problem 4.11: Random Node: You are implementing a binary tree class from scratch
Random Node: You are implementing a binary tree class from scratch which, in addition to insert, find, and delete,
has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen.
Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.

"""

# Run time complexity is O(log N) where N is the number of nodes in the tree
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

    def get_random(self):
        """
        Get a random node from the tree Description: This function will return a random chosen with equal probability
        from the tree. The probability of choosing a node is 1/N where N is the number of nodes in the tree. \n
        Approach: 1. Get the size of the left subtree. \n 2. Generate a random number between 0 and the size of the
        tree. \n 3. If the random number is less than the size of the left subtree, then call get_random on the left
        subtree. \n 4. If the random number is equal to the size of the left subtree, then return the current node.
        \n 5. If the random number is greater than the size of the left subtree, then call get_random on the right
        subtree. \n 6. Return the node. \n Returns: Node

        """
        if self.left is None:
            left_size = 0
        else:
            left_size = self.left.size

        random_index = random.randint(0, self.size - 1)

        if random_index < left_size:
            return self.left.get_random()
        elif random_index == left_size:
            return self
        elif self.right is not None:
            return self.right.get_random()

    def insert_in_order(self, d):
        if d <= self.data:
            if self.left is None:
                self.left = Node(d)
            else:
                self.left.insert_in_order(d)
        else:
            if self.right is None:
                self.right = Node(d)
            else:
                self.right.insert_in_order(d)
        self.size += 1


class Tree:
    def __init__(self):
        self.root = None

    def get_random_node(self):
        if self.root is None:
            return None
        return self.root.get_random()

    def insert_in_order(self, d):
        if self.root is None:
            self.root = Node(d)
        else:
            self.root.insert_in_order(d)

    def find(self, d):
        return None if self.root is None else self.root.find(d)


if __name__ == "__main__":
    tree = Tree()
    tree.insert_in_order(5)
    tree.insert_in_order(3)
    tree.insert_in_order(2)
    tree.insert_in_order(1)
    tree.insert_in_order(4)
    tree.insert_in_order(8)
    tree.insert_in_order(7)
    tree.insert_in_order(6)
    tree.insert_in_order(9)
    print(tree.get_random_node().data)
