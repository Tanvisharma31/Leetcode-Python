# Last updated: 05/03/2026, 17:13:06
1class Solution:
2    def minOperations(self, s: str) -> int:
3        c, j, n = 0, 0, len(s)
4        for ch in s:
5            if int(ch) == j:
6                c += 1
7            j ^= 1
8        return min(c, n - c)