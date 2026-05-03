# Last updated: 5/3/2026, 2:43:25 PM
1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        return len(s) == len(goal) and goal in s + s