# Last updated: 02/03/2026, 14:01:39
class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        mod = 10**9+7
        full = [0 for i in range(n+1)]
        part = [0 for i in range(n+1)]

        full[1] = 1
        full[2] = 2

        part[1] = 0
        part[2] = 1

        for i in range(3, n+1):
            full[i] = (full[i-1]+full[i-2]+2*part[i-1])%mod
            part[i] = (part[i-1]+full[i-2])%mod
        return full[-1]