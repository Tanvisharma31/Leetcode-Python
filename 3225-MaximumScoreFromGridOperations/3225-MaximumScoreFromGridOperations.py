# Last updated: 29/04/2026, 15:50:22
1class Solution:
2    def maximumScore(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        if n == 1:
5            return 0
6        dp0 = [0] * (n + 1)
7        dp1 = [0] * (n + 1)
8        for j in range(1, n):
9            new_dp0 = [0] * (n + 1)
10            new_dp1 = [0] * (n + 1)
11            for i in range(n + 1):
12                prev = 0
13                curr = sum(grid[x][j] for x in range(i))
14                for y in range(n + 1):
15                    if y > 0 and y <= i:
16                        curr -= grid[y - 1][j]
17                    if j > 0 and y > i:
18                        prev += grid[y - 1][j - 1]
19                    new_dp0[y] = max(new_dp0[y], prev + dp0[i], dp1[i])
20                    new_dp1[y] = max(new_dp1[y], curr + dp1[i], curr + prev + dp0[i])
21            dp0, dp1 = new_dp0, new_dp1
22        return max(dp1)