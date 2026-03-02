# Last updated: 02/03/2026, 13:55:47
class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            cs=0
            seen=set()
            for j in range(i,n):
                cs+=nums[j]
                seen.add(nums[j])
                if cs in seen:
                    count+=1
        return count