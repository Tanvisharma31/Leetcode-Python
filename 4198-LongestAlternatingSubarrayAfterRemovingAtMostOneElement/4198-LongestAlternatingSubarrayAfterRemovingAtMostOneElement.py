# Last updated: 02/03/2026, 13:55:29
class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0 : return 0
        if n==1 : return 1
        dp=[[1]*2 for _ in range(n)]
        a=1
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                dp[i][0]=dp[i-1][1]+1
            elif nums[i]>nums[i-1]:
                dp[i][1]=dp[i-1][0]+1
            a=max(a,dp[i][0],dp[i][1])
        rdp=[[1]*2 for _ in range(n)]

        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                rdp[i][0]=rdp[i+1][1]+1
            elif nums[i]<nums[i+1]:
                rdp[i][1]=rdp[i+1][0]+1
        
        for i in range(1,n-1):
            l=nums[i-1]
            r=nums[i+1]
            if l<r:
                a=max(a,dp[i-1][0]+rdp[i+1][0])
            elif l>r:
                a=max(a,dp[i-1][1]+rdp[i+1][1])
        return a