# Last updated: 5/24/2026, 7:45:13 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        counts=Counter(nums)
        ans=[]

        for i in range(1,len(nums)+1):
            if i not in counts:
                ans.append(i)
        
        return ans
        
        i=0
        n=len(nums)

        while i<n:
            homeidx=nums[i]-1

            if nums[i]!=nums[homeidx]:
                nums[i],nums[homeidx]=nums[homeidx],nums[i]
            
            else:
                i+=1
        
        ans=[]
        for i in range(n):
            if nums[i]!=i+1:
                ans.append(i+1)
        
        return ans

        '''
        arr=[0]*(len(nums)+1)
        ans=[]

        for n in nums:
            arr[n]=1
        for i in range(1,len(nums)+1):
            if arr[i]==0:
                ans.append(i)
        
        return ans