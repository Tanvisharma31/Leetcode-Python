# Last updated: 02/03/2026, 14:02:37
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1))-sum(nums)