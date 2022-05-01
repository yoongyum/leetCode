class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        num = list(number)
        ans = -1
        for i,n in enumerate(num):
            if n == digit:
                tmp = deepcopy(num)
                tmp.pop(i)
                ans = max(int(''.join(tmp)), ans)
                
        return str(ans)
        