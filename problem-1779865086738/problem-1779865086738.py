# Last updated: 5/27/2026, 12:28:06 PM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        A = [[False, False] for _ in range(27)]
4
5        for ch in word:
6            i = ord(ch) & 31
7            c = ord(ch) >> 5 & 1
8            A[i][c] = not (c and A[i][0])
9
10        return sum(u and v for u, v in A)