from unittest.mock import NonCallableMagicMock


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

    def deleteNode(self,key):
        cur_node = self.head 
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            return
    
        while cur_node.next != None:
            if cur_node.next.data == key: # if the next node is the key
                cur_node.next = cur_node.next.next # skip the next node .i.e key node
                return
            cur_node = cur_node.next # point to next node

        return 


    def __str__(self):
        cur_node = self.head
        while cur_node:
            if cur_node.next is None:
                print(cur_node.data, end='')
                break
            else:
                print(cur_node.data, end= "->")
                cur_node = cur_node.next
        return ""
    



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
    