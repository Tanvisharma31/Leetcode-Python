# Last updated: 5/30/2026, 8:46:59 AM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s)!=len(t):
4            return False
5        s=sorted(s)
6        t=sorted(t)
7        for c1,c2 in zip(s,t):
8            if c1!=c2:
9                return False
10        return True