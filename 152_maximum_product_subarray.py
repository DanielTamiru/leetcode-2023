from typing import List

# Note: brute force is quadratic in time. We are trying to do better than that

# Observations:
#     (1) Because these are integers, the product of a subarray of positive numbers
#     increases with its length. 
#     (2) Encountering a 0 would mean nothing preceding it mattered, effectively splitting
#     the array into two subproblems.
#     (3) Negative numbers flip the sign of the entire preceding subarray

# Intuition:
#     - To do better than O(n^2), let's try a linear pass through nums whereby we explore only
#     prospectful subarray products and at the end of each iteration, we update our result if we
#     found a larger subarray product (DP)
#     - While the negatives may be tricky to work around, subarrays with large absolute products
#     are the ones worth considering
#     - Start off by considering just one subarray starting from nums[0], setting DP[0] to nums[0]
#     - For each subsequent num, consider this recursive relation:
#         DP[i] = max(DP[i], max product of subarrays that end with nums[i])
#         Let's break the second parameter of that relation down. Depending on how large i is and
#         the composition of nums, the subarrays ending with nums[i] can all have positive products,
#         all have negative products, or often a combination of both.
#         Knowing this and obervation (3), we have a fact that helps us restrict our subarray search space:
#         * A longer positive subarray will always have a larger product AND a longer negative subarray will
#          always a more negative product (whose sign can be flipped with just one addition number) *
#         So, when keeping track of your most positive and negative subarray products so far (if they exist), 
#         you only need to consider a maximum of two subarrays at a time: the longest ones.
#     - The function below is an encoding of this logic whereby checking of negative numbers is circumvented
#       through the use of a max and min abstraction.

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
            

