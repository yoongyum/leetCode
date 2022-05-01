class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1 = []
        ans2 = []
        
        tmp = list(s)
        
        while tmp :
            tt = tmp.pop(0)
            if tt == '#' :
                if ans1 :
                    ans1.pop()
                
            else:
                ans1.append(tt)
        tmp = list(t)
        while tmp :
            tt = tmp.pop(0)
            if tt == '#' :
                if ans2 :
                    ans2.pop()
                
            else:
                ans2.append(tt)
        
        return ans1 == ans2