# Last updated: 02/03/2026, 14:03:10
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = -float("inf")
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum = cur_sum + nums[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum