# Last updated: 02/03/2026, 14:02:04
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)

        res = 0
        for val in freq:
            if val + 1 in freq:
                res = max(res, freq[val] + freq[val + 1])
        
        return res

