# Last updated: 5/27/2026, 7:12:15 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l, r=0, len(height)-1
4        res=0
5        while l<r:
6            res=max(res,(r-l)* min(height[l],height[r]))
7            if height[l]<height[r]:
8                l+=1
9            else:
10                r-=1
11        return res