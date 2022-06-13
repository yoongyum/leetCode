class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        minLen = triangle[-1]
        layer = n - 2
        while layer >= 0:
            for i in range(layer+1):
                minLen[i] = min(minLen[i], minLen[i+1]) + triangle[layer][i]
            layer -= 1
        
        return minLen[0]