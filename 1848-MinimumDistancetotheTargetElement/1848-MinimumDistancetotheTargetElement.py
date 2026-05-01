# Last updated: 01/05/2026, 11:48:15
1class Solution:
2    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
3
4        if nums[start] == target:
5            return 0
6
7        n = len(nums)
8        d = 1
9
10        while True:
11            if start - d >= 0 and nums[start - d] == target:
12                return d
13
14            if start + d < n and nums[start + d] == target:
15                return d
16
17            d += 1