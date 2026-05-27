# Last updated: 5/27/2026, 6:27:01 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l, r = 0, len(numbers) - 1
4
5        while l < r:
6            s = numbers[l] + numbers[r]
7
8            if s == target:
9                return [l + 1, r + 1]
10
11            elif s < target:
12                l += 1
13
14            else:
15                r -= 1