# delete middle node i.e any node except first and last node

from linked_lists import LinkedList, Node

def deleteMiddleNode(node):
    """
    As per the question, you cannot iterate through the linkedlist
    
    """
    
    if node == None or node.next == None: return False
    temp = Node(node.next)
    node.data = temp.data
    node.next = temp.next
    
    return True



