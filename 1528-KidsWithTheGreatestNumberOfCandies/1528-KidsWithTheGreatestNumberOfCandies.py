# Last updated: 02/03/2026, 14:00:23
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        currMax = max(candies)
        ans = []
        for i in candies:
            if i + extraCandies >= currMax:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans