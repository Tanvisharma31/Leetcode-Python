# Last updated: 6/14/2026, 8:10:01 PM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        minn = min(nums)
        return (maxx - minn) * k