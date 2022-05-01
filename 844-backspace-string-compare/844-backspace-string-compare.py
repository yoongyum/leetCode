class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1 = []
        ans2 = []
        
        tmp = list(s)
        
        while tmp :
            tt = tmp.pop(0)
            if tt == '#' :
                if len(ans1) != 0 :
                    ans1.pop()
                
            else:
                ans1.append(tt)
        tmp = list(t)
        while tmp :
            tt = tmp.pop(0)
            if tt == '#' :
                if len(ans2) != 0 :
                    ans2.pop()
                
            else:
                ans2.append(tt)
        
        print(ans1, ans2)
        return ans1 == ans2