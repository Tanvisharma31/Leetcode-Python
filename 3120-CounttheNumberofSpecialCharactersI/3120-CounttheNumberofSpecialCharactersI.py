# Last updated: 5/26/2026, 11:32:33 AM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        lower = 0
4        upper = 0
5
6        for ch in word:
7            if ch.islower():
8                lower |= (1 << (ord(ch) - ord('a')))
9            else:
10                upper |= (1 << (ord(ch) - ord('A')))
11
12        common = lower & upper
13
14        # counting number of set bits
15        return common.bit_count()