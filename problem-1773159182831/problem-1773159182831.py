# Last updated: 10/03/2026, 21:43:02
1MOD = 1_000_000_007
2MAXN = 1000
3fact = [0] * (MAXN + 1)
4invfact = [0] * (MAXN + 1)
5
6def init():
7    fact[0] = 1
8    for i in range(1, MAXN + 1):
9        fact[i] = (fact[i - 1] * i) % MOD
10    invfact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
11    for i in range(MAXN, 0, -1):
12        invfact[i - 1] = (invfact[i] * i) % MOD
13
14init()
15
16class Solution:
17    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
18        if zero > one:
19            zero, one = one, zero
20
21        if limit == 1:
22            if zero == one: return 2
23            if zero + 1 == one: return 1
24            return 0
25
26        def ncr(n: int, r: int) -> int:
27            return fact[n] * invfact[r] * invfact[n - r]
28
29        def ways(n: int, k: int) -> int:
30            if n == k: return 1
31            j, total, flag = 0, 0, True
32            while j <= k <= n:
33                term = ncr(k, j) * ncr(n - 1, k - 1)
34                total = total + term if flag else total - term
35                n -= limit
36                j += 1
37                flag = not flag
38            return total
39
40        result = 0
41        start = (zero + limit - 1) // limit
42        prv, cur, nxt = 0, ways(one, start), ways(one, start + 1)
43
44        for k in range(start, zero + 1):
45            result += (prv + 2 * cur + nxt) * ways(zero, k)
46            prv, cur, nxt = cur, nxt, ways(one, k + 2)
47
48        return result % MOD