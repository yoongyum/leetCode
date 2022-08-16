class Solution:
    def firstUniqChar(self, s: str) -> int:
        A = [0] * 26
        for v in s: A[ord(v) - ord('a')] += 1
        
        for i, v in enumerate(s):
            if A[ord(v) - ord('a')] == 1:
                return i
        return -1
        