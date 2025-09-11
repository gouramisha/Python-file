# Print Increasing using Recursion
def print_increasing(n):
    if n == 0:   
        return
    print_increasing(n - 1)  
    print(n) 