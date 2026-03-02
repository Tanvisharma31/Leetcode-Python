# Last updated: 02/03/2026, 13:55:57
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        if n == 2:
            if (nums[0] + nums[1]) & 1: return 2
            else: return 0 

        best = 0
        # seen[x] = start idx of subarray in which it was last seen 
        seen = [-1] * (max(nums) + 1) # shift to 1-idx: idx = num
        parity = [0, 0] # [distinct_even count, distinct_odd count]

        for left in range(n):
            if n - left <= best: break # early exit from R/S subarrays
            
            for right in range(left, n):
                x = nums[right]

                if seen[x] != left: # not seen yet in subarray nums[left:]
                    seen[x] = left
                    parity[x & 1] += 1
                
                if parity[0] == parity[1]:
                    window = right - left + 1
                    if window > best: best = window
            
            parity[0] = parity[1] = 0 # reset counts for next iteration

        return best