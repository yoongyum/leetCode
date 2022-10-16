class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            tmp = ''
            for digit, group in itertools.groupby(s):
                tmp += str(len(list(group))) + digit
            s= tmp
        return s