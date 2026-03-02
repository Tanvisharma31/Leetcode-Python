# Last updated: 02/03/2026, 14:02:42
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 0 and n.bit_count() == 1