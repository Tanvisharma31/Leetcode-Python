# Last updated: 27/04/2026, 11:50:46
1class Solution:
2    TRANS = [
3        [-1, 1, -1, 3],
4        [0, -1, 2, -1],
5        [3, 2, -1, -1],
6        [1, -1, -1, 2],
7        [-1, 0, 3, -1],
8        [-1, -1, 1, 0]
9    ]
10    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
11    START = [[1, 3], [0, 2], [2, 3], [1, 2], [0, 3], [0, 1]]
12
13    def hasValidPath(self, grid: List[List[int]]) -> bool:
14        if grid[0][0] == 5: return False
15        if grid[-1][-1] == 4: return False
16        
17        m, n = len(grid), len(grid[0])
18        if m == 1 and n == 1: return True
19
20        def check(d):
21            if d == -1: return False
22            r, c = self.DIRS[d]
23            # O(1) Space
24            while 0 <= r < m and 0 <= c < n:               
25                d = self.TRANS[grid[r][c] - 1][d]
26                if d == -1: return False
27                if r == 0 and c == 0: return False
28                if r == m - 1 and c == n - 1: return True
29                
30                dr, dc = self.DIRS[d] 
31                r += dr
32                c += dc
33            return False
34
35        a, b = self.START[grid[0][0] - 1]
36        return check(a) or check(b)