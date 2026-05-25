# Last updated: 5/25/2026, 1:42:10 PM
1class Solution:
2    def findTheDifference(self, s: str, t: str) -> str:
3        for i in t:
4            if i in s:
5                s = s.replace(i,"",1)
6            else:
7                return i
8