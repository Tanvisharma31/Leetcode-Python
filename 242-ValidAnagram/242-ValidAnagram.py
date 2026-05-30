# Last updated: 5/30/2026, 8:47:17 AM
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return dict(Counter(s))==dict(Counter(t))