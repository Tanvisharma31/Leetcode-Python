# Last updated: 02/03/2026, 13:55:58
import bisect

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def ge(arr):
            if not arr:
                return 0
            t=[]
            for x in arr:
                idx=bisect.bisect_left(t,x)
                if idx==len(t):
                    t.append(x)
                else:
                    t[idx]=x
            return len(t)
        max_l=0
        for bit in range(31):
            c=[num for num in nums if (num>>bit) &1]
            c_l=ge(c)
            max_l=max(max_l,c_l)
        return max_l