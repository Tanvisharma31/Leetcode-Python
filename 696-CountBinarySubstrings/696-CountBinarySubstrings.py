# Last updated: 02/03/2026, 14:01:54
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        now, flag = 0, s[0]
        prev = 0
        res = 0
        for x in s:
            if x==flag:
                now += 1
            else:
                res += min(now, prev)
                prev = now
                now, flag = 1, x
        res += min(now, prev)
        return res