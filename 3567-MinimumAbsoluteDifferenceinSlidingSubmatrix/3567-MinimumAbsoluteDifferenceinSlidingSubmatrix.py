# Last updated: 20/03/2026, 13:19:54
1# Added using AI
2class Solution:
3    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
4        m, n = len(grid), len(grid[0])
5        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
6
7        for i in range(m - k + 1):
8            for j in range(n - k + 1):
9                v = sorted(set(
10                    grid[x][y]
11                    for x in range(i, i + k)
12                    for y in range(j, j + k)
13                ))
14                if len(v) <= 1:
15                    ans[i][j] = 0
16                else:
17                    ans[i][j] = min(v[p+1] - v[p] for p in range(len(v) - 1))
18
19        return ans