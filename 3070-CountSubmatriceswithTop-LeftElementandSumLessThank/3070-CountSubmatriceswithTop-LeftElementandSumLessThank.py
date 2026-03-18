# Last updated: 18/03/2026, 14:43:28
1class Solution:
2    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
3        r, c=len(grid), len(grid[0])
4        cnt, brCol=0, c
5        if grid[0][0]>k:
6            return 0
7        cnt+=1
8        for j in range(1, c):
9            grid[0][j]+=grid[0][j-1]
10            if grid[0][j]>k:
11                brCol=j
12                break
13            cnt+=1
14        for i in range(1, r):
15            grid[i][0]+=grid[i-1][0]
16            if grid[i][0]>k:
17                break
18            cnt+=1
19            for j in range(1, brCol):
20                grid[i][j]+=grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1]
21                if grid[i][j]>k:
22                    brCol=j
23                    break
24                cnt+=1
25        return cnt