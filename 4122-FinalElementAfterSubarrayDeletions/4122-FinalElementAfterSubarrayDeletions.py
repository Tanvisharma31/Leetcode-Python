# Last updated: 02/03/2026, 13:55:49
class Solution:
    def finalElement(self, nums: List[int]) -> int:
        return max(nums[0],nums[-1])