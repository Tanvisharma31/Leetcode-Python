# Last updated: 7/1/2026, 8:57:34 PM
1class Solution:
2    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
3
4    def maximumSafenessFactor(self, A: List[List[int]]) -> int:
5        if A[0][0] or A[-1][-1]: return 0
6        n, q = len(A), deque()
7
8        for i in range(n):
9            for j in range(n):
10                if A[i][j]:
11                    q.append((i, j))
12
13        while q:
14            i, j = q.popleft()
15            v = A[i][j]
16
17            for dx, dy in self.dirs:
18                x, y = i + dx, j + dy
19
20                if min(x, y) >= 0 and max(x, y) < n and not A[x][y]:
21                    A[x][y] = v + 1
22                    q.append((x, y))
23
24        pq = [(-A[0][0], 0, 0)]
25
26        while pq:
27            sf, i, j = heapq.heappop(pq)
28            sf = -sf
29
30            if i == n - 1 and j == n - 1:
31                return sf - 1
32
33            for dx, dy in self.dirs:
34                x, y = i + dx, j + dy
35
36                if min(x, y) >= 0 and max(x, y) < n and A[x][y] > 0:
37                    heapq.heappush(pq, (-min(sf, A[x][y]), x, y))
38                    A[x][y] *= -1
39
40        return A[n - 1][n - 1] - 1