# Last updated: 5/25/2026, 1:18:13 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        res=""
4        resLen=0
5        for i in range(len(s)):
6            l,r=i,i
7            while l>=0 and r<len(s) and s[l]==s[r]:
8                if (r-l+1)>resLen:
9                    res=s[l:r+1]
10                    resLen=r-l+1
11                l-=1
12                r+=1
13            #even
14            l,r=i,i+1
15            while l>=0 and r<len(s) and s[l]==s[r]:
16                if (r-l+1)>resLen:
17                    res=s[l:r+1]
18                    resLen=r-l+1
19                l-=1
20                r+=1
21        return res