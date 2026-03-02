# Last updated: 02/03/2026, 14:00:35
class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))