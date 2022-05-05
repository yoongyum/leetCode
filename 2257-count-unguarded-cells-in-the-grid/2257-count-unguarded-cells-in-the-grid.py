class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        tile = [[0]*n for i in range(m)]
        
        # 0은 공백
        # 1은 가드
        # 2는 벽
        # 3은 가드가 왔던 곳
        for x, y in guards:
            tile[x][y] = 1
        
        for x, y in walls:
            tile[x][y] = 2
            
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        
        for x, y in guards:
            for d in range(4):
                i = x + dx[d]
                j = y + dy[d]
                while i >= 0 and i < m and j >= 0 and j < n:
                    if tile[i][j] in (0,3):
                        tile[i][j] = 3
                        i += dx[d]
                        j += dy[d]
                    else : break
            
                
            
        return sum(t.count(0) for t in tile)
        
        
        
       
           
            
            
    