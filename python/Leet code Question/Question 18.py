class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract divisor using bit shifting
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Increase temp and multiple until it's too big
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Subtract the largest found multiple from dividend
            dividend -= temp
            quotient += multiple

        # Apply the correct sign
        if negative:
            quotient = -quotient

        return quotient
