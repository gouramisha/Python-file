class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        currsum = 0
        for value in nums:
            currsum+=value
            ans.append(currsum)


        return ans