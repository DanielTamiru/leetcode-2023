class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        merging and/or visiting every number is linear - can't do that. It must be O(log n)
        - observation: the median of the combined list must be in the range [nums1 median, nums2 median]
        - idea: iteratively trim ends of the combined list in cuts of the same size ([1,2,3] -> [2] with cut size 1)
        - Note: this solution could be made more memory efficient by using left/right bounds instead of list slicing.
                I just wanted a solution that was easier to read.
        """
       
        # Edge case:
        if not nums1: return self.med(nums2)
        if not nums2: return self.med(nums1)

        while len(nums1) > 2 and len(nums2) > 2:
            # identify which of nums1 and nums2 has the smaller/larger median 
            small, large = (nums1, nums2) if self.med(nums1) <= self.med(nums2) else (nums2, nums1)
            # compute size of trim to narrow median search
            trim_size = min(self.mid(nums1, left=True), self.mid(nums2, left=True))

            nums1 = small[trim_size:] 
            nums2 = large[:-trim_size]

        return self.med(sorted(nums1 + nums2)) # O(1) at this point (roughly).

    
    def mid(self, nums, left=False): 
        """
        middle idx of nums, defaulting to right middle idx if there are two
        """
        return (len(nums) - 1)//2 if left else len(nums)//2

    def med(self, nums):
        """
        median of nums assuming it is sorted
        """
        if len(nums) % 2 != 0: return nums[self.mid(nums)]
        return (nums[self.mid(nums, left=True)] + nums[self.mid(nums)])/2
