# Last updated: 03/04/2026, 13:07:56
1class Solution:
2    def maxWalls(
3        self, robots: List[int], distance: List[int], walls: List[int]
4    ) -> int:
5        n = len(robots)
6        left = [0] * n
7        right = [0] * n
8        num = [0] * n
9        robots_to_distance = {}
10
11        for i in range(n):
12            robots_to_distance[robots[i]] = distance[i]
13
14        robots.sort()
15        walls.sort()
16
17        for i in range(n):
18            pos1 = bisect.bisect_right(walls, robots[i])
19
20            if i >= 1:
21                left_bound = max(
22                    robots[i] - robots_to_distance[robots[i]], robots[i - 1] + 1
23                )
24                left_pos = bisect.bisect_left(walls, left_bound)
25            else:
26                left_pos = bisect.bisect_left(
27                    walls, robots[i] - robots_to_distance[robots[i]]
28                )
29
30            left[i] = pos1 - left_pos
31
32            if i < n - 1:
33                right_bound = min(
34                    robots[i] + robots_to_distance[robots[i]], robots[i + 1] - 1
35                )
36                right_pos = bisect.bisect_right(walls, right_bound)
37            else:
38                right_pos = bisect.bisect_right(
39                    walls, robots[i] + robots_to_distance[robots[i]]
40                )
41
42            pos2 = bisect.bisect_left(walls, robots[i])
43            right[i] = right_pos - pos2
44
45            if i == 0:
46                continue
47
48            pos3 = bisect.bisect_left(walls, robots[i - 1])
49            num[i] = pos1 - pos3
50
51        sub_left, sub_right = left[0], right[0]
52        for i in range(1, n):
53            current_left = max(
54                sub_left + left[i],
55                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
56            )
57            current_right = max(sub_left + right[i], sub_right + right[i])
58            sub_left, sub_right = current_left, current_right
59
60        return max(sub_left, sub_right)