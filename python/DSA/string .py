from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        st = []  # (value, stepsNeeded)
        ans = 0

        for num in nums:
            curStep = 0
            # maintain monotonic stack
            while st and st[-1][0] <= num:
                curStep = max(curStep, st[-1][1])
                st.pop()
            if st:
                curStep += 1
            else:
                curStep = 0
            st.append((num, curStep))
            ans = max(ans, curStep)

        return ans
