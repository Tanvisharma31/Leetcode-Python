# Last updated: 25/03/2026, 13:24:12
1class Solution:
2    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
3        m, n = len(grid), len(grid[0])
4        rowSum = [0] * n
5        colSum = [0] * m
6        total = 0
7
8        for i in range(m):
9            for j in range(n):
10                rowSum[j] += grid[i][j]
11                colSum[i] += grid[i][j]
12                total += grid[i][j]
13
14        if total % 2 != 0:
15            return False
16
17        currSum = 0
18        for i in range(m):
19            currSum += colSum[i]
20            if total - currSum == currSum:
21                return True
22
23        currSum = 0
24        for j in range(n):
25            currSum += rowSum[j]
26            if total - currSum == currSum:
27                return True
28
29        return False