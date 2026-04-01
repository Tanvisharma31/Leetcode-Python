# Last updated: 01/04/2026, 20:43:15
1class Solution:
2    def canPartitionGrid(self, grid):
3        m, n = len(grid), len(grid[0])
4
5        total = 0
6        bottom = defaultdict(int)
7        top = defaultdict(int)
8        left = defaultdict(int)
9        right = defaultdict(int)
10
11        # Initialize bottom and right maps
12        for row in grid:
13            for x in row:
14                total += x
15                bottom[x] += 1
16                right[x] += 1
17
18        sumTop = 0
19
20        # Horizontal cuts
21        for i in range(m - 1):
22            for j in range(n):
23                val = grid[i][j]
24                sumTop += val
25
26                top[val] += 1
27                bottom[val] -= 1
28
29            sumBottom = total - sumTop
30
31            if sumTop == sumBottom:
32                return True
33
34            diff = abs(sumTop - sumBottom)
35
36            if sumTop > sumBottom:
37                if self.check(top, grid, 0, i, 0, n - 1, diff):
38                    return True
39            else:
40                if self.check(bottom, grid, i + 1, m - 1, 0, n - 1, diff):
41                    return True
42
43        sumLeft = 0
44
45        # Vertical cuts
46        for j in range(n - 1):
47            for i in range(m):
48                val = grid[i][j]
49                sumLeft += val
50
51                left[val] += 1
52                right[val] -= 1
53
54            sumRight = total - sumLeft
55
56            if sumLeft == sumRight:
57                return True
58
59            diff = abs(sumLeft - sumRight)
60
61            if sumLeft > sumRight:
62                if self.check(left, grid, 0, m - 1, 0, j, diff):
63                    return True
64            else:
65                if self.check(right, grid, 0, m - 1, j + 1, n - 1, diff):
66                    return True
67
68        return False
69
70    def check(self, mp, grid, r1, r2, c1, c2, diff):
71        rows = r2 - r1 + 1
72        cols = c2 - c1 + 1
73
74        # single cell
75        if rows * cols == 1:
76            return False
77
78        # 1D row
79        if rows == 1:
80            return grid[r1][c1] == diff or grid[r1][c2] == diff
81
82        # 1D column
83        if cols == 1:
84            return grid[r1][c1] == diff or grid[r2][c1] == diff
85
86        return mp.get(diff, 0) > 0