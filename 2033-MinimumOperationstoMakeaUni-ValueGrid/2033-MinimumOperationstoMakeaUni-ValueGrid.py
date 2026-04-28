# Last updated: 28/04/2026, 11:24:35
1class Solution:
2    def minOperations(self, grid: List[List[int]], x: int) -> int:
3        n, m = len(grid), len(grid[0])
4        N = n * m
5        freq = [0] * 10001
6        mn = grid[0][0]
7        mx = mn
8
9        for row in grid:
10            for c in row:
11                if (c - grid[0][0]) % x != 0: return -1
12                freq[c] += 1
13                mn = min(mn, c)
14                mx = max(mx, c)
15
16        target = (N + 1) // 2
17        acc = 0
18        median = mn
19
20        for i in range(mn, mx + 1, x):
21            acc += freq[i]
22            if acc >= target:
23                median = i
24                break
25
26        ops = 0
27        for i in range(mn, mx + 1, x):
28            ops += abs(i - median) // x * freq[i]
29
30        return ops