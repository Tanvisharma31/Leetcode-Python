# Last updated: 14/04/2026, 11:35:51
1class Solution:
2    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
3        robot.sort()
4        factory.sort()
5
6        n, m = len(robot), len(factory)
7        INF = float('inf')
8
9        dp = [[INF]*(m+1) for _ in range(n+1)]
10
11        for j in range(m+1):
12            dp[0][j] = 0
13
14        for j in range(1, m+1):
15            pos, limit = factory[j-1]
16
17            for i in range(n+1):
18                dp[i][j] = dp[i][j-1]
19
20                dist = 0
21                for k in range(1, min(limit, i)+1):
22                    dist += abs(robot[i-k] - pos)
23                    dp[i][j] = min(dp[i][j], dp[i-k][j-1] + dist)
24
25        return dp[n][m]