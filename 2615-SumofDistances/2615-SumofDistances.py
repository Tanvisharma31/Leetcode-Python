# Last updated: 23/04/2026, 18:01:17
1class Solution:
2    def distance(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        nxt=[-1]*n
5        idx={}
6        for i, x in enumerate(nums):
7            if x not in idx:
8                idx[x]=i
9            else:
10                nxt[i]=idx[x]
11                idx[x]=i
12        ans=[0]*n
13        for x, h in idx.items():
14            if nxt[h]==-1: continue
15            total, prefix=0, 0
16            vz, j=0, h
17            while j!=-1:
18                total+=j
19                vz+=1
20                j=nxt[j]
21            j=h
22            for i in range(vz-1, -1, -1):
23                 ans[j]=(2*i-vz+2)*j+2*prefix-total
24                 prefix+=j
25                 j=nxt[j]
26        return ans