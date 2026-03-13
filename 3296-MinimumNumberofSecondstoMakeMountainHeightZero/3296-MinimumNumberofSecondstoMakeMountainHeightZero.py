# Last updated: 13/03/2026, 19:12:33
1class Solution:
2    def minNumberOfSeconds(self, height: int, times: list[int]) -> int:
3        lo, hi = 1, 10**16
4
5        while lo < hi:
6            mid = (lo + hi) >> 1
7            tot = 0
8            for t in times:
9                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
10                if tot >= height: break
11            if tot >= height:
12                hi = mid
13            else:
14                lo = mid + 1
15
16        return lo