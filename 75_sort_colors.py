from collections import Counter
from typing import List

RED, WHITE, BLUE = 0, 1, 2

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counts = Counter(nums)

        first_position = {RED: 0}
        first_position[WHITE] = color_counts.get(RED, 0)
        first_position[BLUE] = first_position[WHITE] + color_counts.get(WHITE, 0)
        
        for i in range(len(nums)):
            while i < first_position[nums[i]]:
            
                pos = first_position[nums[i]]
                while pos < first_position[nums[i]] + color_counts[nums[i]]:
                    if nums[pos] != nums[i]:
                        nums[pos], nums[i] = nums[i], nums[pos]
                        break
                    pos += 1


#################################
# Dutch National Flag algorithm #
#################################

class Solution2(object):
    def sortColors(self, nums):
        lo, mid, hi = 0, 0, len(nums)-1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1