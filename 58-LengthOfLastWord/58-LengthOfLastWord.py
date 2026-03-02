# Last updated: 02/03/2026, 14:03:07
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
