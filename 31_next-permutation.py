from ast import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
      """
      Intuition:
      - one swap of two digits in nums is sufficient to generate a new permutation
      - only swaps where left digit is smaller than right will yield a larger permutation
      - numbers are closer together when they have more leading/significant digits in common

      Idea:
      1. starting from least significant (rightmost) digit, find left_dig, a digit that is smaller
      than its right neighbour => digit can be swapped with any other digit in right subarray,
      which is in decreasing order. If it's not found, the list is non-increasing - reverse it.
      2. swap with right_dig, thenext smallest digit in right subarray (use binary search to find it)
      3. put digits to the right of where right_dig was in increasing order to minimize the result
      """
      # 1
      left_dig, right_dig = None, len(nums) - 1
      for dig in reversed(range(right_dig)):
          if nums[dig] < nums[dig + 1]: 
            left_dig = dig
            break

      if left_dig is None:
        nums.reverse()
        return
      
      # 2 - opted to not do binary search for simplicity. It also wouldn't reduce time complexity
      while nums[right_dig] <= nums[left_dig]: right_dig -= 1
      nums[left_dig], nums[right_dig] = nums[right_dig], nums[left_dig]
      
      # 2
      left_dig += 1
      right_dig = len(nums) - 1
      
      while left_dig < right_dig: 
        nums[left_dig], nums[right_dig] = nums[right_dig], nums[left_dig] 

        left_dig += 1
        right_dig -= 1
      