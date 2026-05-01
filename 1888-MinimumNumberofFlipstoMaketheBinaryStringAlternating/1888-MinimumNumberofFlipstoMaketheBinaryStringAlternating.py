# Last updated: 01/05/2026, 11:53:18
1class Solution:
2    def minFlips(self, s: str) -> int:
3        n = len(s)
4        res = n
5        op = [0, 0]
6
7        for i in range(n):
8            op[(ord(s[i]) ^ i) & 1] += 1
9
10        for i in range(n):
11            c = ord(s[i])
12            op[(c ^ i) & 1] -= 1
13            op[(c ^ (n + i)) & 1] += 1
14            res = min(res, min(op))
15
16        return res
17