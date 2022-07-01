class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        matrix = collections.defaultdict(list)
        
        for s , e in edges:
            matrix[s].append(e);
            matrix[e].append(s);
            
        visited = set()
        
        def DFS(node):
            if node in visited:
                return 0;
            visited.add(node);
            res = 1
            for n in matrix[node]:
                res += DFS(n)
            return res;
        
        components = []
        total_sum = 0
        
        for i in range(n):
            temp = DFS(i)
            if temp != 0:
                total_sum += temp
                components.append(temp)
        
        result = 0
        for i in components:
            result += (total_sum - i) * i
        return result//2
