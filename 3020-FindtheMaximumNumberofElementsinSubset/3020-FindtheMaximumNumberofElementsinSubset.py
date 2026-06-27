# Last updated: 6/27/2026, 3:13:27 PM
1class Solution:
2    def maximumLength(self, nums: list[int]) -> int:
3        freq = Counter(nums)
4        res = (freq.pop(1, 0) - 1) | 1
5
6        for f in freq:
7            x = f
8            sq = isqrt(x)
9            if sq * sq == x and freq.get(sq, 0) > 1:
10                continue
11
12            n = 0
13            while x < 31623 and freq.get(x, 0) > 1:
14                n += 2
15                x *= x
16
17            res = max(res, n + ((x in freq) << 1) - 1)
18
19        return res