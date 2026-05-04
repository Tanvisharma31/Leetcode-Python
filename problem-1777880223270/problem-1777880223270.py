# Last updated: 5/4/2026, 1:07:03 PM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        n=len(matrix)
4        for i in range(n):
5            for j in range(i+1,n):
6                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
7        for row in matrix:
8            row.reverse()
9        