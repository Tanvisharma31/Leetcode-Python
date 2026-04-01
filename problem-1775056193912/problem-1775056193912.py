# Last updated: 01/04/2026, 20:39:53
1class Solution:
2    def survivedRobotsHealths(self, positions, healths, directions):
3
4        n = len(positions)
5        order = sorted(range(n), key=lambda i: positions[i])
6
7        h = healths[:]
8        alive = [True]*n
9        stack = []
10
11        for idx in order:
12
13            if directions[idx] == 'R':
14                stack.append(idx)
15
16            else:
17                while stack:
18
19                    top = stack[-1]
20
21                    if h[top] < h[idx]:
22                        alive[top] = False
23                        stack.pop()
24                        h[idx] -= 1
25
26                    elif h[top] > h[idx]:
27                        alive[idx] = False
28                        h[top] -= 1
29                        break
30
31                    else:
32                        alive[top] = False
33                        alive[idx] = False
34                        stack.pop()
35                        break
36
37        return [h[i] for i in range(n) if alive[i]]