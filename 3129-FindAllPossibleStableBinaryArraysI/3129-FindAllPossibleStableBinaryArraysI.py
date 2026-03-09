# Last updated: 09/03/2026, 11:27:19
1class Solution:
2    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
3        MOD = 1000000007
4        maxN = zero + one
5        
6        fact = [0] * (maxN + 1)
7        invFact = [0] * (maxN + 1)
8        
9        fact[0] = 1
10        invFact[0] = 1
11        for i in range(1, maxN + 1):
12            fact[i] = (fact[i - 1] * i) % MOD
13            
14        invFact[maxN] = pow(fact[maxN], MOD - 2, MOD)
15        for i in range(maxN - 1, 0, -1):
16            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD
17            
18        def C(n, k):
19            if k < 0 or k > n:
20                return 0
21            return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
22
23        def F(N, K, L):
24            if K <= 0 or K > N:
25                return 0
26            ans = 0
27            maxJ = (N - K) // L
28            for j in range(maxJ + 1):
29                term = C(K, j) * C(N - j * L - 1, K - 1) % MOD
30                if j & 1:
31                    ans = (ans - term + MOD) % MOD
32                else:
33                    ans = (ans + term) % MOD
34            return ans
35
36        maxK = min(zero, one + 1)
37        fOne = [0] * (maxK + 2)
38        for k in range(1, maxK + 2):
39            fOne[k] = F(one, k, limit)
40            
41        ans = 0
42        for k in range(1, maxK + 1):
43            fz = F(zero, k, limit)
44            if fz == 0:
45                continue
46            fo = (fOne[k - 1] + 2 * fOne[k] + fOne[k + 1]) % MOD
47            ans = (ans + fz * fo) % MOD
48            
49        return ans