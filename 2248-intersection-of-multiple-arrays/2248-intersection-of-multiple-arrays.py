class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set()
        for lst in nums:
            if lst == nums[0]:
                res = set(lst)
            else:
                res &= set(lst)
        return sorted(list(res))

        