from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        check = [-1]*len(graph)
        
        for i in range(len(graph)):
            Q = deque([])
            if check[i] == -1:
                Q.append(i)
                check[i] = 0
            while Q:
                n1 = Q.popleft()
                for n2 in graph[n1]:
                    if check[n2] == -1:
                        check[n2] = (check[n1] + 1)%2
                        Q.append(n2)
                    elif check[n1] == check[n2]:
                            return False
        
        return True