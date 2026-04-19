# Last updated: 19/04/2026, 17:38:35
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        i = 0
        for j in range(n):
            if nums1[i] > nums2[j]:
                i += 1
                if i >= m:
                    break

        return max(j - i, 0)
