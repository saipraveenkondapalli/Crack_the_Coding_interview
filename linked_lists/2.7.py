"""
Linked List Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.


"""

from linked_lists import LinkedList ,Node

def intersection(l1, l2):
    len1 = 0
    len2 = 0
    tail1 = None
    tail2 = None
    # get tail of l1 and l2 
    temp1 = l1.head
    temp2 = l2.head
    while temp1:
        len1 += 1
        tail1 = temp1
        temp1 = temp1.next
    while temp2:
        len2 += 1
        tail2 = temp2
        temp2 = temp2.next
    # if tail of l1 and l2 are not same then they are not intersecting
    if tail1 != tail2:
        return False 
    p1 = l1.head
    p2 = l2.head
    # if l1 is longer than l2 then move p1 by the difference of the length of l1 and l2
    if len1 > len2:
        for i in range(len1-len2):
            p1 = p1.next
    # if l2 is longer than l1 then move p2 by the difference of the length of l2 and l1
    elif len2 > len1:
        for i in range(len2-len1):
            p2 = p2.next
    # now move both p1 and p2 by one step at a time until they are equal
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    if p1 == None:
        return False
    return p1


if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()
    node1  = Node(1)
    node2  = Node(2)
    node3  = Node(3)
    node4  = Node(4)
    node5  = Node(5)
    node6  = Node(6)
    node7  = Node(7)
    l1 = LinkedList()
    l2 = LinkedList()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node7
    node6.next = node5
    l1.head = node1
    l2.head = node6
    ans = intersection(l1, l2)
    if ans:
        print(ans.data)
    else:
        print("No intersection")
    
