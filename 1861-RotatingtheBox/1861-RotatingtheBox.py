# Last updated: 5/6/2026, 12:52:00 PM
1class Solution:
2    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
3        rows, cols = len(grid), len(grid[0])
4        for r in range(rows):
5            p = 0
6            for c in range(cols):
7                if grid[r][c] == '.':
8                    grid[r][c], grid[r][p] = grid[r][p], grid[r][c]
9                    p += 1
10                elif grid[r][c] == '*':
11                    p = c + 1
12        
13        res = [[''] * rows for _ in range(cols)]
14        for r in range(rows):
15            for c in range(cols):
16                res[c][rows - 1 - r] = grid[r][c]
17                
18        return res