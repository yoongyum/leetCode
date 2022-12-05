class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = list(range(n+1))
        
        def find(a):
            nonlocal d
            if d[a] == a:
                return a
            d[a] = find(d[a])
            return d[a]
        
        r = 10001
        for a, b, c in roads:
            d[find(a)] = find(b)
            
        for a, b, c in roads:
            if find(a) == find(1):
                r = min(r, c)
        return r
            
            
        
        