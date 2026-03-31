# Last updated: 31/03/2026, 19:16:36
1class Solution:
2    def generateString(self, s: str, t: str) -> str:
3        n, m = len(s), len(t)
4        ans = ['?'] * (n + m - 1)  # ? indicates a pending position
5        
6        # Process 'T'
7        for i, b in enumerate(s):
8            if b != 'T':
9                continue
10            # The substring must match t
11            for j, c in enumerate(t):
12                v = ans[i + j]
13                if v != '?' and v != c:
14                    return ""
15                ans[i + j] = c
16        
17        old_ans = ans
18        ans = ['a' if c == '?' else c for c in ans]  # Initial default is 'a'
19        
20        # Process 'F'
21        for i, b in enumerate(s):
22            if b != 'F':
23                continue
24            # Substring must not equal t
25            if ''.join(ans[i: i + m]) != t:
26                continue
27            # Locate the last pending position to modify
28            for j in range(i + m - 1, i - 1, -1):
29                if old_ans[j] == '?':  # Change 'a' to 'b'
30                    ans[j] = 'b'
31                    break
32            else:
33                return ""
34        return ''.join(ans)