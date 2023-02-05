from copy import deepcopy
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = deepcopy(grid)
        
        # Base Cases:
        for i in reversed(range(m-1)): dp[i][-1] += dp[i+1][-1]
        for j in reversed(range(n-1)): dp[-1][j] += dp[-1][j+1]

        # General Case:
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])

        return dp[0][0]