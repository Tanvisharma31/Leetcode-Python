# Last updated: 5/8/2026, 4:17:27 PM
1class Solution:
2    N = 10**6 + 5
3    prime = [True] * N
4    prime[0] = prime[1] = False
5    
6    for i in range(2, 1001):
7        if prime[i]:
8            for j in range(i * i, N, i):
9                prime[j] = False
10
11    def minJumps(self, nums: List[int]) -> int:
12        n = len(nums)
13        limit = nums[0]
14        for c in nums:
15            limit = max(limit, c)
16
17        head = [-1] * (limit + 1)
18        nxt = [-1] * n
19        for i in range(n):
20            val = nums[i]
21            nxt[i] = head[val]
22            head[val] = i
23
24        dp = [-1] * n
25        dp[0] = 0
26        queue = deque([0])
27        seen = set()
28
29        while queue:
30            dq = queue.popleft()
31
32            if dq == n - 1:
33                return dp[dq]
34
35            right = dq + 1
36            if right < n and dp[right] == -1:
37                dp[right] = dp[dq] + 1
38                queue.append(right)
39
40            left = dq - 1
41            if left >= 0 and dp[left] == -1:
42                dp[left] = dp[dq] + 1
43                queue.append(left)
44
45            val = nums[dq]
46            if Solution.prime[val] and val not in seen:
47                seen.add(val)
48                for i in range(val, limit + 1, val):
49                    j = head[i]
50                    while j != -1:
51                        if dp[j] == -1:
52                            dp[j] = dp[dq] + 1
53                            queue.append(j)
54                        j = nxt[j]
55                    head[i] = -1
56        return -1