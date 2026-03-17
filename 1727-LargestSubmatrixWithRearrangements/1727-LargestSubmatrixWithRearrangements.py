# Last updated: 17/03/2026, 09:41:10
1class Solution:
2    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
3        m = len(matrix)
4        n = len(matrix[0])
5        res = 0
6
7        for i in range(1, m):
8            for j in range(n):
9                if matrix[i][j] == 1:
10                    matrix[i][j] += matrix[i - 1][j]
11
12        for i in range(m):
13            matrix[i].sort(reverse=True)
14            for j in range(n):
15                res = max(res, matrix[i][j] * (j + 1))
16
17        return res