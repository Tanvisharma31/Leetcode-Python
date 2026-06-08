# Last updated: 6/8/2026, 4:22:34 PM
1class Solution:
2    def newf(self, nums: List[int], pivot: int) -> List[int]:
3        x = []
4        y = []
5        z = []
6        for i in nums:
7            if i < pivot:
8                x.append(i)
9            elif i == pivot:
10                y.append(i)
11            else:
12                z.append(i)
13        return x + y + z
14
15    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
16        
17        return self.newf(nums, pivot)