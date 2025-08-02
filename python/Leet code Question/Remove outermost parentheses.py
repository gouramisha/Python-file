class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        count = 0  # Balance counter
        
        for char in s:
            if char == '(':
                if count > 0:
                    result.append(char)
                count += 1
            else:  # char == ')'
                count -= 1
                if count > 0:
                    result.append(char)
        
        return "".join(result)