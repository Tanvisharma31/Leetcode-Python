# Last updated: 02/03/2026, 14:02:53
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = Counter(nums)
        for i in x.keys():
            if x[i] == 1:
                return i
        return 0