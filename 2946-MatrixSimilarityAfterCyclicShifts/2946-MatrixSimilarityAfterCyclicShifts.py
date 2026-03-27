# Last updated: 27/03/2026, 10:15:09
1class Solution:
2    def areSimilar(self, mat, k):
3        m, n = len(mat), len(mat[0])
4        
5        k %= n  # (reduce k<n)
6        
7        for i in range(m):
8            for j in range(n):
9                if i % 2 == 0:
10                    # even row , left shift
11                    if mat[i][j] != mat[i][(j + k) % n]:
12                        return False
13                else:
14                    # odd row , right shift
15                    if mat[i][j] != mat[i][(j - k) % n]:
16                        return False
17        
18        return True