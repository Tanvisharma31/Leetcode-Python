# Last updated: 02/03/2026, 14:01:11
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])