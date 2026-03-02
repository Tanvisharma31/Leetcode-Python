# Last updated: 02/03/2026, 13:56:56
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        n=len(nums)
        for i in range(0,n):
            if(nums[i]==0):
                if(i+2>=n): return -1
                nums[i+1]^=1
                nums[i+2]^=1
                ans+=1
        return ans
        
