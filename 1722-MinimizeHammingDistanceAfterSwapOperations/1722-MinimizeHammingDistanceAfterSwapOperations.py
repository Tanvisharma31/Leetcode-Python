# Last updated: 21/04/2026, 11:48:10
1class Solution:
2    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
3        n = len(source)
4        parent = list(range(n))
5        rank = [0] * n
6
7        def find(x):
8            if parent[x] != x:
9                parent[x] = find(parent[x])
10            return parent[x]
11
12        def uni(a, b):
13            fa, fb = find(a), find(b)
14            if fa == fb:
15                return
16
17            if rank[fa] < rank[fb]:
18                fa, fb = fb, fa
19
20            parent[fb] = fa
21            if rank[fa] == rank[fb]:
22                rank[fa] += 1
23
24        for a, b in allowedSwaps:
25            uni(a, b)
26
27        groups = defaultdict(list)
28        for i in range(n):
29            groups[find(i)].append(i)
30
31        ans = 0
32
33        for idxs in groups.values():
34            freq = {}
35
36            for i in idxs:
37                freq[source[i]] = freq.get(source[i], 0) + 1
38
39            for i in idxs:
40                if freq.get(target[i], 0) > 0:
41                    freq[target[i]] -= 1
42                else:
43                    ans += 1
44
45        return ans