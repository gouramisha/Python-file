#  Print 3rd, 5th, and 7th element using enumerate()

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for index, value in enumerate(my_list):
    if index in [2, 4, 6]:  # 3rd, 5th, and 7th elements (0-based indexing)
        print(f"{index + 1}th element is: {value}")

        