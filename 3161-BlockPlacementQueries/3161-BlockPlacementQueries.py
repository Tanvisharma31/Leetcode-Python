# Last updated: 5/30/2026, 7:50:13 AM
1import bisect
2
3class MaxSegmentTree:
4    def __init__(self, size: int):
5        self.n = size
6        self.tree = [0] * (4 * size)
7
8    def update(self, index: int, value: int, node: int, start: int, end: int):
9        if index < start or index > end:
10            return
11        if start == end:
12            self.tree[node] = value
13            return
14        mid = (start + end) // 2
15        if index <= mid:
16            self.update(index, value, 2 * node, start, mid)
17        else:
18            self.update(index, value, 2 * node + 1, mid + 1, end)
19        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
20
21    def query(self, l: int, r: int, node: int, start: int, end: int) -> int:
22        if l > end or r < start:
23            return 0
24        if l <= start and end <= r:
25            return self.tree[node]
26        mid = (start + end) // 2
27        p1 = self.query(l, r, 2 * node, start, mid)
28        p2 = self.query(l, r, 2 * node + 1, mid + 1, end)
29        return max(p1, p2)
30
31
32class Solution:
33    def getResults(self, queries: list[list[int]]) -> list[bool]:
34        # 1. Dynamically bound the maximum dimension
35        max_x = max(q[1] for q in queries)
36        
37        seg_tree = MaxSegmentTree(max_x + 1)
38        # Use a safe infinity bound for the right edge to avoid tree array overflows
39        obstacles = [0, float('inf')]
40        
41        results = []
42        
43        for q in queries:
44            if q[0] == 1:
45                x = q[1]
46                
47                idx = bisect.bisect_left(obstacles, x)
48                if obstacles[idx] == x:
49                    continue
50                    
51                left = obstacles[idx - 1]
52                right = obstacles[idx]
53                
54                bisect.insort(obstacles, x)
55                
56                # Update the new left-hand gap split
57                seg_tree.update(x, x - left, 1, 0, max_x)
58                
59                # Only update the right-hand gap if it falls within our tracked coordinate image space
60                if right <= max_x:
61                    seg_tree.update(right, right - x, 1, 0, max_x)
62                
63            elif q[0] == 2:
64                target_x = q[1]
65                required_sz = q[2]
66                
67                idx = bisect.bisect_right(obstacles, target_x) - 1
68                last_obstacle = obstacles[idx]
69                
70                # Query the maximum gap up to the last obstacle safely within bounds
71                max_available_gap = seg_tree.query(0, last_obstacle, 1, 0, max_x)
72                
73                # Capture the trailing residual space up to target_x
74                residual_gap = target_x - last_obstacle
75                
76                final_boundary_max = max(max_available_gap, residual_gap)
77                
78                results.append(bool(final_boundary_max >= required_sz))
79                
80        return results