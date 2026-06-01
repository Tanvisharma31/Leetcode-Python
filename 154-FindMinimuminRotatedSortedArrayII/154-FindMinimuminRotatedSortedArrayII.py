# Last updated: 6/1/2026, 8:13:17 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l=0
4        r=len(nums)-1
5        while l<r:
6            mid=(l+r)//2
7            if nums[mid]<nums[r]:
8                r=mid
9            elif nums[mid]>nums[r]:
10                l=mid+1
11            else:
12                r-=1
13        return nums[l]