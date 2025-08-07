# Step 1: Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Create nodes manually
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

# Step 3: Link nodes
head.next = second
second.next = third
third.next = fourth

# Step 4: Function to print the linked list
def print_linked_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next

# Call the function
print("Linked List:")
print_linked_list(head)