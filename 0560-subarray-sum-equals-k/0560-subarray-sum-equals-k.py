class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        m = {0:1}
        sums = 0
        res = 0
        for i in range(len(a)):
            sums += a[i]
            if sums - k in m:
                res += m[sums-k]
            if sums in m:
                m[sums] += 1
            else:
                m[sums] = 1
        
        return res