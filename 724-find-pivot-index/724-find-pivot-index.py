class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Lsum = 0
        Rsum = sum(nums)
        for i,num in enumerate(nums):
            Rsum -= num
            if Lsum == Rsum:
                return i
            Lsum += num
            
            
        return -1