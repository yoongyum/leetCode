class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        res = []
        if target not in nums:
            return [-1,-1]
        if len(nums) ==1 and nums[0] == target:
            return [0,0]
        n = nums.index(target)
        res.append(n)
        res.append(n)
        for i in range(n+1,len(nums)):
            if nums[i] == target:
                res[1] = i
        return res
        