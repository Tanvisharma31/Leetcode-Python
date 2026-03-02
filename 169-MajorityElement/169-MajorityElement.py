# Last updated: 02/03/2026, 14:02:51
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        return nums[n//2]