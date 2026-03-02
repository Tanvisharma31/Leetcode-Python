# Last updated: 02/03/2026, 14:03:14
class Solution:
    def indexi(self, nums:List[int], target:int, start:int, end:int , isFirst:bool):
        index=-1
        mid=0
        while start<=end:
            mid=start+(end-start)//2
            if(nums[mid]==target):
                index=mid
                if (isFirst):
                    
                    end=mid-1
                else: 
                    start=mid+1
                
            elif (nums[mid]>target):
                end=mid-1
            else: 
                start=mid+1
        return index
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first= self.indexi(nums, target,0, len(nums)-1, True)
        second= self.indexi(nums, target, 0, len(nums)-1, False)
        return [first,second]
        