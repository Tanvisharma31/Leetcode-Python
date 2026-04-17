# Last updated: 17/04/2026, 13:45:48
1class Solution:
2    def minMirrorPairDistance(self, nums: List[int]) -> int:
3        def rev(x):
4            ans=0
5            while x>0:
6                x, d=divmod(x, 10)
7                ans=10*ans+d
8            return ans
9        mp={}
10        dist=inf
11        for i, x in enumerate(nums):
12            R=rev(x)
13            if x in mp:
14                dist=min(dist, i-mp[x])
15            mp[R]=i
16        return -1 if dist==inf else dist
17        