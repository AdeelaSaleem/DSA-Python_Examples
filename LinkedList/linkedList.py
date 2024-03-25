class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next

# Creating a linked list
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# Traversing the linked list
print("Linked List Elements:")
traversal(node1)
