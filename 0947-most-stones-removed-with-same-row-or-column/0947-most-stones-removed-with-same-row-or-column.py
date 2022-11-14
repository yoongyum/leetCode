class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        h_map = {}
        for stone in stones:
            stone = tuple(stone)
            r, c = stone
            if ('r', r) in h_map:
                h_map[('r', r)].add(stone)
            else:
                h_map[('r', r)] = {stone}
                
            if ('c', c) in h_map:
                h_map[('c', c)].add(stone)
            else:
                h_map[('c', c)] = {stone}
        
        def dfs(stone):
            visited.add(stone)
            x, y = stone
            for s in h_map[('r', x)]:
                if s not in visited:
                    dfs(tuple(s))
            for s in h_map[('c', y)]:
                if s not in visited:
                    dfs(tuple(s))
            
        visited = set()
        count = 0
        for stone in stones:
            stone = tuple(stone)
            if stone not in visited:
                dfs(stone)
                count+=1
        return len(stones) - count