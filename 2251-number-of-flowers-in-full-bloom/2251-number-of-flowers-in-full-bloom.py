class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start, end = [] , []     
        for s, e in flowers:
            start.append(s)
            end.append(e)
            
        start.sort()
        end.sort()                                      
        
        return [bisect_right(start, p) - bisect_left(end, p) for p in persons ]
  
        