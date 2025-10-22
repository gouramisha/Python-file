class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list for stack

    def push(self, item):
        """Add an element to the top of the stack"""
        self.stack.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        """Remove the top element from the stack"""
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack"""
        return len(self.stack)


# --- Example Usage ---
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element is:", s.peek())
    print("Stack size:", s.size())
    print("Popp")
