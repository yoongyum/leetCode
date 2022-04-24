class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res =[]
        for i in range(1,1001):
            if all(i in l for l in nums):res.append(i)
                    
        return res
                    

        