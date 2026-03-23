# Last updated: 23/03/2026, 18:34:44
1class Solution:
2    def maxProductPath(self, grid: List[List[int]]) -> int:
3        r, c, MOD=len(grid), len(grid[0]), 10**9+7
4        dp=[[[0]*2 for _ in range(c)] for _ in range(r)]
5
6        p=dp[0][0][0]=dp[0][0][1]=grid[0][0]
7        for j in range(1, c):
8            p*=grid[0][j]
9            dp[0][j][0]=dp[0][j][1]=p
10
11        p=grid[0][0]
12        for i in range(1, r):
13            p*=grid[i][0]
14            dp[i][0][0]=dp[i][0][1]=p
15            for j in range(1, c):
16                x=grid[i][j]
17                xx=(x*dp[i][j-1][0], x*dp[i][j-1][1], x*dp[i-1][j][0], x*dp[i-1][j][1])
18                dp[i][j][0], dp[i][j][1]=min(xx), max(xx)
19        ans=dp[r-1][c-1][1]
20        return -1 if ans<0 else ans%MOD