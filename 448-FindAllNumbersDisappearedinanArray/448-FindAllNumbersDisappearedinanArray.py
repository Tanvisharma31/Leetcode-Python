# Last updated: 5/24/2026, 7:44:48 PM
1class Solution:
2    def findDisappearedNumbers(self, nums):
3        nums.sort()
4        return [i for i in range(1, len(nums)+1) if nums[bisect_left(nums, i)%len(nums)] != i]