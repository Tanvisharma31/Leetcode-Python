# Last updated: 5/20/2026, 12:54:34 PM
1class Solution:
2    def findThePrefixCommonArray(self, A, B):
3        n = len(A)
4
5        freq = [0] * (n + 1)
6        ans = [0] * n
7
8        cnt = 0
9
10        for i in range(n):
11
12            freq[A[i]] += 1
13            if freq[A[i]] == 2:
14                cnt += 1
15
16            freq[B[i]] += 1
17            if freq[B[i]] == 2:
18                cnt += 1
19
20            ans[i] = cnt
21
22        return ans