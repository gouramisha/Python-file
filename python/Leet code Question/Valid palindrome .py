class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Keep only alphanumeric characters and convert to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        # Check if cleaned string is a palindrome
        return cleaned == cleaned[::-1]