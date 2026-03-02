# Last updated: 02/03/2026, 14:02:39
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = set(s + t)
        valid = True
        for i in s1:
            if s.count(i) != t.count(i):
                valid = False
                break
        return valid
        