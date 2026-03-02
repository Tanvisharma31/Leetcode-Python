# Last updated: 02/03/2026, 13:55:30
import sys
sys.setrecursionlimit(10**5)
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        a=[[] for _ in range(n)]
        for u,v in edges:
            a[u].append(v)
            a[v].append(u)
        ti,to=[0]*n,[0]*n
        t=0
        LOG=n.bit_length()
        up=[[-1]*LOG for _ in range(n)]
        def df(u,p):
            nonlocal t
            ti[u]=t
            t+=1
            up[u][0]=p
            for i in range(1,LOG):
                if up[u][i-1]!=-1:
                    up[u][i]=up[up[u][i-1]][i-1]
            for v in a[u]:
                if v!=p:df(v,u)
            to[u]=t-1
        df(0,-1)
        def is_a(u,v):
            return ti[u]<=ti[v] and to[u]>=to[v]
        def get_lca(u,v):
            if is_a(u,v): return u
            if is_a(v,u): return v
            for i in range(LOG-1,-1,-1):
                if up[u][i]!=-1 and not is_a(up[u][i],v):
                    u=up[u][i]
            return up[u][0]
        bit=[0]*(n+1)
        def up_bit(idx,val):
            idx+=1
            while idx<=n:
                bit[idx]^=val
                idx+=idx&(-idx)
        def q_bit(idx):
            idx+=1
            res=0
            while idx>0:
                res^=bit[idx]
                idx-=idx&(-idx)
            return res
        chars=list(s)
        def char_t(c): return 1 <<(ord(c)-ord('a'))
        for i in range(n):
            m=char_t(chars[i])
            up_bit(ti[i],m)
            up_bit(to[i]+1,m)
        ans=[]
        for q in queries:
            parts=q.split()
            if parts[0]=="update":
                u,c=int(parts[1]),parts[2]
                diff=char_t(chars[u])^char_t(c)
                up_bit(ti[u],diff)
                up_bit(to[u]+1,diff)
                chars[u]=c
            else:
                u,v=int(parts[1]),int(parts[2])
                lca=get_lca(u,v)
                path_xor=q_bit(ti[u])^q_bit(ti[v])^char_t(chars[lca])
                ans.append((path_xor & (path_xor-1))==0)
        return ans
            