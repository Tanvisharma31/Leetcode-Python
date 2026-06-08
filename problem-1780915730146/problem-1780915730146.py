# Last updated: 6/8/2026, 4:18:50 PM
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        n=len(nums)
4        if n==1: return nums
5        R=[]
6        l, m=0, 0
7        for x in nums:
8            if x<pivot:
9                nums[l]=x
10                l+=1
11            elif x>pivot:
12                R.append(x)
13            else:
14                m+=1
15        return nums[:l]+[pivot]*m+R
16        