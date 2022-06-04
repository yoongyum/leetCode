class Solution:
    def valid(self, board, row, col):
        i, j = row-1, col
        while i >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i, j = i-1, j-1
            
        i, j = row-1, col+1
        while i >= 0 and j < len(board[0]):
            if board[i][j] == 'Q':
                return False
            i, j = i-1, j+1
            
        return True
    
    def solve(self, board, row):
        if row == len(board):
            temp = []
            for val in board:
                temp.append(''.join(val.copy()))
            self.ans.append(temp)
            return
            
        for col in range(len(board)):
            if self.valid(board, row, col) == True:
                #print(row, col)
                board[row][col] = 'Q'
                self.solve(board, row+1)
                board[row][col] = '.'
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.ans = []
        self.solve(board, 0)
        return self.ans
        