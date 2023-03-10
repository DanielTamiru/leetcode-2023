from math import inf

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Likely a candidate for dynanamic programming due to base case redundancy
        """
        n = len(nums)

        dp = [inf for num in nums]
        dp[-1] = 0

        for i in reversed(range(n-1)):
            max_j = nums[i]
            if max_j == 0: continue
            for j in range(i + 1, i + max_j + 1):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]