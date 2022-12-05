class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        m = defaultdict(list)
        
        for a,b,dist in roads:
            m[a].append([b, dist])
            m[b].append([a, dist])
            
        res = math.inf
        
        visit = set()
        
        def dfs(node):
            
            visit.add(node)
            
            for nei, cost in m[node]:
                nonlocal res
                res = min(res, cost)
                
                if nei in visit:
                    continue
                dfs(nei)
                
        dfs(1)
        
        return res
            
            
        
        