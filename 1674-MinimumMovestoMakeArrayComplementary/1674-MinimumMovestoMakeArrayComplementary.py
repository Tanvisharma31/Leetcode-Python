# Last updated: 5/13/2026, 1:54:00 PM
1class Solution:
2    def minMoves(self, nums, limit):
3        n = len(nums)
4
5        diff = [0] * (2 * limit + 2)
6
7        for i in range(n // 2):
8
9            a = nums[i]
10            b = nums[n - i - 1]
11
12            if a > b:
13                a, b = b, a
14
15            summ = a + b
16
17            left = a + 1
18            right = b + limit
19
20            # Assume 2 moves for all sums
21            diff[2] += 2
22            diff[2 * limit + 1] -= 2
23
24            # 1 move range
25            diff[left] -= 1
26            diff[right + 1] += 1
27
28            # 0 move point
29            diff[summ] -= 1
30            diff[summ + 1] += 1
31
32        res = float('inf')
33        curr = 0
34
35        for s in range(2, 2 * limit + 1):
36            curr += diff[s]
37            res = min(res, curr)
38
39        return res