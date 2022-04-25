from bisect import bisect
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:

        rectangle_map = defaultdict(list)

        for l, h in rectangles:
            rectangle_map[h].append(l)
            
        for k , vl in rectangle_map.items():
            rectangle_map[k].sort()

        def contains(x, y):
            count = 0

            for height, widths in rectangle_map.items():
                if height >= y:
                    count += len(widths) - bisect(widths, x - 1)

            return count

        res = []

        for point in points:
            x, y = point
            res.append(contains(x, y))

        return res