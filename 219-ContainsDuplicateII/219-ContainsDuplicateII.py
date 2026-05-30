# Last updated: 5/30/2026, 1:36:13 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==len(set(nums)):
            return False
        else:
            for i in range(len(nums)):
                if nums[i] in nums[i+1:i+1+k]:
                    return True
            return False


        