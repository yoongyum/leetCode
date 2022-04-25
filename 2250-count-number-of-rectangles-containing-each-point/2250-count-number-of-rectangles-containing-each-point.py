from bisect import bisect
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:

        rectangles = sorted(rectangles, key=lambda x:x[0])

        rectangle_map = defaultdict(list)

        for l, h in rectangles:
            rectangle_map[h].append(l)

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