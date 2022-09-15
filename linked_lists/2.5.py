"""
Sum Lists: You have two numbers represented by a linked list, where each node
contains a single digit. The digits are stored in reverse order, such that the 1's
digit is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

"""
from linked_lists import LinkedList, Node # import the linked list class from the linked_lists.py file

# my iterative solution

def sum_lists(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    if len1 > len2:
        for x in range(len1 - len2):
            l2.appendAthead(0) # add zeros to the head of the shorter list
    elif len2 > len1:
        for x in range(len2 - len1):
            l1.appendAthead(0) # add zeros to the head of the shorter list
    sum_linked_list = LinkedList()
    carry = 0
    cur_node1 = l1.head
    cur_node2 = l2.head
    while cur_node1 and cur_node2:
        sum = cur_node1.data + cur_node2.data + carry # add the two nodes and the carry
        if sum > 9: 
            carry = 1
            sum = sum %10 # get the last digit e.g 12 % 10 = 2
            sum_linked_list.appendatTail(sum) # add the last digit to the sum linked list
        else:
            sum_linked_list.appendatTail(sum)
            carry = 0 # reset the carry
        cur_node1 = cur_node1.next # point to the next node
        cur_node2 = cur_node2.next # point to the next node

    if carry: # if there is a carry left over
        sum_linked_list.appendatTail(carry)
    return sum_linked_list


# Follow up: Suppose the digits are stored in forward order. Repeat the above


if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l1.appendatTail(7)
    l1.appendatTail(1)
    l1.appendatTail(6)
    l1.appendatTail(5)
    l2.appendatTail(5)
    l2.appendatTail(9)
    l2.appendatTail(9)
    print(sum_lists(l1,l2))