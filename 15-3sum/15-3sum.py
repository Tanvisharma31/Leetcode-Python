# Last updated: 02/03/2026, 14:03:17
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=[]
        nums.sort()
        for i,v in enumerate(nums):
            if (i>0) and (v==nums[i-1]):
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                c_sum=v+nums[l]+nums[r]
                if c_sum>0:
                    r-=1
                elif c_sum<0:
                    l+=1
                else:
                    triplets.append([v,nums[l],nums[r]])
                    l+=1
                    while (l<r) and nums[l]==nums[l-1]:
                        l+=1
        return triplets