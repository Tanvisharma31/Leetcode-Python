# Last updated: 02/03/2026, 14:03:13
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            
            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicates
                if candidates[i] == prev:
                    continue
                # Choose the current number
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
                # Update prev to the current number
                prev = candidates[i]
        
        # Sort candidates to handle duplicates and facilitate the process
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result
