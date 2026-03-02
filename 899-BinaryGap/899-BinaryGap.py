# Last updated: 02/03/2026, 14:01:24
class Solution:
    def binaryGap(self, n: int) -> int:
        n //= n & -n
        if n == 1: return 0

        max_gap = 0
        gap = 0

        while n:
            if n & 1:
                max_gap = max(max_gap, gap)
                gap = 0
            else:
                gap += 1
            n >>= 1

        return max_gap + 1