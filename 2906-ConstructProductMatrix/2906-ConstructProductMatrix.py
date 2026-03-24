# Last updated: 24/03/2026, 18:01:18
1
2class Solution:
3    def constructProductMatrix(self, grid):
4        MOD = 12345
5        n, m = len(grid), len(grid[0])
6        p = [[0]*m for _ in range(n)]
7
8        suffix = 1
9        for i in range(n-1, -1, -1):
10            for j in range(m-1, -1, -1):
11                p[i][j] = suffix
12                suffix = (suffix * (grid[i][j] % MOD)) % MOD
13
14        prefix = 1
15        for i in range(n):
16            for j in range(m):
17                p[i][j] = (p[i][j] * prefix) % MOD
18                prefix = (prefix * (grid[i][j] % MOD)) % MOD
19
20        return p