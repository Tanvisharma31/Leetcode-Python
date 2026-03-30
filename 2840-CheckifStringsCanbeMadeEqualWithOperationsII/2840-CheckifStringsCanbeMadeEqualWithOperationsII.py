# Last updated: 30/03/2026, 10:34:14
1class Solution:
2    def checkStrings(self, s1: str, s2: str) -> bool:
3        prime = [
4            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
5            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
6        ]
7
8        mod = 10**9 + 7
9        h1 = [1, 1]
10        h2 = [1, 1]
11
12        for i in range(len(s1)):
13            off = i & 1
14            h1[off] = (h1[off] * prime[ord(s1[i]) - ord('a')]) % mod
15            h2[off] = (h2[off] * prime[ord(s2[i]) - ord('a')]) % mod
16
17        return h1 == h2