# Last updated: 15/04/2026, 17:36:43
1class Solution:
2    def closestTarget(self, words: List[str], target: str, s: int) -> int:
3        n = len(words)
4        for i in range((n >> 1) + 1):
5            if ((words[(s + i) % n] == target) |
6                (words[(s - i) % n] == target)):
7                return i
8        return -1