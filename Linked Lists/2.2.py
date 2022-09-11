
# Return kth element from the end of a linked list



from linked_lists import LinkedList


# Solution 1, recursive solution
def kth_element(head, k):
    if head == None: return 0

    index = kth_element(head.next, k) +1
    if index == k:
        return head.data

# solution 2, iterative solution
def kth_element2(head,k):
    """ 
    first we will move the first pointer k nodes ahead of the second pointer
     and then we will move both the pointers one node at a time
        when the first pointer reaches the end of the linked list, the second pointer will be at the kth node from the end
        
        Run time complexity: O(N)
        Space complexity: O(1)

     """

    p1= head # pointer 1
    p2 = head # pointer 2
    for i in range(k):
        if p1 == None:return None

        p1 = p1.next # move pointer 1 k times

    while p1 != None:
        p1 = p1.next
        p2= p2.next

    return p2.data    


