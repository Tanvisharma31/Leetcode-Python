# Last updated: 02/03/2026, 13:58:43
MOD = 10 ** 9 + 7

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        a = []
        while n:
            lb = n & -n
            a.append(lb)
            n ^= lb
        na = len(a)
        res = [[0] * na for _ in range(na)]
        for i, x in enumerate(a):
            res[i][i] = x
            for j in range(i + 1, na):
                res[i][j] = res[i][j - 1] * a[j] % MOD
        return [res[l][r] for l, r in queries]

