from linked_lists import LinkedList, Node

# partition of linked list 

def partition(llist, k):
    """
    partition a linked list around a value k
    """
    head = llist.head
    tail = llist.head
    cur = llist.head
    while cur:
        next = cur.next
        if cur.data < k:
            cur.next = head
            head = cur
        else:
            tail.next = cur
            tail = cur
        cur = next
    tail.next = None
    return head
"""
partiton2 is not working, I am not sure why
hold for review and fix later

"""
def partition2(node, k):
    head = None
    tail = None
    while node != None:
        if node.data  < k :
            node.next = head
            head = None
        else:
            tail.next = node
            tail = node
        node = node.next
    tail.next = None
    return head



if __name__ == "__main__":
    llist = LinkedList()
    llist.appendatTail(3)
    llist.appendatTail(5)
    llist.appendatTail(8)
    llist.appendatTail(5)
    llist.appendatTail(10)
    llist.appendatTail(2)
    llist.appendatTail(1)
    print(llist)
    llist.head = (partition2(llist, 5))
    print(llist)
