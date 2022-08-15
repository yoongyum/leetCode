class Solution:
    def romanToInt(self, s: str) -> int:
        m = 0
        res = 0
        romanTable = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        roman = list(map(lambda x: romanTable[x], s[::-1]))
        for val in roman:
            m = max(m, val)
            if val < m:
                res -= val
            else:
                res += val
        
        return res
        