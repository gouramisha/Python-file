class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Step 1: Roman letters ki value map karo
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0         # Final answer
        prev_value = 0    # Peeche wale character ki value yaad rakhna

        # Step 2: Right to Left jao (kyunki subtraction rule tabhi samjhenge)
        for ch in reversed(s):
            curr_value = roman[ch]   # Current roman letter ki value nikalo

            if curr_value < prev_value:
                total -= curr_value  # Agar chhoti value badi se pehle ho → subtract
            else:
                total += curr_value  # Nahi toh normal add

            prev_value = curr_value  # Current value ko next round ke liye store karo

        return total
