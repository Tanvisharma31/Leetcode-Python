# Last updated: 02/03/2026, 14:01:20
from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Initialize the directions for right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        
        # Add the starting point to the result
        result.append([rStart, cStart])
        
        # Initialize the variables
        x, y = rStart, cStart
        direction_index = 0
        steps = 1
        
        while len(result) < rows * cols:
            for _ in range(2):  # Each direction is visited twice before increasing steps
                for _ in range(steps):
                    x += directions[direction_index][0]
                    y += directions[direction_index][1]
                    
                    # Check if the position is within bounds
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                
                # Change direction
                direction_index = (direction_index + 1) % 4
            
            # Increase the steps after visiting in both directions
            steps += 1
        
        return result