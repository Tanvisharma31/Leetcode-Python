# Last updated: 11/03/2026, 11:40:02
1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        if n == 0: return 1
4        return ~n & (1 << n.bit_length()) - 1