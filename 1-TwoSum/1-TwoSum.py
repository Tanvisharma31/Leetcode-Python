# Last updated: 5/30/2026, 9:01:28 AM
1class Solution:
2    def longestCommonPrefix(self, v: List[str]) -> str:
3        ans=""
4        v=sorted(v)
5        first=v[0]
6        last=v[-1]
7        for i in range(min(len(first),len(last))):
8            if(first[i]!=last[i]):
9                return ans
10            ans+=first[i]
11        return ans 