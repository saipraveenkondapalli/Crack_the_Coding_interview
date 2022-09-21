from traceback import print_tb
from webbrowser import get
from linked_lists import LinkedList
from tree_linked_in import Tree, Node


def convertToLinkedList(sample_list):
    l = LinkedList()
    for i in sample_list:
        l.appendatTail(i)
    return l

def getNodesAtDepth(root, depth, nodes = []):
    if depth == 0:
        nodes.append(root.data)

    if root.left:
        getNodesAtDepth(root.left, depth-1, nodes)
    
    if root.right:
        getNodesAtDepth(root.right, depth-1, nodes)
    return nodes

"""
Run time is O(n^2) because we are calling getNodesAtDepth for each level
Space complexity is O(n) because we are storing the nodes in a list
"""        

def listOFDepths(root):
    height  = root.height() 
    ans = [] # list of linked lists
    for i in range(height+1): # if height is 3 then we have 4 levels
        x = (getNodesAtDepth(root.root, i,[])) # gets the nodes at depth i
        ans.append(convertToLinkedList(x)) 

    
    return ans



# solution 2

def solution2(root):
    # Run Time is O(n) because we are visiting each node once
    # Space complexity is O(n) because we are storing the nodes in a list
    root = root.root
    q = []
    q.append(root)
    ans = []
    while q[0]:
        count = len(q)
        temp = []
        while count >0:
            x = q.pop(0)
            if x:
                if root.left:
                    q.append(x.left)
                if root.right:
                    q.append(x.right)
                temp.append(x.data)
            count -= 1
        ans.append(convertToLinkedList(temp))
        #print(temp)
    return ans




if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.left.left = Node(8)
    tree.root.left.left.right = Node(9)
    tree.root.left.right.left = Node(12)

    print(listOFDepths(tree))
    print(solution2(tree))
