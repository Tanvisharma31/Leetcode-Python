# Last updated: 02/03/2026, 13:57:15
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0]+sum(heapq.nsmallest(2,nums[1:]))