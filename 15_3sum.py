class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force - O(n^3) Consider all possible triplet combinations and check their sum
        The best solution I can think of uses a hashmap to store the difference between the 
        target sum (0) and a pair of numbers.
        """
        l = len(nums)
        res, targets = set(), set()

        for i in range(l):
            for j in range(i+1, l):
                if (nums[i] + nums[j]) in targets:
                    triplet = [-nums[i]-nums[j], nums[i], nums[j]]
                    res.add(tuple(sorted(triplet)))
            
            targets.add(-nums[i])
        
        return list(map(lambda triplet: list(triplet), res))

        