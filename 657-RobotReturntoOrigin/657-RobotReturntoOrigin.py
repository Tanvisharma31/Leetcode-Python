# Last updated: 05/04/2026, 15:35:39
1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        if len(moves) & 1: return False
4        x, y = [0, 0]
5
6        move = {
7            'U': (0, 1),
8            'D': (0, -1),
9            'L': (-1, 0),
10            'R': (1, 0),
11        }
12
13        for c in moves:
14            dx, dy = move[c]
15            x += dx
16            y += dy
17
18        return [x, y] == [0, 0]