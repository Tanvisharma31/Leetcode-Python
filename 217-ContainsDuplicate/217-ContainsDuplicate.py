# Last updated: 5/24/2026, 7:37:29 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))       