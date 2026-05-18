# Last updated: 5/18/2026, 5:00:52 PM
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        # pair robots with their distances and sort by position
        rob = sorted(zip(robots, distance))
        p = [r[0] for r in rob]
        d = [r[1] for r in rob]

        # count walls that are exactly at a robot position
        robot_set = set(p)
        ans0 = 0
        walls_filtered = []
        for w in walls:
            if w in robot_set:
                ans0 += 1
            else:
                walls_filtered.append(w)
        walls_filtered.sort()
        m = len(walls_filtered)

        if m == 0:
            return ans0

        # ----- left region (walls before the first robot) -----
        left_count = 0
        j = 0
        while j < m and walls_filtered[j] < p[0]:
            if walls_filtered[j] >= p[0] - d[0]:
                left_count += 1
            j += 1

        # ----- gaps between consecutive robots -----
        # for each gap we store: only left robot can cover, only right robot can cover, both can cover
        left_only = [0] * (n - 1)
        right_only = [0] * (n - 1)
        both = [0] * (n - 1)

        for i in range(n - 1):
            start = p[i]
            end = p[i + 1]
            while j < m and walls_filtered[j] < end:
                if walls_filtered[j] > start:
                    distL = walls_filtered[j] - start
                    distR = end - walls_filtered[j]
                    if distL <= d[i] and distR <= d[i + 1]:
                        both[i] += 1
                    elif distL <= d[i]:
                        left_only[i] += 1
                    elif distR <= d[i + 1]:
                        right_only[i] += 1
                    # else: not coverable by any robot
                j += 1

        # ----- right region (walls after the last robot) -----
        right_count = 0
        while j < m and walls_filtered[j] <= p[-1] + d[-1]:
            right_count += 1
            j += 1

        # ----- DP over robots -----
        # dpL: best total if current robot fires left
        # dpR: best total if current robot fires right
        dpL = left_count   # robot 0 fires left
        dpR = 0            # robot 0 fires right

        for i in range(1, n):
            idx = i - 1
            A = left_only[idx] + both[idx]      # covered if left robot fires right
            B = right_only[idx] + both[idx]     # covered if right robot fires left
            C = left_only[idx] + right_only[idx] + both[idx]  # covered if both fire appropriately

            new_dpL = max(dpL + B, dpR + C)   # current robot fires left
            new_dpR = max(dpL, dpR + A)       # current robot fires right
            dpL, dpR = new_dpL, new_dpR

        result = ans0 + max(dpL, dpR + right_count)
        return result