# Last updated: 18/03/2026, 15:13:52
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        grid = map(accumulate, grid)
        grid = map(accumulate, zip(*grid))
        return sum(val <= k for row in grid for val in row )