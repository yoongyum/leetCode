class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        H, W = m, n
        M = [[0] * W for _ in range(H)]
        ans = (H * W) - len(guards) - len(walls)

        # free = 0
        # wall = 1
        # guard = 2
        # guarded = 3

        for r, c in walls: M[r][c] = 1
        for r, c in guards: M[r][c] = 2
            
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
        def dfs(y, x, d):
            nonlocal ans
            if 0 <= y < H and 0 <= x < W:
                cell = M[y][x]
                if cell == 2 or cell == 1:
                    return
                
                if cell == 0:
                    ans -= 1
                    M[y][x] = 3
                
                dy, dx = y + d[0], x + d[1]
                dfs(dy, dx, d)        
            
        for guard in guards:
            r, c = guard
            for d in dirs:
                dy, dx = r + d[0], c + d[1]
                dfs(dy, dx, d)    
            
        return ans
        
        
        
       
           
            
            
    