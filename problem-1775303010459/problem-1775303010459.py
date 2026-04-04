# Last updated: 04/04/2026, 17:13:30
1class Solution:
2    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
3        if rows == 1:
4            return encodedText
5
6        n = len(encodedText)
7        cols = n // rows
8        res = []
9
10        for c in range(cols):
11            r, j = 0, c
12            while r < rows and j < cols:
13                res.append(encodedText[r * cols + j])
14                r += 1
15                j += 1
16
17        return "".join(res).rstrip()