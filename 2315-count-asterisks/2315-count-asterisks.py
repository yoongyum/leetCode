class Solution:
    def countAsterisks(self, s: str) -> int:
        stack= False;
        answer = 0;
        for i in range(len(s)):
            if s[i] == '|':
                stack = not stack
            if s[i] == '*' and stack == False:
                answer+=1
        return answer