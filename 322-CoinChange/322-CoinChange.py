# Last updated: 02/03/2026, 14:02:31
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            minval = amount + 1
            for j in coins:
                if j <= i:
                    minval = min(dp[i - j], minval)
            dp[i] = 1 + minval

        if dp[amount] == amount + 2:
            return -1
        return dp[amount]