class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = 'aeoiuAEOIU'
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            while l < r and s[l] not in arr:
                l += 1
            while l < r and s[r]not in  arr:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1   ;   r -= 1    
        
        return ''.join(s)