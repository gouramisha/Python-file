#  Rotate Array by K Steps

def rotate_array(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))