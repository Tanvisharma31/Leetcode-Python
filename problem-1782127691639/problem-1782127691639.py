# Last updated: 6/22/2026, 4:58:11 PM
1class Solution:
2    def maxNumberOfBalloons(self, text: str) -> int:
3        f = Counter(text)
4        return min(f["b"], f["a"], f["l"] >> 1, f["o"] >> 1, f["n"])