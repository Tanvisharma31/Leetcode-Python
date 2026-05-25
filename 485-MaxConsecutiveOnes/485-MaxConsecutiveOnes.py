# Last updated: 5/25/2026, 3:57:10 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        maxCount = 0
4        count = 0
5
6        for num in nums:
7            if num == 1:
8                count += 1
9                maxCount = max(maxCount, count)
10            else:
11                count = 0
12
13        return maxCount