class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1:
            if n in seen:
                return False  # Cycle detected
            seen.add(n)

            # Replace n with the sum of the squares of its digits
            n = sum(int(digit) ** 2 for digit in str(n))

        return True  # If we reach 1, it's a happy number
