# Last updated: 18/04/2026, 16:18:07
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        rev, x=0, n
4        while x>0:
5            x, r=divmod(x, 10)
6            rev=10*rev+r
7        return abs(rev-n)
8        