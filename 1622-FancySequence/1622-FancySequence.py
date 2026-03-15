# Last updated: 15/03/2026, 19:01:29
p = 10**9 + 7
inv = [None] + [pow(m, -1, p) for m in range(1, 101)]

class Fancy:

    def __init__(self):
        self.x = []
        self.a = 1
        self.ainv = 1
        self.b = 0

    def append(self, val):
        self.x.append((val - self.b) * self.ainv)

    def addAll(self, inc):
        self.b += inc

    def multAll(self, m):
        self.a = self.a * m % p
        self.ainv = self.ainv * inv[m] % p
        self.b = self.b * m % p

    def getIndex(self, idx):
        if idx >= len(self.x):
            return -1
        return (self.a * self.x[idx] + self.b) % p