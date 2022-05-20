from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1: return 0

        @cache
        def dfs(x: int, y: int) -> int:
            if (x, y) == (m-1, n-1):
                return 1
            if x>=m or y>=n or obstacleGrid[x][y] == 1:
                return 0
            return dfs(x+1, y) + dfs(x, y+1)

        return dfs(0, 0)
        