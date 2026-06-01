# Last updated: 6/1/2026, 8:07:59 AM
1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        if n == 1:
4            return '0'
5        
6        length = (1 << n) - 1
7        mid = (length + 1) // 2
8        
9        if k == mid:
10            return '1'
11        if k < mid:
12            return self.findKthBit(n - 1, k)
13        
14        c = self.findKthBit(n - 1, length - k + 1)
15        return '1' if c == '0' else '0'