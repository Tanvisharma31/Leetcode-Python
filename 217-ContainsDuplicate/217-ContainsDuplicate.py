# Last updated: 5/24/2026, 7:36:58 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        return len(nums)!=len(set(nums))