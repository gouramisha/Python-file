class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Pointers to the end of initial parts of nums1 and nums2
        i = m - 1
        j = n - 1
        # Pointer to the end of nums1
        k = m + n - 1

        # Merge from back to front
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements left in nums2 (nums1 is already in place if i >= 0)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        