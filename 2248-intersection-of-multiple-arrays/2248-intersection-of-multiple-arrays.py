class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res =[]
        for i in range(1,1001):
            cnt = 0
            for l in nums:
                cnt += l.count(i)
                if cnt == len(nums):
                    res.append(i)
                    
        return res
                    

        