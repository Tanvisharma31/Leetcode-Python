# Last updated: 6/1/2026, 11:07:03 AM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        a=[]
4        for i in nums:
5          s=i*i
6          a.append(s)
7        a.sort()
8        return a
9        
10        