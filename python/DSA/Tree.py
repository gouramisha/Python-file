# Define a class for a tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    # Add a child to the current node
    def add_child(self, child):
        self.children.append(child)

    # Print the tree structure
    def print_tree(self, level=0):
        print(" " * level * 4 + str(self.data))
        for child in self.children:
            child.print_tree(level + 1)


# Create the root node
root = Node("Electronics")

# Create child nodes
laptop = Node("Laptop")
phone = Node("Phone")
tv = Node("TV")

# Add children to root
root.add_child(laptop)
root.add_child(phone)
root.add_child(tv)

# Add sub-children
laptop.add_child(Node("MacBook"))
laptop.add_child(Node("Dell"))

phone.add_child(Node("iPhone"))
phone.add_child(Node("Samsung"))

# Print the tree
root.print_tree()
