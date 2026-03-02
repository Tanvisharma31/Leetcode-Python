# Last updated: 02/03/2026, 13:56:41
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        # 1. cur_cnt // 2
        # 2. min(pre_cnt, cur_cnt)
        
        n = len(nums)
        pre_cnt = 0
        cur_cnt = 0
        i = 0
        ans = 1

        while i < n - 1:
            if nums[i] >= nums[i + 1]:
                i += 1
                pre_cnt = 1
                continue
            
            start = i
            i += 1
            while i < n and nums[i] > nums[i - 1]:
                i += 1
            cur_cnt = i - start
            ans = max(ans, min(pre_cnt, cur_cnt), cur_cnt // 2)
            pre_cnt = cur_cnt
        return ans