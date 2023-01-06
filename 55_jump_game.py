class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DP: Break into subproblem canJump(pos) for pos = last...0

        dp, last = [False for pos in nums], len(nums) - 1
        dp[last] = True # Base Case

        for pos in reversed(range(last)):
            dp[pos] = nums[pos] >= last - pos or any(dp[pos+1:pos+nums[pos]+1])
        
        return dp[0]