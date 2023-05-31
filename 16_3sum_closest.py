from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        - I can't see how there could be a solution to this problem that is faster that 
        O(n log n) in time => sort the list because 
        - Commonly, you capitalize off of  a list being sorted by using two pointers. Often
        you conditionally move them inwards towards each other (by 1/2 arr length in case
        of binary search)
        """
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i, num in enumerate(nums[:-2]):
            target_diff = target - num
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                pair_sum = nums[l] + nums[r]
                if abs(target_diff - pair_sum) <  abs(closest_sum - target):
                    closest_sum = num + pair_sum

                if target_diff > pair_sum: l += 1
                else: r -= 1
        
        return closest_sum
