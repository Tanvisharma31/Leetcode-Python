# Last updated: 26/04/2026, 13:04:35
1class Solution:
2    def containsCycle(self, grid: List[List[str]]) -> bool:
3        m, n = len(grid), len(grid[0])
4        visit = [False] * (m * n)
5        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
6
7        def dfs(r, c, pr, pc):
8            visit[r * n + c] = True
9
10            for dr, dc in dirs:
11                nr, nc = r + dr, c + dc
12
13                if (nr, nc) != (pr, pc):
14                    if 0 <= nr < m and 0 <= nc < n:
15                        if grid[nr][nc] == grid[r][c]:
16                            if visit[nr * n + nc] or dfs(nr, nc, r, c):
17                                return True
18
19            return False
20
21        return any(not visit[i] and dfs(i // n, i % n, -1, -1) for i in range(m * n))