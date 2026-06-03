# Last updated: 6/3/2026, 1:35:12 PM
1class Solution:
2    def earliestFinishTime(
3        self, la: list[int], lb: list[int], wa: list[int], wb: list[int]
4    ) -> int:
5        MAX = 300005
6        l = w = minL = minW = MAX
7        n, m = len(la), len(wa)
8
9        for i in range(n):
10            l = min(l, la[i] + lb[i])
11
12        for i in range(m):
13            w = min(w, wa[i] + wb[i])
14            minL = min(minL, max(wa[i], l) + wb[i])
15
16        for i in range(n):
17            minW = min(minW, max(la[i], w) + lb[i])
18
19        return min(minW, minL)