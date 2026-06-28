# Last updated: 6/28/2026, 5:04:33 PM
1class Solution:
2    def maximumElementAfterDecrementingAndRearranging(self, A: list[int]) -> int:
3        A.sort()
4        n = len(A)
5
6        A[0] = 1
7        for i in range(1, n):
8            A[i] = min(A[i], A[i - 1] + 1)
9            
10        return A[-1]