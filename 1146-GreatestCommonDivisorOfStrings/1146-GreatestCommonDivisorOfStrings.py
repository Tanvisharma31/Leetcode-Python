# Last updated: 02/03/2026, 14:01:02
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        from math import gcd
        return str1[:gcd(len(str1),len(str2))]