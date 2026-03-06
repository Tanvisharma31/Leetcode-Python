# Last updated: 06/03/2026, 21:29:41
1class Solution:
2    def checkOnesSegment(self, s: str) -> bool:
3        seen_zero = False
4
5        for c in s:
6            if c == '0':
7                seen_zero = True
8            elif seen_zero:
9                return False
10
11        return True