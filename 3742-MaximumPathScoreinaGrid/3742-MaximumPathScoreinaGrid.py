# Last updated: 30/04/2026, 12:31:31
1from typing import List
2
3class Solution:
4    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
5        m = len(grid)
6        n = len(grid[0])
7        NEG = -10**9
8
9        prev = [[NEG] * (k + 1) for _ in range(n)]
10
11        for i in range(m):
12            curr = [[NEG] * (k + 1) for _ in range(n)]
13
14            for j in range(n):
15                gain = grid[i][j]
16                need = 1 if gain > 0 else 0
17
18                limit = min(k, i + j)
19
20                if i == 0 and j == 0:
21                    curr[0][0] = 0
22                    continue
23
24                for c in range(need, limit + 1):
25                    best = NEG
26
27                    if i > 0 and prev[j][c - need] != NEG:
28                        best = max(best, prev[j][c - need] + gain)
29
30                    if j > 0 and curr[j - 1][c - need] != NEG:
31                        best = max(best, curr[j - 1][c - need] + gain)
32
33                    curr[j][c] = best
34
35            prev = curr
36
37        ans = max(prev[n - 1])
38        return -1 if ans < 0 else ans