from enum import Enum
from typing import List

class Direction(Enum):
    left = 1
    right = 2

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force - O(n^3): Consider all possible triplet combinations and check their sum
        Uniqueness: To ensure triplets (or any group of subsets) are unique, measures need to be
        put in place so that at least one value is different between them. A common approach is to
        sort the set, because you ensure the ordering of any subset becomes consistent (permutations 
        'merge' with combinations) and after, it is easy to skip over values that appear more than once
        (e.g. [0, 2, 2, 9] -> skip over second 2).
        Optimal Solution - O(n^2): Iteratively isolate the first number in the triplet, and then solve
        2sum with the subsequent numbers. Use the two pointer trick instead of a hashmap to save memory
        """
        nums.sort()
        i, length = 0, len(nums)
        res = []

        while i is not None:
            l, r = i + 1, length - 1

            while l and r and l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                if current_sum <= 0:
                    l = self.next_num(nums, l, Direction.right)
                else: 
                    r = self.next_num(nums, r, Direction.left)

            i = self.next_num(nums, i, Direction.right)
                    
        return res


    def next_num(self, nums: List[int], i: int, dir: Direction) -> Optional[int]:
        """
        Returns the position of the next distinct number from nums[i] in whichever
        Direction specified. If none are found, None is returned
        """
        if dir is Direction.right:
            while i < len(nums) - 1 and nums[i] == nums[i+1]: i += 1
            return i + 1 if i < len(nums) - 1 else None
        # left
        while i > 0 and nums[i-1] == nums[i]: i -= 1
        return i - 1 if i > 0 else None