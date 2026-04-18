# Last updated: 18/04/2026, 16:18:24
class Solution:
    def mirrorDistance(self, n: int) -> int:

        return abs(n - int(str(n)[::-1]))
        