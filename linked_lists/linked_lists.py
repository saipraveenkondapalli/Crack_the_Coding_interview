"""

This is a simple implementation of a linked list in Python. This class is used through out  the second chapter to
solve the coding problems.
 
this class is imported in the other files in this folder to solve the problems related to linked lists in the book
Cracking the Coding Interview.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def appendatTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def appendAthead(self, key):
        temp = self.head
        self.head = Node(key)
        self.head.next = temp
        return

        # def append at position

    def appendAtPosition(self, data, position):
        new_node = Node(data)
        cur_node = self.head
        if position == 0:
            new_node.next = cur_node
            self.head = new_node
            return
        for i in range(position - 1):
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next = new_node
        return

    def deleteNode(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            return

        while cur_node.next != None:
            if cur_node.next.data == key:  # if the next node is the key
                cur_node.next = cur_node.next.next  # skip the next node .i.e key node
                return
            cur_node = cur_node.next  # point to next node

        return

    # reverse a linked list
    def reverse(self):
        prev = None
        cur_node = self.head
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
        self.head = prev
        return

    def get_last_node(self):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        return cur_node

    def __str__(self):
        cur_node = self.head
        while cur_node:
            if cur_node.next is None:
                print(cur_node.data, end='')
                break
            else:
                print(cur_node.data, end="->")
            cur_node = cur_node.next
        return ""

    def __len__(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("Index out of range")
        cur_node = self.head
        for i in range(index):
            cur_node = cur_node.next
        return cur_node.data

    def __setitem__(self, index, value):
        if index >= len(self):
            raise IndexError("Index out of range")
        cur_node = self.head
        for i in range(index):
            cur_node = cur_node.next
        cur_node.data = value


if __name__ == "__main__":
    llist = LinkedList()
    llist.appendatTail("A")
    llist.appendatTail("B")
    llist.appendatTail("C")
    llist.appendatTail("D")
    llist.appendatTail("E")
    llist.appendatTail("B")
    llist.appendatTail("C")
    print(llist)
    # ----- output: A->B->C->D->E->B->C
