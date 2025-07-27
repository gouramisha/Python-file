class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Step 1: Agar list empty ho
        if not strs:
            return ""

        # Step 2: Pehla string base banalo
        prefix = strs[0]

        # Step 3: Baaki sab string ke saath compare karo
        for word in strs[1:]:
            while not word.startswith(prefix):
                # Prefix ko ek ek karke chhota karo jab tak match na ho
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
