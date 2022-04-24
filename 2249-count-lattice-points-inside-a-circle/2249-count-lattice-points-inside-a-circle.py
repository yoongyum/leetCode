class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = set()
        for x,y,r in circles:
            for dx in range(r+1):
                y_upper = int((r**2-dx**2)**0.5)
                for dy in range(y_upper+1):
                    ans.add((x+dx,y+dy))
                    ans.add((x+dx,y-dy))
                    ans.add((x-dx,y+dy))
                    ans.add((x-dx,y-dy))
        return len(ans)