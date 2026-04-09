# Last updated: 09/04/2026, 13:00:52
1class Solution:
2    MOD = 10**9 + 7
3
4    def modpow(self, a: int, e: int) -> int:
5        r = 1
6        a %= self.MOD
7        while e:
8            if e & 1:
9                r = (r * a) % self.MOD
10            a = (a * a) % self.MOD
11            e >>= 1
12        return r
13
14    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
15        n = len(nums)
16        B = int(math.sqrt(n)) + 1
17
18        # events[k][rem] = list of (position, multiplier)
19        events = [[] for _ in range(B + 1)]
20        for k in range(1, B + 1):
21            events[k] = [[] for _ in range(k)]
22
23        # Process queries
24        for l, r, k, v in queries:
25            if k > B:
26                # direct update
27                i = l
28                while i <= r:
29                    nums[i] = (nums[i] * v) % self.MOD
30                    i += k
31            else:
32                rem = l % k
33                start = (l - rem) // k
34                end = (r - rem) // k
35
36                events[k][rem].append((start, v))
37
38                maxT = (n - 1 - rem) // k
39                if end + 1 <= maxT:
40                    inv = self.modpow(v, self.MOD - 2)
41                    events[k][rem].append((end + 1, inv))
42
43        # Apply small k events
44        for k in range(1, B + 1):
45            for rem in range(k):
46                ev = events[k][rem]
47                if not ev:
48                    continue
49
50                # sort events
51                ev.sort()
52
53                # compress same positions
54                comp = []
55                for t, val in ev:
56                    if comp and comp[-1][0] == t:
57                        comp[-1] = (t, comp[-1][1] * val % self.MOD)
58                    else:
59                        comp.append((t, val))
60
61                # apply prefix multiplication
62                cur = 1
63                ptr = 0
64                t = 0
65                idx = rem
66
67                while idx < n:
68                    while ptr < len(comp) and comp[ptr][0] == t:
69                        cur = (cur * comp[ptr][1]) % self.MOD
70                        ptr += 1
71
72                    nums[idx] = nums[idx] * cur % self.MOD
73
74                    t += 1
75                    idx += k
76
77        # Compute XOR
78        ans = 0
79        for x in nums:
80            ans ^= x
81
82        return ans