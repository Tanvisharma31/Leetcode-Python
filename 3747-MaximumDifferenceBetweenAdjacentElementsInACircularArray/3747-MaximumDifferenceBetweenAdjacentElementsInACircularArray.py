# Last updated: 02/03/2026, 13:56:20
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(nums[0])
        return max(abs(nums[i] - nums[i+1]) for i in range(N))