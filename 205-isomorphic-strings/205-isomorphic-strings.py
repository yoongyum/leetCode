from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        shash = defaultdict(str)
        thash = defaultdict(str)
        for i in range(len(s)):  # 5*10_000
            if s[i] in shash:
                if shash[s[i]] != t[i]:
                    return False
            elif t[i] in thash:
                if thash[t[i]] != s[i]:
                    return False
            else:
                shash[s[i]] = t[i]
                thash[t[i]] = s[i]
    
        return True
            