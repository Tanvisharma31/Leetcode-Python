# Last updated: 5/31/2026, 9:23:09 AM
1class Solution:
2    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
3        asteroids.sort()
4        for a in asteroids:
5            if mass<a:
6                return False
7            mass+=a
8        return True