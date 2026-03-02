# Last updated: 02/03/2026, 13:55:40
import sys
sys.setrecursionlimit(200000)
class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:

        def dfs(u,p):
            for v,i in a[u]:
                if v!=p:
                    dfs(v,u)
                    if diff[v]==1:
                        res.append(i)
                        diff[v]^=1
                        diff[u]^=1
                        
                    
        diff=[0]*n
        for i in range(n):
            if start[i]!=target[i]:
                diff[i]=1
        a=[[] for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            a[u].append((v,i))
            a[v].append((u,i))
        res=[]
        dfs(0,-1)
        if diff[0]==1:
            return [-1]
        res.sort()
        return res
            