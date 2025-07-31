class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')   # All possible vowels (both lowercase and uppercase)
        s = list(s)                  # Convert string to list for easy swapping
        i, j = 0, len(s) - 1         # Two pointers: start (i) and end (j)

        while i < j:
            # Move left pointer until a vowel is found
            while i < j and s[i] not in vowels:
                i += 1
            # Move right pointer until a vowel is found
            while i < j and s[j] not in vowels:
                j -= 1
            # Swap the vowels
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(s)           # Join list back to string and return

sol = Solution()
print(sol.reverseVowels("IceCreAm"))   # Output: "AceCreIm"
print(sol.reverseVowels("leetcode"))   # Output: "leotcede"






        