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
        self.size = 0

    def getRandom(self):
        """
        :return: a random node from the tree
        """
        leftSize = 0 if self.left == None else self.left.size
        index = random.randint(0, self.size - 1)
        if index < leftSize:
            return self.left.getRandom()
        elif index == leftSize:
            return self
        else:
            return self.right.getRandom()

    def insertInOrder(self, d):
        if d <= self.data:
            if self.left is None:
                self.left = Node(d)
            else:
                self.left.insertInOrder(d)
        else:
            if self.right is None:
                self.right = Node(d)
            else:
                self.right.insertInOrder(d)
        self.size += 1

    def find(self, d):
        if d == self.data:
            return self
        elif d <= self.data:
            return None if self.left == None else self.left.find(d)
        else:
            return None if self.right == None else self.right.find(d)


class Tree:
    def __init__(self):
        self.root = None

    def getRandomNode(self):
        if self.root == None:
            return None
        return self.root.getRandom()

    def insertInOrder(self, d):
        if self.root == None:
            self.root = Node(d)
        else:
            self.root.insertInOrder(d)

    def find(self, d):
        return None if self.root == None else self.root.find(d)


if __name__ == "__main__":
    tree = Tree()
    tree.insertInOrder(5)
    tree.insertInOrder(3)
    tree.insertInOrder(2)
    tree.insertInOrder(1)
    tree.insertInOrder(4)
    tree.insertInOrder(8)
    tree.insertInOrder(7)
    tree.insertInOrder(6)
    tree.insertInOrder(9)
    print(tree.getRandomNode().data)
