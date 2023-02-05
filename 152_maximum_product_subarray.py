from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Note: brute force is quadratic in time. We are trying to do better than that
        Observations:
            - Because these are integers, the product of a subarray of positive numbers
            increases with its length. 
            - Encountering a 0 would mean nothing preceding it mattered, effectively splitting
            the array into two subproblems.
            - Encountering a negative number is only bad until we encounter a second one. In fact, 
            if we just keep multiplying non-zero numbers, we'll get abs max that bounces between
            max and min.
        """
        res = max_prod = min_prod = nums[0]

        for num in nums[1:]:
            cur_vals = (min_prod * num, max_prod * num, num)
            max_prod, min_prod = max(cur_vals), min(cur_vals)
            res = max(res, max_prod)
            
        return res
            

