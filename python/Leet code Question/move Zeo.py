class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Modify nums in-place.
        """
        non_zero_index = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        # Fill remaining spaces with zeros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
