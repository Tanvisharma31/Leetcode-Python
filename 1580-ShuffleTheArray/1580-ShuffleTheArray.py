# Last updated: 02/03/2026, 14:00:16
import random

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
