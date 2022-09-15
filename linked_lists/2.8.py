#loop detection in a linked list 

"""

Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

"""

from linked_lists import LinkedList ,Node

def loop_detection(l1):
    slow = l1.head # slow pointer
    fast = l1.head # fast pointer
    while fast and fast.next: # while fast and fast.next are not None
        fast = fast.next.next # move fast by two steps
        slow = slow.next  # move slow by one step
        if fast == slow: # if fast and slow are equal then there is a loop
            break
    if fast is None or fast.next is None: # if fast or fast.next is None then there is no loop
        return None
    
    slow = l1.head # move slow to head
    while fast:
        slow = slow.next # move slow by one step
        fast = fast.next  # move fast by one step   
        if slow == fast: # if slow and fast are equal then they are at the start of the loop
            return slow
    return None




if __name__ == "__main__":    
    node1  = Node(1)
    node2  = Node(2)
    node3  = Node(3)
    node4  = Node(4)
    node5  = Node(5)
    node6  = Node(6)
    node7  = Node(7)
    l1 = LinkedList()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node4
    l1.head = node1
    print(loop_detection(l1).data)