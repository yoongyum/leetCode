class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = matrix
        self.build_sum_matrix(matrix)
    
    def build_sum_matrix(self, matrix):
        row_limit, col_limit = len(self.sum_matrix), len(self.sum_matrix[0])
        
        for row in range(row_limit):
            for col in range(col_limit):
                if row:
                    self.sum_matrix[row][col] += self.sum_matrix[row-1][col]
                if col:
                    self.sum_matrix[row][col] += self.sum_matrix[row][col-1]
                if row and col:
                    self.sum_matrix[row][col] -= self.sum_matrix[row-1][col-1]      

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.sum_matrix[row2][col2]
        if row1 - 1 >= 0:
            result -= self.sum_matrix[row1-1][col2]
        if col1 - 1 >= 0:
            result -= self.sum_matrix[row2][col1-1]
        if row1-1 >= 0 and col1-1 >= 0:
            result += self.sum_matrix[row1-1][col1-1]
        return result