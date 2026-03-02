# Last updated: 02/03/2026, 13:57:03
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy[:]
        for i in range(len(energy) - k - 1, -1, -1):
            dp[i] += dp[i + k]
        return max(dp)
        # time: O(n)
        # space: O(1)