# Last updated: 02/03/2026, 13:59:42
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        anslist=[]
        for i in range(len(nums)):
            anslist.append(nums[nums[i]])
        return anslist
        