# Last updated: 02/03/2026, 14:00:05
from typing import List
from collections import deque

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def countIslands(g):
            m, n = len(g), len(g[0])
            visited = [[False] * n for _ in range(m)]
            
            def bfs(r, c):
                queue = deque([(r, c)])
                visited[r][c] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            
            count = 0
            for r in range(m):
                for c in range(n):
                    if g[r][c] == 1 and not visited[r][c]:
                        bfs(r, c)
                        count += 1
            return count
        
        def isDisconnected(g):
            m, n = len(g), len(g[0])
            visited = [[False] * n for _ in range(m)]
            
            def bfs(r, c):
                queue = deque([(r, c)])
                visited[r][c] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            
            # Find the first land cell and start BFS from it
            start_found = False
            for r in range(m):
                for c in range(n):
                    if g[r][c] == 1:
                        if not start_found:
                            bfs(r, c)
                            start_found = True
                        else:
                            for x in range(m):
                                for y in range(n):
                                    if g[x][y] == 1 and not visited[x][y]:
                                        return False
                            return True
            return True

        # Initial number of islands
        initial_islands = countIslands(grid)
        
        if initial_islands == 0:
            return 0
        if initial_islands > 1:
            return 0
        
        # Check for single removal
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if countIslands(grid) != 1:
                        return 1
                    grid[r][c] = 1
        
        # Check for double removal
        for r1 in range(len(grid)):
            for c1 in range(len(grid[0])):
                if grid[r1][c1] == 1:
                    for r2 in range(r1, len(grid)):
                        for c2 in range(c1 + 1 if r1 == r2 else 0, len(grid[0])):
                            if grid[r2][c2] == 1 and (r1 != r2 or c1 != c2):
                                grid[r1][c1] = 0
                                grid[r2][c2] = 0
                                if countIslands(grid) != 1:
                                    return 2
                                grid[r1][c1] = 1
                                grid[r2][c2] = 1
        
        return -1
