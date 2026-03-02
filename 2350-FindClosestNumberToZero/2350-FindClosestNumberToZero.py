# Last updated: 02/03/2026, 13:59:02
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        len_nums=len(nums)
        min_d=None
        close_n=None
        i=0
        while i<len_nums:
            num=nums[i]
            if min_d is None or abs(num-0)<=min_d:
                close_n=max(num,close_n) if min_d==abs(num-0) else num
                min_d=abs(num-0)
            i+=1
        return close_n