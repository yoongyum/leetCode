class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        d = {}
        c = 0
        res = 0
        for i in s:
            d[i]=d.get(i, 0)+1
        f=0
        for i in d:
            c+=d[i]//2 * 2
            if d[i]%2 != 0 and f==0:
                c=c-(d[i]//2 * 2)
                c+=d[i]
                f=1
        
        return c
        