# Last updated: 5/18/2026, 5:00:34 PM
class Solution:
    def mirrorDistance(self, n: int) -> int:

        return abs(n - int(str(n)[::-1]))
        
        