# Last updated: 16/03/2026, 15:43:16
1diag=[[0]*51 for _ in range(100)]
2antid=[[0]*51 for _ in range(100)]
3OFFSET=50
4class Solution:
5    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
6        def rhombusSum(i, j, d):
7            if d==0: return grid[i][j]
8            l, r, u, b=j-d, j+d, i-d, i+d
9            i0, i1=u-j+OFFSET, i-l+OFFSET
10            Sum=diag[i0][r+1]-diag[i0][j]
11            Sum+=diag[i1][j+1]-diag[i1][l]
12
13            j0, j1=u+j, b+j
14            Sum+=antid[j0][i]-antid[j0][u+1]
15            Sum+=antid[j1][b]-antid[j1][i+1]
16            return Sum
17
18        m, n=len(grid), len(grid[0])
19        for i, row in enumerate(grid):
20            for j, x in enumerate(row):
21                i0, j0=i-j+OFFSET, i+j
22                diag[i0][j+1]=diag[i0][j]+x
23                antid[j0][i+1]=antid[j0][i]+x
24
25        dM=min(m, n)>>1
26        x=[-1]*3
27        for d in range(dM+1):
28            for i in range(d, m-d):
29                for j in range(d, n-d):
30                    y=rhombusSum(i, j, d)
31                    if y==x[0] or y==x[1] or y==x[2]: continue
32                    if y>x[0]:
33                        x[2]=x[1]
34                        x[1]=x[0]
35                        x[0]=y
36                    elif y>x[0]:
37                        x[2]=x[1]
38                        x[1]=x[0]
39                        x[0]=y
40                    elif y>x[1]:
41                        x[2]=x[1]
42                        x[1]=y
43                    elif y>x[2]:
44                        x[2]=y
45
46        for i in range(2, -1, -1):
47            if x[i]==-1: x.pop()
48
49        return x