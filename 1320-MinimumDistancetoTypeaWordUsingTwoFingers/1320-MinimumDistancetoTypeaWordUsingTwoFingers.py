# Last updated: 12/04/2026, 15:04:21
1# dp[i][j]=min cost after typing word[i], with the OTHER finger at j
2# 26 denotes hovering
3class Solution:
4    def minimumDistance(self, word: str) -> int:
5        def dist(x, y):
6            if x==26 or y==26: return 0
7            return abs(x//6-y//6)+abs(x%6-y%6)
8        # setting for dp
9        n=len(word)
10        INF=1<<30
11        dp=[[INF]*27 for _ in range(n)]
12        dp[0][26]=0
13        prev=ord(word[0])-65
14        for i, c in enumerate(word[1:], start=1):
15            x=ord(c)-65
16            for j in range(27):
17                dp[i][j]=min(dp[i][j], dp[i-1][j]+dist(prev, x))
18                dp[i][prev]=min(dp[i][prev], dp[i-1][j]+dist(j, x))
19            prev=x
20        return min(dp[-1])
21        
22        