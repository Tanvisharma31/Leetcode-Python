# Last updated: 6/1/2026, 8:10:00 AM
1class Solution:
2    def digits(self, x):
3        cnt = 0
4        while x > 0:
5            cnt += 1
6            x //= 10
7        return cnt
8
9    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
10        prefixes = set()
11
12        # storing all prefixes of arr1
13        for num in arr1:
14            x = num
15            while x > 0:
16                prefixes.add(x)
17                x //= 10
18
19        ans = 0
20
21        # check prefixes of arr2 numbers
22        for num in arr2:
23            x = num
24            len_ = self.digits(num)
25
26            # checking from larger => smaller
27            while x > 0:
28                if x in prefixes:
29                    ans = max(ans, len_)
30                    # first match is the longest
31                    # so we stop
32                    break
33
34                x //= 10
35                len_ -= 1
36
37        return ans