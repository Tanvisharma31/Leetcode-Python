# Last updated: 5/24/2026, 7:38:21 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        return len(set(nums)) < len(nums)