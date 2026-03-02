# Last updated: 02/03/2026, 14:00:46
from itertools import accumulate
from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])   # m = rows, n = cols

        # Row prefix sums
        # rs[r][c] = sum of grid[r][0..c-1]
        rs = [[0] + list(accumulate(row)) for row in grid]
        # Column prefix sums
        # cs[r][c] = sum of grid[0..r-1][c]
        cs = [[0] * n for _ in range(m + 1)]

        # Main diagonal prefix sums
        # ds[r][c] = sum along diagonal ending at (r-1, c-1)
        ds = [[0] * (n + 1) for _ in range(m + 1)]

        # Anti-diagonal prefix sums
        # ads[r][c] = sum along anti-diagonal ending at (r-1, c+1)
        ads = [[0] * (n + 1) for _ in range(m + 1)]

        # Build column, diagonal, anti-diagonal prefix arrays
        for r in range(m):
            for c in range(n):
                x = grid[r][c]
                cs[r + 1][c] = cs[r][c] + x
                ds[r + 1][c + 1] = ds[r][c] + x
                ads[r + 1][c] = ads[r][c + 1] + x

        # Try k x k square sizes from largest to smallest
        for k in range(min(m, n), 0, -1):
            # bottom-right corner of square in 1-based prefix space: (R, C)
            for R in range(k, m + 1):
                for C in range(k, n + 1):

                    # Main diagonal sum for this k × k square
                    diag_sum = ds[R][C] - ds[R - k][C - k]

                    # Anti-diagonal sum check
                    if ads[R][C - k] - ads[R - k][C] != diag_sum:
                        continue

                    # Check all row sums
                    # Row index in grid = r, row range = R-k .. R-1
                    if any(rs[r][C] - rs[r][C - k] != diag_sum for r in range(R - k, R)):
                        continue

                    # Check all column sums
                    # Column index in grid = c, column range = C-k .. C-1
                    if any(cs[R][c] - cs[R - k][c] != diag_sum for c in range(C - k, C)):
                        continue

                    return k  # Found largest valid square

        return 1  # At minimum, 1x1 squares are always magic

# Time = O(m n min(m, n)), Space = O(m n)