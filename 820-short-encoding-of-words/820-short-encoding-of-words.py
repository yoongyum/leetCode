class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x : x[::-1],reverse = True)
        res = 0
        last = words.pop(0)
        for x in words:
            if not last.endswith(x):
                res += len(last) + 1
                last = x
        return len(last) + res + 1
        