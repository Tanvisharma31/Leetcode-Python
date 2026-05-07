# Last updated: 5/7/2026, 12:48:57 PM
1class Solution:
2    def maxValue(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        if n == 0: return []
5
6        suffix_min = [0] * n
7        suffix_min[n - 1] = nums[n - 1]
8        for i in range(n - 2, -1, -1):
9            suffix_min[i] = min(suffix_min[i + 1], nums[i])
10
11        res = [0] * n
12        prefix_max = float('-inf')
13        chunk_start = 0
14
15        for i in range(n):
16            prefix_max = max(prefix_max, nums[i])
17
18            if i == n - 1 or prefix_max <= suffix_min[i + 1]:
19                for j in range(chunk_start, i + 1):
20                    res[j] = prefix_max
21                chunk_start = i + 1
22                prefix_max = float('-inf')
23
24        return res