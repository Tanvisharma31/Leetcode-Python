# Last updated: 5/24/2026, 7:37:52 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)

        return  not(len(s) == len(nums))