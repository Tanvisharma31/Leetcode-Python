# Last updated: 6/6/2026, 5:33:57 PM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        return (L:=list(accumulate(nums, initial=0))) and [abs(L[-1]-x-2*l) for l, x in zip(L, nums)]