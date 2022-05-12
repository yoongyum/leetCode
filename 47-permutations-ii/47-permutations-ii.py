class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        visited = [False]*len(nums)
        save = set()
        def DFS(arr):
            if len(arr) == len(nums):
                if not tuple(arr) in save:
                    ans.append([*arr])
                    save.add(tuple(arr))
                return
            for i in range(len(nums)):
                if visited[i]:continue
                visited[i] = True
                arr.append(nums[i])
                DFS(arr)
                arr.pop()
                visited[i] = False
                
                
        DFS([])
        
        return ans