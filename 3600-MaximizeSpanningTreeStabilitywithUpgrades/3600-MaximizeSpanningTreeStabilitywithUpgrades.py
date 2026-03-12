# Last updated: 12/03/2026, 14:08:52
1class Solution:
2    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
3        parent = list(range(n))
4
5        def find(i):
6            while i != parent[i]:
7                parent[i] = parent[parent[i]]
8                i = parent[i]
9            return i
10
11        min_m = float('inf')
12        comp_count = n
13
14        for u, v, w, must in edges:
15            if must == 1:
16                ru = find(u)
17                rv = find(v)
18                if ru == rv:
19                    return -1
20                parent[ru] = rv
21                comp_count -= 1
22                if w < min_m:
23                    min_m = w
24
25        opt = []
26        for u, v, w, must in edges:
27            if must == 0:
28                ru = find(u)
29                rv = find(v)
30                if ru != rv:
31                    # Packing: weight (30 bits) | ru (17 bits) | rv (17 bits)
32                    opt.append((w << 34) | (ru << 17) | rv)
33
34        if comp_count == 1:
35            return int(min_m)
36
37        # Radix Sort
38        if len(opt) > 1:
39            temp = [0] * len(opt)
40            for shift in range(34, 64, 8):
41                count = [0] * 256
42                for val in opt:
43                    count[(val >> shift) & 0xFF] += 1
44                for i in range(1, 256):
45                    count[i] += count[i - 1]
46                for i in range(len(opt) - 1, -1, -1):
47                    val = opt[i]
48                    idx = (val >> shift) & 0xFF
49                    count[idx] -= 1
50                    temp[count[idx]] = val
51                opt, temp = temp, opt
52
53        upg = []
54        for i in range(len(opt) - 1, -1, -1):
55            packed = opt[i]
56            ru = find((packed >> 17) & 0x1FFFF)
57            rv = find(packed & 0x1FFFF)
58            
59            if ru != rv:
60                parent[ru] = rv
61                upg.append(packed >> 34)
62                comp_count -= 1
63                if comp_count == 1:
64                    break
65
66        if comp_count > 1:
67            return -1
68
69        for i in range(len(upg) - 1, -1, -1):
70            if k > 0:
71                k -= 1
72                upgraded = upg[i] << 1
73                if upgraded < min_m:
74                    min_m = upgraded
75            else:
76                if upg[i] < min_m:
77                    min_m = upg[i]
78                break
79
80        return int(min_m)