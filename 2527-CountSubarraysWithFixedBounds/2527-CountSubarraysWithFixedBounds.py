# Last updated: 02/03/2026, 13:58:44
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        min_position = max_position = bad_position = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_position = i
            if num == minK:
                min_position = i
            if num == maxK:
                max_position = i
            
            valid_start = min(min_position, max_position)
            if valid_start > bad_position:
                answer += valid_start - bad_position
        
        return answer
