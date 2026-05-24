# Last updated: 5/24/2026, 7:42:04 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hashset={}
4        for i, num in enumerate(nums):
5            if target-num in hashset:
6                return hashset[target-num],i
7            hashset[num]=i
8