# Last updated: 02/03/2026, 14:02:43
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums))==len(nums):
            return False
        if len(nums)<=k+1:
            return True
        hashmap = {}
        for i, v in enumerate(nums):
            if v in hashmap:
                if i - hashmap[v] <= k:
                    return True
            hashmap[v] = i
        return False
                 