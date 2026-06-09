# Last updated: 6/9/2026, 9:29:52 AM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        minn = min(nums)
        return (maxx - minn) * k