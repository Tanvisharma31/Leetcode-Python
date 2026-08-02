# Last updated: 8/2/2026, 5:20:36 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]