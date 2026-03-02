# Last updated: 02/03/2026, 13:57:42
import numpy as np

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        counts = np.zeros(n + 1, dtype=np.int64)
        val = int(1e9 + 7)
        counts[0] = 1

        for i in range(1, n + 1):
            # Don't add it
            v = i ** x
            if v > n:
                break
            counts[v:] += counts[:n - v + 1]
            counts = counts % val

        return int(counts[n])