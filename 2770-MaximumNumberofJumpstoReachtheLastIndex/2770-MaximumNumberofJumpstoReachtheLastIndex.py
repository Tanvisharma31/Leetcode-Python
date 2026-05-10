# Last updated: 5/10/2026, 12:11:17 PM
1class Solution:
2    def maximumJumps(self, nums: List[int], target: int) -> int:
3        @cache
4        def dfs(i: int):
5            if i == len(nums) - 1:
6                return 0
7
8            res = -inf
9            for j in range(i + 1, len(nums)):
10                if abs(nums[i] - nums[j]) <= target:
11                    res = max(res, dfs(j) + 1)
12            return res
13
14        ans = dfs(0)
15        return -1 if ans < 0 else ans