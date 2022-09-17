class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for i in range(len(s)):   #record the index of the 2 strings and then compare
            s1.append(s.index(s[i]))
            s2.append(t.index(t[i]))
        return s1==s2
            