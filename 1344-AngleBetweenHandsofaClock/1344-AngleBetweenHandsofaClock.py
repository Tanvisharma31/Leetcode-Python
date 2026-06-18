# Last updated: 6/18/2026, 4:44:55 PM
1class Solution:
2    def angleClock(self, hour: int, minutes: int) -> float:
3        x = hour + minutes / 60
4        diff = (11 * x) % 12
5        return min(diff, 12 - diff) * 30