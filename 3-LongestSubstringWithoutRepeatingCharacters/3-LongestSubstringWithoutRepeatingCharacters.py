# Last updated: 02/03/2026, 14:03:21
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        m = 0
        dp = 0
        base = 0
        for i in range(len(s)):
            if s[i] in d:
                base = d[s[i]] if d[s[i]] > base else base
                dp = i - base
            else:
                dp = dp + 1
            if dp > m:
                m = dp
            d[s[i]] = i
        return m

