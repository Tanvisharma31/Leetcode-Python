# Last updated: 01/05/2026, 11:41:57
1class Solution:
2    def maxRotateFunction(self, nums: List[int]) -> int:
3
4        n = len(nums)
5        total_sum = sum(nums)
6
7        f = sum(i * nums[i] for i in range(n))
8        max_val = f
9
10        for k in range(1, n):
11            f = f + total_sum - n * nums[n - k]
12            max_val = max(max_val, f)
13
14        return max_val