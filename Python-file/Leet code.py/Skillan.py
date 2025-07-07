#1 
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        i = 0
        min_len = min(len(word1), len(word2))

        while i < min_len:
            result += word1[i] + word2[i]
            i += 1

# 2
p1 = m - 1  # Last actual element in nums1
        p2 = n - 1  # Last element in nums2
        p = m + n - 1  # End of nums1

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are leftover elements in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# 3.
class Solution(object):
    def validPalindrome(self, s):
        def is_palindrome_range(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try removing either the left or right character
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1

        return True

        """
        :type s: str
        :rtype: bool
        """
#4.
class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)               # First define n
        ans = [0] * (2 * n)         # Now use n to create ans array

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans
    #5
    class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
#6
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        
