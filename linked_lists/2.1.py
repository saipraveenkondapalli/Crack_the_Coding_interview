"""
NOTE : WE ARE IMPORTING CUSTOM LINKED LIST CLASS FROM THE LINKED_LISTS.PY FILE
QUESTION: Remove duplicate nodes from linked list

EXAMPLE:
Input: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
Output: 1 -> 2 -> 3 -> 4 -> 5

"""
from linked_lists import LinkedList
import unittest


# solution 1 using a set as a buffer takes O(N) time and O(N) space

def remove_duplicates(llist):
    cur_node = llist.head
    prev_node = None
    seen = set() # using set to store the values, so that we can check if the value is already present in O(1) time
    while cur_node:
        if cur_node.data in seen: # if the value is already present in the set
            prev_node.next = cur_node.next # skip the current node, i.e remove the current node, by pointing the previous node to the next node
            cur_node = None  # delete the current node
        else:
            seen.add(cur_node.data) # if the value is not present in the set, add it to the set
            prev_node = cur_node # point the previous node to the current node
        cur_node = prev_node.next # point the current node to the next node
    return llist 

# Solution 2, wthout using buffer, takes O(N^2) time and O(1) space

def remove_duplicates2(llist):
    cur_node = llist.head
    while cur_node:
        runner = cur_node
        while runner.next:
            if runner.next.data == cur_node.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur_node = cur_node.next
    return llist



if __name__ == "__main__":
    llist = LinkedList()
    llist.appendatTail("A")
    llist.appendatTail("B")
    llist.appendatTail("C")
    llist.appendatTail("D")
    llist.appendatTail("E")
    llist.appendatTail("B")
    llist.appendatTail("C")
    
    print("orginal linked list:       ",llist)
    print("After removing duplicates: ",remove_duplicates2(llist))