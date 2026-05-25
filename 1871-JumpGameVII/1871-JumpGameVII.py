# Last updated: 5/25/2026, 1:26:30 PM
1class Solution:
2    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
3        n=len(s)
4        if int(s[-1]): return False
5        dp=[False]*n
6        dp[0]=True
7        reach,maxR=0,maxJump
8        for i in range(minJump,n):
9            if i>maxR:
10                return False
11            reach+=dp[i-minJump]
12            if i>maxJump:
13                reach-=dp[i-maxJump-1]
14            if reach and not int(s[i]):
15                dp[i]=True
16                maxR=i+maxJump
17        return reach>0