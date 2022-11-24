class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set() # to avoid duplicates
        
        def dfs(r, c, i):
            if i == len(word): #word found
                return True
            
            # if out of bounds or char not equal to that word or already in path: return False
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            # Check all directions
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c)) # remove possition alrady visited
            
            return res
        
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False