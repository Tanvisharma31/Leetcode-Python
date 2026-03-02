# Last updated: 02/03/2026, 13:55:52
class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n=len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        if colors[1]==colors[0]:
            dp[1]=max(nums[0],nums[1])
        else:
            dp[1]=nums[0]+nums[1]
        for i in range(2,n):
            o=dp[i-1]
            if colors[i]==colors[i-1]:
                p=nums[i]+dp[i-2]
            else:
                p=nums[i]+dp[i-1]
            dp[i]=max(o,p)
        return dp[-1]