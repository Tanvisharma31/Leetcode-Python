# Last updated: 5/26/2026, 7:08:51 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        l=0
7        for i in range(len(nums)):
8            if nums[i]!=0:
9                nums[i],nums[l]=nums[l],nums[i]
10                l+=1
11        return nums        