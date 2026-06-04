# Last updated: 6/4/2026, 6:56:31 PM
1class Solution:
2    MAX = 100001
3    dp = [0] * MAX
4    pref = [0] * MAX
5
6    for i in range(100, MAX):
7        r = i % 10
8        m = (i // 10) % 10
9        l = (i // 100) % 10
10
11        isWave = m > max(l, r) or m < min(l, r)
12        dp[i] = dp[i // 10] + int(isWave)
13        pref[i] = pref[i - 1] + dp[i]
14
15    def totalWaviness(self, A: int, B: int) -> int:
16        return self.pref[B] - self.pref[A - 1]
17