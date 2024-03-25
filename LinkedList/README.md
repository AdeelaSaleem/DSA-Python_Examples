
# Traversing a Linked List

This repository contains a Python program that demonstrates traversing a linked list and includes a dry run explanation.

## Linked List Traversal

The program defines a Node class to create nodes with data and a reference to the next node. It also includes a traversal function to traverse through the linked list and print the data of each node.

### Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Traversal Function

```python
def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next
```

## Usage

1. Create instances of the Node class to build a linked list.
2. Connect the nodes using the `next` attribute.
3. Call the `traversal` function with the head node to traverse the linked list and print its elements.

### Example

```python
# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Connecting nodes
node1.next = node2
node2.next = node3

# Traversing the linked list
print("Linked List Elements:")
traversal(node1)
```

## Dry Run Explanation

Initial linked list:
```
1 -> 2 -> 3 -> None
```

### Iteration 1:
- Current node: 1
- Output: Print 1

### Iteration 2:
- Current node: 2
- Output: Print 2

### Iteration 3:
- Current node: 3
- Output: Print 3

### End of linked list

The output of the program will be:
```
Linked List Elements:
1
2
3
```

Feel free to contribute, suggest improvements, or report any issues by opening an issue or submitting a pull request.
```

This README file provides a clear overview of the program, its usage, and includes a detailed dry run explanation for better understanding.
