class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                dp[i] = min(dp[i], dp[i-c]+1 if i>=c else float('inf'))
        return dp[-1] if dp[-1] != float('inf') else -1
