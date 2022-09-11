from linked_lists import LinkedList

# solution extra revese the linked list
def is_palindrome(llist):
    node = llist.head
    reverse = LinkedList()
    while node:
        reverse.appendAthead(node.data)
        node = node.next
    node = llist.head
    reverse_node = reverse.head
    while reverse_node:
        if not node.data == reverse_node.data:
            return False 
    
        node = node.next
        reverse_node = reverse_node.next
    return True

# using stack approach
"""
Assuming we don't know the length of the linked list, we are using fast/slow runner technique to find the middle of the linked list.

"""

def is_palindrome2(llist):
    fast = llist.head
    slow = llist.head
    stack = []
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    
    # if linked list has odd elements then slow pointer points at middle element, skip it
    if fast != None:
        slow = slow.next

    # pop the elements from the stack and compare them with the slow pointer
    while slow:
        if slow.data != stack.pop(): return False
        slow = slow.next
    return True


if __name__ == "__main__":
    # test case
    llist = LinkedList()
    llist.appendatTail("A")
    llist.appendatTail("B")
    llist.appendatTail("C")
    llist.appendatTail("D")
    llist.appendatTail("C")
    llist.appendatTail("B")
    llist.appendatTail("A")
    print(llist)
    print(is_palindrome2(llist))
