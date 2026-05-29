# Last updated: 5/29/2026, 11:43:28 AM
1class Solution:
2    def minElement(self, nums: list[int]) -> int:
3        min_val = float('inf')
4        
5        for num in nums:
6            current_sum = 0
7            
8            while num > 0:
9                current_sum += num % 10
10                num //= 10
11            
12            min_val = min(min_val, current_sum)
13                
14        return min_val