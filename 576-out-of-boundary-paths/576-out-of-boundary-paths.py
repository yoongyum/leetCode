class Solution:
    def neighbors(self, cell: (int, int)):
        x, y = cell
        for r, s in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            yield (x + r, y + s)
            
    def pathsFrom(self, cell: (int, int), maxMove: int) -> int:
        if (cell, maxMove) not in self.memo:
            x, y = cell
            if x == -1 or x == self.m or y == -1 or y == self.n:
                pathCount = 1
            elif maxMove == 0:
                pathCount = 0
            else:
                pathCount = 0
                for neighbor in self.neighbors(cell):
                    pathCount += self.pathsFrom(neighbor, maxMove - 1)
            self.memo[(cell, maxMove)] = pathCount % (10 ** 9 + 7)
        return self.memo[(cell, maxMove)]
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m, self.n = m, n; self.memo = {}
        return self.pathsFrom((startRow, startColumn), maxMove)
        