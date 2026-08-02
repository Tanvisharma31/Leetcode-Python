# Last updated: 8/2/2026, 5:19:15 PM
1class Solution:
2    def predictTheWinner(self, A: List[int]) -> bool:
3        n = len(A)
4        if ~n & 1: return True
5
6        @cache
7        def maxDiff(i: int, j: int) -> int:
8            if i == j: return A[i]
9            return max(A[i] - maxDiff(i + 1, j),
10                       A[j] - maxDiff(i, j - 1))
11
12        return maxDiff(0, n - 1) >= 0