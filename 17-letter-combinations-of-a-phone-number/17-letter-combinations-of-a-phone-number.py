class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits : return [] 
        tel = ['###', '###','abc', 'def', 'ghi', 'jkl','mno', 'pqrs', 'tuv','wxyz']
        
        length = len(digits)
        ans = []
        def DFS(i, curS: str):
            if len(curS) == length:
                ans.append(curS)
            for idx in range(i,length):
                for c in tel[int(digits[idx])]:
                    curS += c
                    DFS(idx+1,curS)
                    curS = curS[:-1]
                
        DFS(0,"")
        return ans
            
        