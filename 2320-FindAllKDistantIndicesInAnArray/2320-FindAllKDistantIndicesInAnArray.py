# Last updated: 02/03/2026, 13:59:06
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] == key:
                while  left < n and abs(left-right)>k:
                    left+=1
                while left < n and abs(left-right)<=k:
                    result.add(left)
                    left+=1
        return list(result)