# Last updated: 02/03/2026, 14:02:47
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        def explore_island(row, col, island_id):
            if row < 0 or row > max_row or col < 0 or col > max_col or grid[row][col] != "1":
                return
            grid[row][col] = str(island_id)

            explore_island(row + 1, col, island_id)
            explore_island(row - 1, col, island_id)
            explore_island(row, col + 1, island_id)
            explore_island(row, col - 1, island_id)



        island_id = 1
        for row in range(max_row + 1):
            for col in range(max_col + 1):
                if grid[row][col] == "1":
                    island_id += 1
                    explore_island(row, col, island_id)

        return island_id - 1
                    