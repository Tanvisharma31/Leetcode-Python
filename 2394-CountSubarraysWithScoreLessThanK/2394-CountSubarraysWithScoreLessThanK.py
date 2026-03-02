# Last updated: 02/03/2026, 13:58:57
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        total_sum=0
        current_sum=0
        n=len(nums)
        for right in range(n):
            current_sum+=nums[right]
            while current_sum *(right-left+1) >= k:
                current_sum-=nums[left]
                left+=1
            total_sum+=(right-left+1)
        return total_sum