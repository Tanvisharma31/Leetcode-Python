# Last updated: 21/03/2026, 11:35:33
1class Solution:
2    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
3        t, b=x, x+k-1
4        while t<b:
5            grid[t][y:y+k], grid[b][y:y+k]=grid[b][y:y+k],grid[t][y:y+k]
6            t+=1
7            b-=1
8        return grid