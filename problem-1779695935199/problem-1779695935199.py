# Last updated: 5/25/2026, 1:28:55 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        i=0
4        for j in range(1,len(nums)):
5            if nums[j]!=nums[i]:
6                i+=1
7                nums[i]=nums[j]
8        return i+1
9