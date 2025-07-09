# def func(x, N):
#     print(x)
#     function(x,n)
#     func(15, 4)


def print_numbers(i, n):
    if i > n:      # Jab i n se bada ho jaaye to ruk jao
        return
    print(i)       # Number print karo
    print_numbers(i + 1, n)   # Next number ke liye call karo

# Function call karo
print_numbers(1, 5)