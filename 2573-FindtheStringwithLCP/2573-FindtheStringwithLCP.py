# Last updated: 01/04/2026, 20:41:53
1class Solution:
2    def findTheString(self, lcp: List[List[int]]) -> str:
3        n = len(lcp)
4        word = [""] * n
5        current = ord("a")
6
7        for i in range(n):
8            if not word[i]:
9                if current > ord("z"):
10                    return ""
11                word[i] = chr(current)
12                for j in range(i + 1, n):
13                    if lcp[i][j]:
14                        word[j] = word[i]
15                current += 1
16
17        for i in range(n - 1, -1, -1):
18            for j in range(n - 1, -1, -1):
19                if word[i] != word[j]:
20                    if lcp[i][j]:
21                        return ""
22                else:
23                    if i == n - 1 or j == n - 1:
24                        if lcp[i][j] != 1:
25                            return ""
26                    else:
27                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
28                            return ""
29
30        return "".join(word)