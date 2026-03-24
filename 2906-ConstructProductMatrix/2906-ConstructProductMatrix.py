# Last updated: 24/03/2026, 18:02:27
1class Solution:
2    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
3        """
4        n = len(grid)
5        m = len(grid[0])
6        zero = 0
7        total = 1
8        mod = 12345
9        for i in range(n):
10            for j in range(m):
11                grid[i][j] %= mod
12                if grid[i][j] == 0:
13                    zero += 1
14                else:
15                    total = total * grid[i][j]
16
17        for i in range(n):
18            for j in range(m):
19                if zero > 1:
20                    grid[i][j] = 0
21                elif zero == 1:
22                    if grid[i][j]:
23                        grid[i][j] = 0
24                    else:
25                        grid[i][j] = total % mod
26                else:
27                    grid[i][j] = (total // grid[i][j]) % mod
28        return grid
29        """
30        
31        
32        n = len(grid)
33        m = len(grid[0])
34        zero = 0
35        total = 1
36        dp = [[0] * m for _ in range(n)]
37        for i in range(n - 1, -1, -1):
38            for j in range(m - 1, -1, -1):
39                dp[i][j] = total
40                total = (total * grid[i][j]) % 12345
41        total = 1
42        for i in range(n):
43            for j in range(m):
44                dp[i][j] = (dp[i][j] * total) % 12345
45                total = (total * grid[i][j]) % 12345
46        return dp