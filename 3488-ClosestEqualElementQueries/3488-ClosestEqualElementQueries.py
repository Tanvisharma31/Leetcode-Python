# Last updated: 16/04/2026, 15:29:08
1class Solution:
2    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
3        n = len(nums)
4        mp = defaultdict(list)
5
6        # store indices
7        for i in range(n):
8            mp[nums[i]].append(i)
9
10        ans = []
11
12        for q in queries:
13            v = mp[nums[q]]
14
15            # only one time present
16            if len(v) == 1:
17                ans.append(-1)
18                continue
19
20            pos = bisect_left(v, q)
21            res = float('inf')
22
23            # left neighbor
24            left = v[(pos - 1) % len(v)]
25            d1 = abs(q - left)
26            res = min(res, min(d1, n - d1))
27
28            # right neighbor
29            right = v[(pos + 1) % len(v)]
30            d2 = abs(q - right)
31            res = min(res, min(d2, n - d2))
32
33            ans.append(res)
34
35        return ans