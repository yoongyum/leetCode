class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        intervals = [[] for _ in range(201)]
        for x, y, r in circles:
            for i in range(-r, r + 1):
                d = math.floor(math.sqrt(r**2 - i**2))
				# Add [start, 0] and [end, 1] to the list of intervals.
                intervals[x + i].append([y - d, 0])
                intervals[x + i].append([y + d, 1])
        res = 0

        for l in intervals:
            if l:
                l.sort()
				# count of open intervals.
                count = 0
                for i, ind in l:
                    if count == 0:
                        s = i
                    if ind == 0:
                        count += 1
                    else:
                        count -= 1
                        if count == 0:
                            res += i - s + 1
        return res