# Last updated: 06/04/2026, 17:14:16
1class Solution:
2    def robotSim(self, commands, obstacles):
3        # Store obstacles
4        blocked = set()
5        for o in obstacles:
6            blocked.add((o[0], o[1]))
7
8        # Directions: North, East, South, West
9        directions = [
10            (0, 1), (1, 0), (0, -1), (-1, 0)
11        ]
12
13        x, y = 0, 0
14        dir = 0  # initially facing North
15        maxDist = 0
16
17        for cmd in commands:
18            if cmd == -1:
19                dir = (dir + 1) % 4  # turn right
20            elif cmd == -2:
21                dir = (dir + 3) % 4  # turn left
22            else:
23                while cmd > 0:
24                    nx = x + directions[dir][0]
25                    ny = y + directions[dir][1]
26
27                    # check obstacle
28                    if (nx, ny) in blocked:
29                        break
30
31                    x = nx
32                    y = ny
33
34                    maxDist = max(maxDist, x * x + y * y)
35                    cmd -= 1
36
37        return maxDist