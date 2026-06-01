# Last updated: 6/1/2026, 12:04:24 PM
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        res = []
4
5        for n in range(numRows):
6            row = []
7
8            val = 1
9            row.append(val)
10
11            for k in range(1, n + 1):
12                val = val * (n - k + 1) // k
13                row.append(val)
14
15            res.append(row)
16
17        return res