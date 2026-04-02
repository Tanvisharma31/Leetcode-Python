# Last updated: 02/04/2026, 12:46:30
1class Solution:
2    def maximumAmount(self, coins: List[List[int]]) -> int:
3        n = len(coins[0])
4        dp = [[-inf] * 3 for _ in range(n + 1)]
5        dp[1] = [0] * 3
6        for row in coins:
7            for j, x in enumerate(row):
8                dp[j + 1][2] = max(dp[j][2] + x, dp[j + 1][2] + x, dp[j][1], dp[j + 1][1])
9                dp[j + 1][1] = max(dp[j][1] + x, dp[j + 1][1] + x, dp[j][0], dp[j + 1][0])
10                dp[j + 1][0] = max(dp[j][0], dp[j + 1][0]) + x
11        return dp[n][2]