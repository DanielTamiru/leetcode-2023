from itertools import accumulate
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Brute force approach: iterate through every subarray, computing the subarray's sum
        (can be done in O(1) if cumulative sum array is computed) and incrementing counter if sum == k.
        This is O(n^2) or O(n^3). We can do better.

        Optimized approach: Similar to Pair Sum Equals k, use a linear pass putting cumulative sums 
        in a dict, where the key is the sum and the value is the number of times it has occured. 
        If (cumalitive sum - k) is a key in the dict, then there are dict[cumalitive sum - k] subarrays
        from this int back to others in nums with sum == k.
        """
        subarray_count = 0
        cumulative_sum_counts = defaultdict(int)
        cumulative_sum_counts[0] = 1
       
        for cumulative_sum in accumulate(nums):
            subarray_count += cumulative_sum_counts[cumulative_sum - k]
            cumulative_sum_counts[cumulative_sum] += 1
        
        return subarray_count
        