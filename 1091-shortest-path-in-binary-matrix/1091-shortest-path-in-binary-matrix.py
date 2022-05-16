class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dxy = [(0,1), (0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)] #이동방향
        
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n-1][n-1] != 0 : return -1
        
        grid[0][0] = 1
        
        Q = [(0,0)]
        if n == 1: return 1
        
        cnt = 1
        
        while Q: #BFS start
            adjs = []
            cnt += 1
            
            for x, y in Q:
                adj = []
                for dx, dy in dxy:
                    i = x+dx
                    j = y+dy
                    
                    if 0 <= i <n and 0 <= j < n and grid[i][j] == 0:
                        if i == j == n-1 : return cnt #도착지에 도달할 경우 종료
                        grid[i][j] = 1
                        adj.append((i,j))
                        
                adjs.extend(adj)
                
            Q = adjs
            
        return -1
                        