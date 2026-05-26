# Last updated: 5/26/2026, 7:10:37 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        return " ".join(s.split()[::-1])