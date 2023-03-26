from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Unlike a tree, triangle 'nodes' share children (=> subproblem redundancy)
        and layers increase in size linearly. 
        This problem has the following recursive relation: 
            minimumTotal(l, i) = triangle[l, i] + min(minimumTotal(l+1, i), minimumTotal(l+1, i+1))
        """
        dp = triangle[-1].copy()

        for l in reversed(range(len(triangle) - 1)):
            for i in range(l + 1):
                dp[i] = triangle[l][i] + min(dp[i], dp[i+1])

        return dp[0]