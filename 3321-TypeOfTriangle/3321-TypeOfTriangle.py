# Last updated: 02/03/2026, 13:57:10
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[2]>=nums[0]+nums[1]: return "none"
        if nums[0]==nums[2]: return "equilateral"
        if nums[0]==nums[1] or nums[1]==nums[2]: return "isosceles"
        return "scalene"

