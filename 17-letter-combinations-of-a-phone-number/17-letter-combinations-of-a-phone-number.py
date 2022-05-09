class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        tele = ['###', '###','abc', 'def', 'ghi', 'jkl','mno', 'pqrs', 'tuv','wxyz']
        
        length = len(digits)
        if length == 0 : return []
        ans = []
        def DFS(i, curS: str):
            if len(curS) == length:
                ans.append(curS)
            for index in range(i,length):
                for c in tele[int(digits[index])]:
                    curS += c
                    DFS(index+1,curS)
                    curS = curS[:-1]
                
        DFS(0,"")
        return ans
            
        