class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cnt = 0
        Max = sum(nums)
        left = 0
        right = Max
        for i in range(len(nums)-1):
            left += nums[i]
            right = Max - left
            if left >= right:
                cnt +=1 
                
        return cnt
            