class Solution:
    def countAsterisks(self, s: str) -> int:
        ls=s.split('|')[::2]
        ans=0
        for i in ls:
            ans+=i.count('*')
        return ans