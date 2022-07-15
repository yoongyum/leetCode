class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dim = [len(grid), len(grid[0])]
        ans = 0
        def dfs(i, j):
            if(not 0 <= i < dim[0] or not 0 <= j < dim[1] or grid[i][j] == 0):
                return
            temp[0] += 1
            grid[i][j] = 0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(dim[0]):
            for j in range(dim[1]):
                if(grid[i][j] == 1):
                    temp = [0]
                    dfs(i, j)
                    ans = max(ans, temp[0])
        return ans
        