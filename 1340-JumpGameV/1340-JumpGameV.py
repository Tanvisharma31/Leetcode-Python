# Last updated: 5/24/2026, 1:53:02 PM
1class Solution:
2    def maxJumps(self, arr: list[int], d: int) -> int:
3        n = len(arr)
4        dp = [-1] * n
5
6        def dfs(i):
7            if dp[i] != -1:
8                return dp[i]
9
10            best = 1
11
12            # Right scan
13            for nxt in range(i + 1, min(n, i + d + 1)):
14                if arr[nxt] >= arr[i]:
15                    break
16
17                best = max(best, 1 + dfs(nxt))
18
19            # Left scan
20            for nxt in range(i - 1, max(-1, i - d - 1), -1):
21                if arr[nxt] >= arr[i]:
22                    break
23
24                best = max(best, 1 + dfs(nxt))
25
26            dp[i] = best
27            return dp[i]
28
29        return max(dfs(i) for i in range(n))