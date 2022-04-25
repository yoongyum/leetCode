from bisect import bisect
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:

        rm = defaultdict(list)

        for l, h in rectangles:
            rm[h].append(l)
            
        for k , vl in rm.items():
            rm[k].sort()

        def contains(x, y):
            count = 0

            for height, widths in rm.items():
                if height >= y:
                    count += len(widths) - bisect_left(widths, x) #widths 리스트 안에 x보다 작은 것의 갯수

            return count

        res = []

        for point in points:
            x, y = point
            res.append(contains(x, y))

        return res
    
    
