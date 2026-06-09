# Last updated: 6/9/2026, 9:29:33 AM
1class Solution:
2    def maxTotalValue(self, A: List[int], k: int) -> int:
3        return k*max(A) - k*min(A)