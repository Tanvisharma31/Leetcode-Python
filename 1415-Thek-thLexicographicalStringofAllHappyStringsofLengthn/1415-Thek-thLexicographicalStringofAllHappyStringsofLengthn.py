# Last updated: 14/03/2026, 13:47:04
1class Solution:
2    def getHappyString(self, n: int, k: int) -> str:
3
4        total = 3 * (2 ** (n - 1))
5        if k > total:
6            return ""
7
8        k -= 1
9        result = []
10        last = ""
11
12        for pos in range(n):
13
14            branch = 2 ** (n - pos - 1)
15            choices = [c for c in "abc" if c != last]
16
17            idx = k // branch
18            result.append(choices[idx])
19
20            last = choices[idx]
21            k %= branch
22
23        return "".join(result)