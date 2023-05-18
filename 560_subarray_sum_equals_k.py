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


###################################################################################
## Variation of this problem:                                                    ##
## Given an integer, k, determine the longest subarray in arr with sum at most k ##
###################################################################################

def max_length(arr, k):
    """
    Note: positive ints => the longer the subarrayy, the larger the sum
    subarray is [start_idx, idx] inclusive and subarray_sum should
    accurately reflect its sum at all times
    """

    start_idx = 0
    subarray_sum = 0

    result = 0

    for idx in range(len(arr)):
        subarray_sum += arr[idx]
        if subarray_sum <= k: result = max(result, idx - start_idx + 1)

        while subarray_sum > k and start_idx <= idx:
            subarray_sum -= arr[start_idx]
            start_idx += 1
    
    return result
