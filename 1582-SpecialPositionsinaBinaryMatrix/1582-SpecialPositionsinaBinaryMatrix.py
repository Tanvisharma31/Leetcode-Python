# Last updated: 04/03/2026, 19:10:21
1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3        def check1(row):
4            ans=[]
5            for i, x in enumerate(row):
6                if x==1: 
7                    ans.append(i)
8            return ans
9        m=len(mat)
10        n=len(mat[0])
11        ans=0
12        col=[False]*n
13        for row in mat:
14            idx=check1(row)
15            if len(idx)==1 and not col[j:=idx[0]]:
16                col[j]=True
17                count_col1=0
18                for k in range(m):
19                    count_col1+=mat[k][j]
20                if count_col1==1:
21                    ans+=1
22            else:
23                for j in idx:
24                    col[j]==True
25        return ans