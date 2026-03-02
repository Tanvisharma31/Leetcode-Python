# Last updated: 02/03/2026, 14:01:14
class Solution(object):
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()

        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return i