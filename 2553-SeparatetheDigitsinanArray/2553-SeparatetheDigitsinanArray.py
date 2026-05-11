# Last updated: 5/11/2026, 8:07:53 PM
1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        
4        result = []
5
6        for num in nums:
7
8            s = str(num)
9
10            for ch in s:
11
12                result.append(int(ch))
13
14        return result