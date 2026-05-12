# Last updated: 5/12/2026, 12:36:33 PM
1class Solution:
2    def minimumEffort(self, tasks: List[List[int]]) -> int:
3        # sort by (minimum - actual) in descending order
4        tasks.sort(
5            key=lambda x: x[1] - x[0],
6            reverse=True
7        )
8
9        ans = 0
10        energy = 0
11
12        for i in range(len(tasks)):
13
14            actual = tasks[i][0]
15            minimum = tasks[i][1]
16
17            # increase initial energy if needed
18            if energy < minimum:
19                ans += (minimum - energy)
20                energy = minimum
21
22            # perform task
23            energy -= actual
24
25        return ans