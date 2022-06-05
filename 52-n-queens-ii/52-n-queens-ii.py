class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self._backtrack(n, [], list(range(n)))
        return self.count
    
    
    def _backtrack(self, n: int, curr_picks: List[int], available_cols: List[int]):
        if len(curr_picks) == n:
            self.count += 1
            
        for idx in range(len(available_cols)):
            col = available_cols[idx]
            
            if self._eligible(curr_picks, col):
                self._backtrack(n, curr_picks + [col], available_cols[:idx] + available_cols[idx+1:])
                
    
    def _eligible(self, curr_picks: List[int], col: int):
        row = len(curr_picks)
        
        for r in range(len(curr_picks)):
            c = curr_picks[r]
            
            if abs(r - row) == abs(c - col):
                return False
            
        return True
        