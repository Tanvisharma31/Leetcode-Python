# Last updated: 08/03/2026, 19:49:05
1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        return "".join('1' if x[i]=='0' else '0' for i, x in enumerate(nums))