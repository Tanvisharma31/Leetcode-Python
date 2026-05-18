# Last updated: 5/18/2026, 1:04:44 PM
1class Solution:
2    def minJumps(self, arr: List[int]) -> int:
3        n=len(arr)
4        vis=[False]*n
5        mp=defaultdict(list)
6        for i, x in enumerate(arr):
7            mp[x].append(i)
8        q=deque([0])
9        step=0
10        while q:
11            s=len(q)
12            for _ in range(s):
13                cur=q.popleft()
14                if cur==n-1: return step
15                if cur>=1 and not vis[cur-1]:
16                    q.append(cur-1)
17                    vis[cur-1]=True
18                if cur<=n and not vis[cur+1]:
19                    q.append(cur+1)
20                    vis[cur+1]=True
21                x=arr[cur]
22                for idx in mp[x]:
23                    if not vis[idx]:
24                        q.append(idx)
25                        vis[idx]=True
26                mp[x].clear()
27            step+=1
28        return -1