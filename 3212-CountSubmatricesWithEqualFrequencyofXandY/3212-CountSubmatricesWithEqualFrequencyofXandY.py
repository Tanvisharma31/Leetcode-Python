# Last updated: 19/03/2026, 11:41:59
1class Solution:
2    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
3        m = len(grid)
4        n = len(grid[0])
5        res = 0
6        ox = [0] * n
7        oy = [0] * n
8        for i in range(m):
9            rowx, rowy = 0, 0
10            for j in range(n):
11                if grid[i][j] == 'X':
12                    rowx += 1
13                elif grid[i][j] == 'Y':
14                    rowy += 1
15                ox[j] += rowx
16                oy[j] += rowy
17                if ox[j] == oy[j] and ox[j] > 0:
18                    res += 1
19        return res