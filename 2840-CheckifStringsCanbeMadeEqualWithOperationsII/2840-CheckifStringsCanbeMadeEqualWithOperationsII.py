# Last updated: 30/03/2026, 10:34:31
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # strategy:
        # 1. odd indexes should contain the same elements in s1 and s2        
        # 2. even indexes should contain the same elements in s1 and s2

        return Counter(s1[::2]) == Counter(s2[::2]) and \
               Counter(s1[1::2]) == Counter(s2[1::2])
