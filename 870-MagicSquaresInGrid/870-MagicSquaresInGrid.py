# Last updated: 02/03/2026, 14:01:31
from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # All possible 3x3 magic squares
        magic_squares = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        ]
        
        def isMagicSquare(square: List[List[int]]) -> bool:
            return square in magic_squares

        def getSubgrid(grid: List[List[int]], r: int, c: int) -> List[List[int]]:
            return [row[c:c+3] for row in grid[r:r+3]]

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                subgrid = getSubgrid(grid, r, c)
                if isMagicSquare(subgrid):
                    count += 1

        return count
