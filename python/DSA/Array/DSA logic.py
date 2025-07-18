# 1. Initialize first = second = -infinity
# 2. Traverse array:
#     a. If current number > first:
#         - second = first
#         - first = number
#     b. Else if current number > second and not equal to first:
#         - second = number
# 3. After loop ends, second is your answer
