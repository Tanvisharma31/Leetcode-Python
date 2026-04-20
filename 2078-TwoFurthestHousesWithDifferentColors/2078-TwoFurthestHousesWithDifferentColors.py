# Last updated: 20/04/2026, 10:22:20
1class Solution:
2    def maxDistance(self, A: List[int]) -> int:
3        n = len(A)
4        left, right = 0, n - 1
5
6        for i in range(n):
7            if A[i] ^ A[-1]:
8                left = i
9                break
10
11        for i in range(n - 1, -1, -1):
12            if A[i] ^ A[0]:
13                right = i
14                break
15
16        return max(n - 1 - left, right)