class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(nums, path):

            if not nums:
                return len(path)
            
            temp = path + nums[0]
            if len(temp) > len(set(temp)):
                return backtrack(nums[1:], path)
            
            return max(backtrack(nums[1:], path + nums[0]), backtrack(nums[1:], path))
        
        return backtrack(arr,"")