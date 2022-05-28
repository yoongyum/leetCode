class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        maxN = max(nums)
        
        for i, n in enumerate(nums):
            if i != n:
                return i
            
        
        return maxN+1