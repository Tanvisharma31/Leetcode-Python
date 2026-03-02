# Last updated: 02/03/2026, 14:00:24
x, y = 6,6
nb = [1, (x+y) % (10**9+7)]
for _ in range(1, 5000):
    x,y = 3*x+2*y, 2*x+2*y
    nb.append((x+y) % (10**9+7))

class Solution:
    def numOfWays(self, n: int) -> int:
        return nb[n]
        