# Last updated: 02/03/2026, 14:00:30
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
	    temp = sorted(nums)
	    mapping = {}
	    result = []
	    for i in range(len(temp)):
		    if temp[i] not in mapping:
			    mapping[temp[i]] = i
	    for i in range(len(nums)):
		    result.append(mapping[nums[i]])
	    return result