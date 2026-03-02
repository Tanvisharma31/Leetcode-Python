# Last updated: 02/03/2026, 13:55:31
class Solution:
    def reverseByType(self, s: str) -> str:
        l=[c for c in s if c.islower()]
        m=[c for c in s if not c.islower()]
        r=[]
        for c in s:
            if c.islower():
                r.append(l.pop())
            else:
                r.append(m.pop())
        return "".join(r)
            