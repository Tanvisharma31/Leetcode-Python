# Last updated: 02/03/2026, 13:58:48
from itertools import groupby

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ = max(nums)

        return max(
            len(list(values))
            for key, values in groupby(nums)
            if key == max_
        )
        