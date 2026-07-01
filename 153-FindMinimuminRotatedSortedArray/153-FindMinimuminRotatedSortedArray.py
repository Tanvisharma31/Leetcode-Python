# Last updated: 7/1/2026, 8:58:17 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]