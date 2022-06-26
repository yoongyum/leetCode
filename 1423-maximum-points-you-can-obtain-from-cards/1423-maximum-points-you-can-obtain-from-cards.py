class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        sm=sum(card[:k])
        mx=sm
        for i in range(1,k+1):
            sm=sm+card[-i]-card[k-i]
            mx=max(mx,sm)
        return mx
        