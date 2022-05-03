class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max = -float('inf')
        min = float('inf')
        
        idx1 = -1
        idx2 = -1
        
        for idx, val in enumerate(nums):
            if max < val:
                max = val
            elif val < max:
                idx1 = idx
        
        for idx, val in enumerate(nums[::-1]):
            if min > val:
                min = val
            elif min < val:
                idx2 = idx
        
        if idx1 == -1:
            return 0
        
        return idx1 - (len(nums) -idx2 -1) + 1
        