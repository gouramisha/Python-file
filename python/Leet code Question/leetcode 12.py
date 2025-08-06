class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # Create a (m+1) x (n+1) DP table initialized to False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Fill in first row (matching empty string with pattern)
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the rest of the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Zero occurrence of the character before '*'
                    dp[i][j] = dp[i][j - 2]
                    # One or more occurrences if matching character
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
        
        return dp[m][n]