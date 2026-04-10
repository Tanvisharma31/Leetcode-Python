# Last updated: 10/04/2026, 13:05:33
1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        n = len(nums)
4        last2 = [0] * n
5        res = 200
6
7        for i in range(n):
8            val, pos = nums[i] - 1, i + 1
9            pack = last2[val]
10            old, cur = pack & 255, pack >> 8
11
12            last2[val] = cur | (pos << 8)
13
14            if old:
15                res = min(res, (pos - old) << 1)
16
17        return -(res == 200) | res