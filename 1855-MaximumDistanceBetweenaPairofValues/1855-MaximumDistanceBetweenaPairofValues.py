# Last updated: 19/04/2026, 17:38:05
1class Solution:
2    def maxDistance(self, A: List[int], B: List[int]) -> int:
3        i, j = 0, 1
4
5        while i < len(A) and j < len(B):
6            i += A[i] > B[j]
7            j += 1
8
9        return j - i - 1