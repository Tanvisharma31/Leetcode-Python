# Last updated: 02/03/2026, 14:01:06
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = 0
            while queue:
                x,y = queue.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                        grid[nx][ny] = 0
                        queue.append((nx,ny))
        for r in range(rows):
            for c in [0,cols-1]:
                if grid[r][c]==1:
                    dfs(r,c)
        for c in range(cols):
            for r in [0,rows-1]:
                if grid[r][c]==1:
                    dfs(r,c)
        return sum(sum(row) for row in grid)