class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set([])
        for x,y,r in circles:
            sx= x-r
            sy = y-r
            for sx in range(x+r+1):
                for sy in range(y+r+1):
                    if math.pow(r,2) >= math.pow(x-sx,2) + math.pow(y-sy,2):
                        res.add((sx,sy))
                     
        return len(res)