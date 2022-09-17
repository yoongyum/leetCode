class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        st = deque(list(s))
        for i in t:
            if len(st) == 0:
                return True
            if st[0] == i:
                st.popleft()
        return len(st) == 0