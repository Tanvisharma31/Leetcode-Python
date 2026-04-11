# Last updated: 11/04/2026, 13:36:54
1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        n, M=len(nums), max(nums)
4        pos=[(-1, -1) for _ in range(M+1)]
5        ans=1<<32
6        for k, x in enumerate(nums):
7            if pos[x][1]!=-1:
8                ans=min(ans, (k-pos[x][1])<<1)
9            pos[x]=k, pos[x][0]
10        return -1 if ans==1<<32 else ans      