# Last updated: 5/25/2026, 3:57:29 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        counter = 0
        for val in nums:
            if val == 1:
                counter += 1
            else:
                max_ones = max(max_ones, counter)
                counter = 0
        return max(max_ones, counter)
        