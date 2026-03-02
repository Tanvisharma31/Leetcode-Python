# Last updated: 02/03/2026, 13:55:42
from typing import List
from collections import deque

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        a=[[] for _ in range(n)]
        for u,v in edges:
            a[u].append(v)
            a[v].append(u)

        def d(start_node):
            di=[-1]*n
            di[start_node]=0
            queue=deque([start_node])
            while queue:
                c=queue.popleft()
                for ne in a[c]:
                    if di[ne]==-1:
                        di[ne]=di[c]+1
                        queue.append(ne)
            return di

        di_x=d(x)
        di_y=d(y)
        di_z=d(z)
        s=0
        for i in range(n):
            d1=[di_x[i],di_y[i],di_z[i]]
            d1.sort()
            if d1[0]**2+d1[1]**2==d1[2]**2:
                s+=1
        return s